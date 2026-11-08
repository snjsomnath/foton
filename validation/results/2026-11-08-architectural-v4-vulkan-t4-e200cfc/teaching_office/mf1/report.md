# Foton report

Status: **passed**

```json
{
  "scene": "teaching_office",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_office",
    "category": "teaching",
    "question": "How is a 12 x 8 m open-plan office with a ribbon window lit?",
    "interactions": [
      "multiple_bounces",
      "room",
      "side_glazing",
      "window"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 0,
    "sensors": 96,
    "floor_area": 96.0,
    "aperture_area": 17.6
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "578893ea413954ea7d3a1c7b21acd5b4cb1b64c1f0d5e0c42a96eecaf26a9ddc",
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
      "scene_fingerprint": 17113111844658936175,
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
      "solver_version": "0.3.5",
      "scene_fingerprint": 17113111844658936175,
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
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:1",
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
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "825ad310dbb74f08c550af303c2dbd0c86b8b317ca49c6afd9c865e96c466ecd",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "4265e63cc63ede966c40bbb0f0c0b2ace848568cf0a2cd56b667f1cf881eec43",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00034570228308439255,
          "p95": 3.073783591389656e-05,
          "p99": 0.0001424197107553482
        },
        "bias_percent": -0.08361818512771475,
        "identifier": "teaching_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.990511182857689,
        "worst_index": [
          86,
          95,
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
          "maximum": 0.000872977077960968,
          "p95": 9.63973579928279e-05,
          "p99": 0.0001896405592560768
        },
        "bias_percent": 0.04752275213019179,
        "identifier": "teaching_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7014417079044841,
        "worst_index": [
          37,
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
          "maximum": 0.0007426664233207703,
          "p95": 8.049586322158648e-05,
          "p99": 0.0001579965464770794
        },
        "bias_percent": -0.005446764394493093,
        "identifier": "teaching_office_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6077462427773319,
        "worst_index": [
          14,
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
            "identifier": "teaching_office_grid",
            "sensor_count": 96,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008506275480613112,
                  "p50": 0.0,
                  "p90": 8.857017382979393e-05,
                  "p95": 0.00018153599812649205,
                  "p99": 0.00037834455724805593
                },
                "candidate_energy": 37.11127013896294,
                "cvrmse_percent": 8.984320633906258,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0007702121057195087,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 37.11098430566926,
                "relative_energy_error_percent": 0.0007702121057195087,
                "rms_normalized_rmse_percent": 2.720782163722853,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0030734684551134706,
                  "global_sensor_index": 73,
                  "local_sensor_index": 73,
                  "reference": 0.0022228409070521593,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0017045382410287857,
                  "p50": 0.0,
                  "p90": 0.00014132066280581057,
                  "p95": 0.0002906929170421791,
                  "p99": 0.0006043434841558337
                },
                "candidate_energy": 15.4765159647723,
                "cvrmse_percent": 34.872987602911216,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.22278005686349067,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 15.511071538766501,
                "relative_energy_error_percent": 0.22278005686349067,
                "rms_normalized_rmse_percent": 2.3804914877046723,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06025893986225128,
                  "global_sensor_index": 44,
                  "local_sensor_index": 44,
                  "reference": 0.058554401621222496,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 182.95079201925546,
            "full": 481.06483300216496
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.0744170062244,
            "full": 481.29220900591463
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.6917500216514,
            "full": 482.73358296137303
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 175.2189580583945,
            "full": 490.9423750359565
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
            "identifier": "teaching_office_grid",
            "sensor_count": 96,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006324499263428152,
                  "p50": 0.0,
                  "p90": 5.0809059757739305e-05,
                  "p95": 0.00011667623730318156,
                  "p99": 0.0002327000256627798
                },
                "candidate_energy": 37.067603742288156,
                "cvrmse_percent": 5.506104534955863,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.027130472047387576,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 37.07766308730788,
                "relative_energy_error_percent": 0.027130472047387576,
                "rms_normalized_rmse_percent": 1.6679846772852844,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018244640086777508,
                  "global_sensor_index": 70,
                  "local_sensor_index": 70,
                  "reference": 0.002456913935020566,
                  "rgb_channel": 0,
                  "sky_patch_index": 15
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012942217290401459,
                  "p50": 4.03882268074085e-07,
                  "p90": 9.786942973732948e-05,
                  "p95": 0.00019056759192608342,
                  "p99": 0.00037009455263614655
                },
                "candidate_energy": 26.793466498608684,
                "cvrmse_percent": 12.97747339395714,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.007616999451379286,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 26.795507512268887,
                "relative_energy_error_percent": 0.007616999451379286,
                "rms_normalized_rmse_percent": 1.2814697659371104,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06714986637234688,
                  "global_sensor_index": 93,
                  "local_sensor_index": 93,
                  "reference": 0.06844408810138702,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 262.6795000396669,
            "full": 5655.657625058666
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 267.57645804900676,
            "full": 5502.723083016463
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 263.1268328987062,
            "full": 5573.681040899828
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 262.7902500098571,
            "full": 5656.6507909446955
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
            "identifier": "teaching_office_grid",
            "sensor_count": 96,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004005038645118475,
                  "p50": 0.0,
                  "p90": 6.104167550802231e-05,
                  "p95": 0.00011678505688905716,
                  "p99": 0.00023119745310395956
                },
                "candidate_energy": 37.1056172886465,
                "cvrmse_percent": 5.53625168514501,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.029833047327744854,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 37.09455085373429,
                "relative_energy_error_percent": 0.029833047327744854,
                "rms_normalized_rmse_percent": 1.6767243904188884,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0077223083935678005,
                  "global_sensor_index": 61,
                  "local_sensor_index": 61,
                  "reference": 0.007321804529055953,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013689547777175903,
                  "p50": 3.63372265610451e-07,
                  "p90": 9.552598930895329e-05,
                  "p95": 0.0001882856100564825,
                  "p99": 0.0003736380022019148
                },
                "candidate_energy": 26.78877796404664,
                "cvrmse_percent": 12.978218675281656,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.06423812952413098,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 26.805997635527987,
                "relative_energy_error_percent": 0.06423812952413098,
                "rms_normalized_rmse_percent": 1.2814329262477961,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.09145251661539078,
                  "global_sensor_index": 69,
                  "local_sensor_index": 69,
                  "reference": 0.09008356183767319,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 265.331375063397,
            "full": 5964.290624950081
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 277.14408398605883,
            "full": 5900.130500085652
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 262.95020803809166,
            "full": 5966.4519999641925
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 266.3335420656949,
            "full": 5863.209666102193
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
            "identifier": "teaching_office_grid",
            "sensor_count": 96,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00028844852931797504,
                  "p50": 0.0,
                  "p90": 3.337068483233452e-05,
                  "p95": 6.813640939071775e-05,
                  "p99": 0.0001272745430469513
                },
                "candidate_energy": 37.088399122369765,
                "cvrmse_percent": 3.1773372949284764,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.012439263563261036,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 37.083786172468535,
                "relative_energy_error_percent": 0.012439263563261036,
                "rms_normalized_rmse_percent": 0.9623658951148601,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005529705435037613,
                  "global_sensor_index": 79,
                  "local_sensor_index": 79,
                  "reference": 0.005241256905719638,
                  "rgb_channel": 0,
                  "sky_patch_index": 45
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008514001965522766,
                  "p50": 2.6539319541996065e-07,
                  "p90": 5.664152558892965e-05,
                  "p95": 0.00010525281686568648,
                  "p99": 0.00021642091451212764
                },
                "candidate_energy": 26.808991184546482,
                "cvrmse_percent": 7.664220104526663,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.008148128107849904,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 26.806806931576073,
                "relative_energy_error_percent": 0.008148128107849904,
                "rms_normalized_rmse_percent": 0.756934934269358,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.09147404506802559,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.09062264487147331,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 437.7314579905942,
            "full": 10480.278374976479
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 455.6479159509763,
            "full": 10338.828334002756
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 449.41095903050154,
            "full": 10452.580749988556
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
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "96",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 449.06850007828325,
            "full": 10425.176042015664
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
    "/content/suite-vulkan/teaching_office/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4352.439292008057,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_office/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 16512.052582926117,
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
      96,
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
        "identifier": "teaching_office_grid",
        "full_identifier": "teaching_office_grid",
        "start_sensor_index": 0,
        "sensor_count": 96,
        "stages": {
          "direct": {
            "nmbe_percent": -0.00038932480942579936,
            "cvrmse_percent": 1.7219356756553075,
            "rms_normalized_rmse_percent": 0.5216888627342711,
            "reference_energy": 37.09276737671553,
            "candidate_energy": 37.09262296536963,
            "relative_energy_error_percent": 0.00038932480942579936,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.820728695951402e-06,
              "p95": 1.7230864614248276e-05,
              "p99": 7.874239236116409e-05,
              "maximum": 0.0002032015472650528
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.00414408789947629,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.821300226167945,
            "cvrmse_percent": 31.932995343316257,
            "rms_normalized_rmse_percent": 3.1528768863706302,
            "reference_energy": 26.801224231430965,
            "candidate_energy": 26.31309347388813,
            "relative_energy_error_percent": 1.821300226167958,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1371899972800747e-06,
              "p90": 5.748809780925512e-05,
              "p95": 9.064063197001819e-05,
              "p99": 0.0002140405122190714,
              "maximum": 0.004980042576789856
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.09431495517492294,
              "candidate": 0.08933491259813309,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.7641957508043294,
            "cvrmse_percent": 13.388973681277388,
            "rms_normalized_rmse_percent": 3.1515197350600506,
            "reference_energy": 63.89399160814649,
            "candidate_energy": 63.40571643925776,
            "relative_energy_error_percent": 0.764195750804335,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1565036288629926e-06,
              "p90": 5.6847056839615107e-05,
              "p95": 8.750692941248423e-05,
              "p99": 0.00021646730601787567,
              "maximum": 0.004980042576789856
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.09431495517492294,
              "candidate": 0.08933491259813309,
              "position": [
                5.5,
                2.5,
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
      96,
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
        "identifier": "teaching_office_grid",
        "full_identifier": "teaching_office_grid",
        "start_sensor_index": 0,
        "sensor_count": 96,
        "stages": {
          "direct": {
            "nmbe_percent": -0.00038932480942579936,
            "cvrmse_percent": 1.7219356756553075,
            "rms_normalized_rmse_percent": 0.5216888627342711,
            "reference_energy": 37.09276737671553,
            "candidate_energy": 37.09262296536963,
            "relative_energy_error_percent": 0.00038932480942579936,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.820728695951402e-06,
              "p95": 1.7230864614248276e-05,
              "p99": 7.874239236116409e-05,
              "maximum": 0.0002032015472650528
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.00414408789947629,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 69.62888745105147,
            "cvrmse_percent": 307.2274341726809,
            "rms_normalized_rmse_percent": 20.986013072372614,
            "reference_energy": 15.51215354252742,
            "candidate_energy": 26.31309347388813,
            "relative_energy_error_percent": 69.62888745105147,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.699999868127634e-07,
              "p90": 0.0006365403532981873,
              "p95": 0.0008662747452035566,
              "p99": 0.001310950145125389,
              "maximum": 0.01882752776145935
            },
            "worst": {
              "global_sensor_index": 95,
              "local_sensor_index": 95,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.053234174847602844,
              "candidate": 0.0720617026090622,
              "position": [
                11.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.53191095296156,
            "cvrmse_percent": 90.59780931989837,
            "rms_normalized_rmse_percent": 20.986591971106854,
            "reference_energy": 52.60492091924295,
            "candidate_energy": 63.40571643925776,
            "relative_energy_error_percent": 20.531910952961557,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.444819671154619e-07,
              "p90": 0.0006402099970728159,
              "p95": 0.0008667402085848162,
              "p99": 0.0013003824278712273,
              "maximum": 0.01882752776145935
            },
            "worst": {
              "global_sensor_index": 95,
              "local_sensor_index": 95,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.053234174847602844,
              "candidate": 0.0720617026090622,
              "position": [
                11.5,
                0.5,
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
      "bias_percent": 0.17876085110901335,
      "rms_normalized_error_percent": 0.2293020246061048,
      "absolute_error": {
        "p95": 0.18845453672481982,
        "p99": 0.22187701045459424,
        "maximum": 0.2596984679108889
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 28.442747190351625,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2293020246061048
    },
    "overcast": {
      "bias_percent": 0.1474031517989201,
      "rms_normalized_error_percent": 0.1964068652055662,
      "absolute_error": {
        "p95": 0.09593737125396729,
        "p99": 0.159147834777832,
        "maximum": 0.16216659545898438
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.109018325805664,
      "reference_fraction_of_uniform": 0.6366831660270691,
      "rms_normalized_to_uniform_percent": 0.13665107456451012
    },
    "horizon": {
      "bias_percent": 0.8302509062886565,
      "rms_normalized_error_percent": 1.968041504598496,
      "absolute_error": {
        "p95": 0.13620695360675816,
        "p99": 0.16911604565123808,
        "maximum": 0.20400979028833355
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7815484352744213,
      "reference_fraction_of_uniform": 0.09779464749516112,
      "rms_normalized_to_uniform_percent": 0.14305402057044167
    },
    "north": {
      "bias_percent": -49.22422461260941,
      "rms_normalized_error_percent": 101.28708508698833,
      "absolute_error": {
        "p95": 0.0001436321192613832,
        "p99": 0.00023540640331702823,
        "maximum": 0.0004544466228253441
      },
      "worst_index": [
        92
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 3.883660610881634e-05,
      "reference_fraction_of_uniform": 1.3654308759214473e-06,
      "rms_normalized_to_uniform_percent": 0.00018806833771501928
    },
    "east": {
      "bias_percent": 0.057578982856919717,
      "rms_normalized_error_percent": 0.2659781437690086,
      "absolute_error": {
        "p95": 0.045823484659194946,
        "p99": 0.05963244438171383,
        "maximum": 0.07318878173828125
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.8586106300354,
      "reference_fraction_of_uniform": 0.20597906410694122,
      "rms_normalized_to_uniform_percent": 0.05759772126875478
    },
    "south": {
      "bias_percent": 0.22377205830320976,
      "rms_normalized_error_percent": 0.29973063979693965,
      "absolute_error": {
        "p95": 0.16717016696929932,
        "p99": 0.19906771183013905,
        "maximum": 0.23926877975463867
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 19.54828643798828,
      "reference_fraction_of_uniform": 0.6872854828834534,
      "rms_normalized_to_uniform_percent": 0.1895762614130184
    },
    "west": {
      "bias_percent": 0.1652516223473207,
      "rms_normalized_error_percent": 0.2870344012893914,
      "absolute_error": {
        "p95": 0.04439544677734375,
        "p99": 0.06110975742340082,
        "maximum": 0.08090066909790039
      },
      "worst_index": [
        68
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.66806173324585,
      "reference_fraction_of_uniform": 0.19927968084812164,
      "rms_normalized_to_uniform_percent": 0.060085794421858844
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
        "identifier": "teaching_office_grid",
        "sensor_count": 96,
        "illuminance": {
          "nmbe_percent": 0.04013081917284023,
          "cvrmse_percent": 1.0768608440382992,
          "absolute_error_percentiles_lux": {
            "p50": 4.22149658203125,
            "p90": 36.76127929687502,
            "p95": 55.214965820312415,
            "p99": 111.78062500000033
          },
          "maximum_absolute_error_lux": 448.623046875,
          "worst": {
            "sensor_index": 54,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 13340.6318359375,
            "radiance_lux": 12892.0087890625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.09595176940639279,
            "maximum_error_percentage_points": 0.7153424657534231,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.03874055672328591,
            "maximum_error_percentage_points": 0.3199208667398068,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.03320633561643821,
            "maximum_error_percentage_points": 0.22342465753424534,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0797345890410965,
            "maximum_error_percentage_points": 0.4887671232876656,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.08092465753424664,
            "maximum_error_percentage_points": 0.5231506849315082,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0,
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
      "maximum_error_percentage_points": 0.004997859589039422,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004997859589039422,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_office_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
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
      "study_preparation_seconds": 0.36954726800013304,
      "weather_seconds": 0.22345464999989417,
      "metric_reduction_seconds": 0.14312354399999094,
      "write_seconds": 0.014064732999941043,
      "total_seconds": 0.3809761049997178,
      "cold_end_to_end_seconds": 0.7505233729998508,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0029404199999589764,
      "engine_upload_seconds": 0.026676322,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.020288421,
      "engine_annual_reduction_seconds": 0.007069341,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.020288421
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.36954726800013304,
      "weather_seconds": 0.22688028099992152,
      "metric_reduction_seconds": 0.11993892200007394,
      "write_seconds": 0.013765365999915957,
      "total_seconds": 0.36084804200027065,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.36084804200027065,
      "raw_export_seconds": 0.002799782000238338,
      "engine_upload_seconds": 0.023964213,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5e-08,
      "engine_annual_reduction_seconds": 0.007214296,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.022490354000183288,
      "full": 0.04005122299986397
    }
  },
  "elapsed_seconds": 3.2519397259998186,
  "result_class": "passed"
}
```
