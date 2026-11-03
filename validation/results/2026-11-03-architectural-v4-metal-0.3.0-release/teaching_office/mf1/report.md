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
  "model_sha256": "ae0bd42e908e8c15d6604192c7a129fbc3ea59ec589babbf839e94091f489982",
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
      "scene_fingerprint": 17113111844658936175,
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
      "solver_version": "0.3.0",
      "scene_fingerprint": 17113111844658936175,
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
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/foton-references-corpus4-2026-11-03",
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
    "/usr/local/radiance/bin/oconv",
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/teaching_office/mf1/oracle/scene.rad"
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
            "nmbe_percent": -0.00038728471907736,
            "cvrmse_percent": 1.7219345116160605,
            "rms_normalized_rmse_percent": 0.5216885100693489,
            "reference_energy": 37.09276737671553,
            "candidate_energy": 37.092623722095595,
            "relative_energy_error_percent": 0.00038728471907736005,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.820728695951402e-06,
              "p95": 1.7230864614248276e-05,
              "p99": 7.874332368373871e-05,
              "maximum": 0.0002032020129263401
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.004144088365137577,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.8212936449067758,
            "cvrmse_percent": 31.932913637693847,
            "rms_normalized_rmse_percent": 3.1528688192361316,
            "reference_energy": 26.801224231430965,
            "candidate_energy": 26.313095237746694,
            "relative_energy_error_percent": 1.821293644906789,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1371899972800747e-06,
              "p90": 5.748809780925512e-05,
              "p95": 9.064063197001819e-05,
              "p99": 0.00021404074504971504,
              "maximum": 0.004979915916919708
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.09431495517492294,
              "candidate": 0.08933503925800323,
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
            "nmbe_percent": -0.7641918058566638,
            "cvrmse_percent": 13.388939058076973,
            "rms_normalized_rmse_percent": 3.151511585391376,
            "reference_energy": 63.89399160814649,
            "candidate_energy": 63.40571895984229,
            "relative_energy_error_percent": 0.7641918058566693,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1565036288629926e-06,
              "p90": 5.6847056839615107e-05,
              "p95": 8.750692941248423e-05,
              "p99": 0.00021646730601787567,
              "maximum": 0.004979915916919708
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 45,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.09431495517492294,
              "candidate": 0.08933503925800323,
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
            "nmbe_percent": -0.00038728471907736,
            "cvrmse_percent": 1.7219345116160605,
            "rms_normalized_rmse_percent": 0.5216885100693489,
            "reference_energy": 37.09276737671553,
            "candidate_energy": 37.092623722095595,
            "relative_energy_error_percent": 0.00038728471907736005,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.820728695951402e-06,
              "p95": 1.7230864614248276e-05,
              "p99": 7.874332368373871e-05,
              "maximum": 0.0002032020129263401
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 100,
              "rgb_channel": 0,
              "reference": 0.003940886352211237,
              "candidate": 0.004144088365137577,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 69.62889882186828,
            "cvrmse_percent": 307.2275283155973,
            "rms_normalized_rmse_percent": 20.986019503062895,
            "reference_energy": 15.51215354252742,
            "candidate_energy": 26.313095237746694,
            "relative_energy_error_percent": 69.62889882186828,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.699999868127634e-07,
              "p90": 0.0006365403532981873,
              "p95": 0.0008662746346090009,
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
            "nmbe_percent": 20.531915744499095,
            "cvrmse_percent": 90.59783810418382,
            "rms_normalized_rmse_percent": 20.986598638862493,
            "reference_energy": 52.60492091924295,
            "candidate_energy": 63.40571895984229,
            "relative_energy_error_percent": 20.531915744499088,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.444819671154619e-07,
              "p90": 0.0006402099970728159,
              "p95": 0.0008667402085848162,
              "p99": 0.0013003833591938019,
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
      "bias_percent": 0.17876330638884333,
      "rms_normalized_error_percent": 0.2293033654393979,
      "absolute_error": {
        "p95": 0.188455021216289,
        "p99": 0.22187711152055928,
        "maximum": 0.2596985095875741
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 28.442747190351625,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.2293033654393979
    },
    "overcast": {
      "bias_percent": 0.1474034691687093,
      "rms_normalized_error_percent": 0.19640626358242755,
      "absolute_error": {
        "p95": 0.09593737125396729,
        "p99": 0.15914440155029297,
        "maximum": 0.16217041015625
      },
      "worst_index": [
        30
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 18.109018325805664,
      "reference_fraction_of_uniform": 0.6366831660270691,
      "rms_normalized_to_uniform_percent": 0.13665064769700294
    },
    "horizon": {
      "bias_percent": 0.830271898471428,
      "rms_normalized_error_percent": 1.968051866551838,
      "absolute_error": {
        "p95": 0.136206974445101,
        "p99": 0.16911604669315522,
        "maximum": 0.20400981112667615
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7815484352744213,
      "reference_fraction_of_uniform": 0.09779464749516112,
      "rms_normalized_to_uniform_percent": 0.14305477376547496
    },
    "north": {
      "bias_percent": -49.22422432713369,
      "rms_normalized_error_percent": 101.28708516118846,
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
      "bias_percent": 0.05757614803737333,
      "rms_normalized_error_percent": 0.26597434900642614,
      "absolute_error": {
        "p95": 0.0458238422870636,
        "p99": 0.05963158607482906,
        "maximum": 0.07318973541259766
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.8586106300354,
      "reference_fraction_of_uniform": 0.20597906410694122,
      "rms_normalized_to_uniform_percent": 0.05759689599157425
    },
    "south": {
      "bias_percent": 0.22377851245478336,
      "rms_normalized_error_percent": 0.2997322960414276,
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
      "rms_normalized_to_uniform_percent": 0.18957732383881404
    },
    "west": {
      "bias_percent": 0.1652560760603212,
      "rms_normalized_error_percent": 0.28703541609814687,
      "absolute_error": {
        "p95": 0.0443958044052124,
        "p99": 0.061110663414001405,
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
      "rms_normalized_to_uniform_percent": 0.06008600785561243
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
          "nmbe_percent": 0.04013411903392791,
          "cvrmse_percent": 1.0768613860599017,
          "absolute_error_percentiles_lux": {
            "p50": 4.221343994140625,
            "p90": 36.76171875,
            "p95": 55.21635742187493,
            "p99": 111.77733398437539
          },
          "maximum_absolute_error_lux": 448.6240234375,
          "worst": {
            "sensor_index": 54,
            "position": [
              6.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 13340.6328125,
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
      "study_preparation_seconds": 0.008525124983862042,
      "weather_seconds": 0.09169916703831404,
      "metric_reduction_seconds": 0.07129304204136133,
      "write_seconds": 0.04229866701643914,
      "total_seconds": 0.20543691597413272,
      "cold_end_to_end_seconds": 0.21396204095799476,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.013424917007796466,
      "engine_upload_seconds": 0.000316834,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0499433750519529,
      "engine_annual_reduction_seconds": 0.0008515416411682963,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0499433750519529
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008525124983862042,
      "weather_seconds": 0.09484633302781731,
      "metric_reduction_seconds": 0.013549999915994704,
      "write_seconds": 0.03483491693623364,
      "total_seconds": 0.14338595909066498,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14338595909066498,
      "raw_export_seconds": 0.01213966601062566,
      "engine_upload_seconds": 5.6792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0007875417359173298,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.0163268749602139,
      "full": 0.05657562497071922
    }
  },
  "elapsed_seconds": 0.9506797080393881,
  "result_class": "passed"
}
```
