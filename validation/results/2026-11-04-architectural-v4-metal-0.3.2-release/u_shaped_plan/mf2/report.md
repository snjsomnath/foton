# Foton report

Status: **passed**

```json
{
  "scene": "u_shaped_plan",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "u_shaped_plan",
    "category": "form",
    "question": "Do the wings of a U-shaped room occlude one another?",
    "interactions": [
      "concave_plan",
      "self_occlusion",
      "multiple_openings"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 3,
    "shades": 0,
    "sensors": 53,
    "floor_area": 63.0,
    "aperture_area": 9.0
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "9e5fdc72726f7e91db50f61fdada00cb29e89250e097643c5313da21dca02bd8",
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
      "scene_fingerprint": 6169704301367242066,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 6169704301367242066,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "a42ccfeab8ae79ba3fcaa01e5cba3aeca3609463ed2b42d1d5355c23044cd9f2",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "41ef2f2774bff44b552e4bcb5440641cfa316a6a7716fe665a18b2f1b83a474a",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00019046594388782978,
          "p95": 2.674838469829244e-07,
          "p99": 1.4548982107953634e-05
        },
        "bias_percent": -0.013317759312156598,
        "identifier": "u_shaped_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8538041362104279,
        "worst_index": [
          47,
          281,
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
          "maximum": 0.0005627721548080444,
          "p95": 3.3925913885468445e-05,
          "p99": 0.00010293093509972095
        },
        "bias_percent": 0.04756795411670592,
        "identifier": "u_shaped_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.338651421892052,
        "worst_index": [
          29,
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
          "maximum": 0.000541292130947113,
          "p95": 2.862757428374602e-05,
          "p99": 8.627492934465408e-05
        },
        "bias_percent": 0.007311363497802743,
        "identifier": "u_shaped_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1170791093200718,
        "worst_index": [
          39,
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
            "identifier": "u_shaped_plan_grid",
            "sensor_count": 53,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007853979477658868,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.717061528936023e-05,
                  "p99": 0.00021517055574804544
                },
                "candidate_energy": 11.555479662812274,
                "cvrmse_percent": 31.389309544480582,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.014022234810719666,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.553859553495982,
                "relative_energy_error_percent": 0.014022234810719665,
                "rms_normalized_rmse_percent": 6.760443291928425,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001847783976700157,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": 0.0010623860289342701,
                  "rgb_channel": 0,
                  "sky_patch_index": 229
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001653779298067093,
                  "p50": 0.0,
                  "p90": 2.33726004807977e-05,
                  "p95": 9.20037738069367e-05,
                  "p99": 0.00033514201641082764
                },
                "candidate_energy": 3.5214003569611485,
                "cvrmse_percent": 165.5891463470802,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.247681683971419,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.5127000423434076,
                "relative_energy_error_percent": 0.24768168397141901,
                "rms_normalized_rmse_percent": 5.372475333027485,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.045913685113191605,
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "reference": 0.0475674644112587,
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.4512919774279,
            "full": 317.3624579794705
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.76612498704344,
            "full": 329.4857500586659
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 141.38429192826152,
            "full": 322.6335420040414
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.05099994596094,
            "full": 320.19329199101776
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
            "identifier": "u_shaped_plan_grid",
            "sensor_count": 53,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000388765474781394,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.2684923391789165e-05,
                  "p99": 0.00014740147162228823
                },
                "candidate_energy": 11.567272383444667,
                "cvrmse_percent": 21.503570049203226,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.048034248878882434,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.561718798662241,
                "relative_energy_error_percent": 0.04803424887888244,
                "rms_normalized_rmse_percent": 4.631858075760141,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0028894220013171434,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.0025006565265357494,
                  "rgb_channel": 0,
                  "sky_patch_index": 353
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009897798299789429,
                  "p50": 2.066766910502338e-06,
                  "p90": 2.179119019274367e-05,
                  "p95": 6.259011988731791e-05,
                  "p99": 0.00021131389621587005
                },
                "candidate_energy": 6.793416848748937,
                "cvrmse_percent": 55.95370526975801,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.08536004030743174,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.799220666250239,
                "relative_energy_error_percent": 0.08536004030743174,
                "rms_normalized_rmse_percent": 2.592103904741095,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05645694024860859,
                  "global_sensor_index": 46,
                  "local_sensor_index": 46,
                  "reference": 0.05744672007858753,
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 204.10054200328887,
            "full": 3782.6855829916894
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 200.78441605437547,
            "full": 3807.9567910172045
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 198.21566704194993,
            "full": 3779.5392910484225
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.3823329685256,
            "full": 3691.5313329081982
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
            "identifier": "u_shaped_plan_grid",
            "sensor_count": 53,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004564794944599271,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.126326584810126e-05,
                  "p99": 0.00013731804210692644
                },
                "candidate_energy": 11.558916641180232,
                "cvrmse_percent": 20.430636878477596,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01483419944540225,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.560631568324226,
                "relative_energy_error_percent": 0.014834199445402253,
                "rms_normalized_rmse_percent": 4.4033269082782285,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035621559945866466,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0031056765001267195,
                  "rgb_channel": 0,
                  "sky_patch_index": 263
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011676587164402008,
                  "p50": 2.0932952509156166e-06,
                  "p90": 2.1529795048991218e-05,
                  "p95": 6.0301610119495064e-05,
                  "p99": 0.00020194763783365488
                },
                "candidate_energy": 6.815963860490392,
                "cvrmse_percent": 54.206457883902985,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1819563505531093,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.803584306778973,
                "relative_energy_error_percent": 0.1819563505531093,
                "rms_normalized_rmse_percent": 2.5127859373466075,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06275858357548714,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": 0.061590924859046936,
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 218.85562490206212,
            "full": 3964.2379159340635
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 205.07629204075783,
            "full": 4073.92495800741
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.4023340139538,
            "full": 4040.2825420023873
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 212.14883401989937,
            "full": 4005.134209059179
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
            "identifier": "u_shaped_plan_grid",
            "sensor_count": 53,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000260457512922585,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.197769936174149e-05,
                  "p99": 7.807393558323383e-05
                },
                "candidate_energy": 11.562751185333592,
                "cvrmse_percent": 11.636279519054302,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0018059247324674216,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.562960003688104,
                "relative_energy_error_percent": 0.0018059247324674213,
                "rms_normalized_rmse_percent": 2.5087783047368224,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018134944839403033,
                  "global_sensor_index": 47,
                  "local_sensor_index": 47,
                  "reference": 0.0015530369710177183,
                  "rgb_channel": 0,
                  "sky_patch_index": 138
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008653141558170319,
                  "p50": 1.511058897563089e-06,
                  "p90": 1.4509021639241837e-05,
                  "p95": 3.5342855699127524e-05,
                  "p99": 0.00011857855133712292
                },
                "candidate_energy": 6.811881249733464,
                "cvrmse_percent": 31.88632137579884,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.11303420501550573,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.80419018744734,
                "relative_energy_error_percent": 0.11303420501550575,
                "rms_normalized_rmse_percent": 1.4779397413497,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07492992654442787,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.07406461238861084,
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 321.39554095920175,
            "full": 7189.441499998793
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 318.478083005175,
            "full": 7210.058375028893
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 304.5430419733748,
            "full": 7111.2439159769565
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
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "53",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 326.9439999712631,
            "full": 7060.415500076488
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/u_shaped_plan/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 6160.3016249137,
      "invocation_count": 4,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/u_shaped_plan/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 23874.25379198976,
      "invocation_count": 4,
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
      53,
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
        "identifier": "u_shaped_plan_grid",
        "full_identifier": "u_shaped_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 53,
        "stages": {
          "direct": {
            "nmbe_percent": -0.17310721115045677,
            "cvrmse_percent": 3.2722385765894244,
            "rms_normalized_rmse_percent": 0.7055904830932875,
            "reference_energy": 11.565094779794606,
            "candidate_energy": 11.545074766754396,
            "relative_energy_error_percent": 0.1731072111504568,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.2469764593988233e-07,
              "p99": 1.6958691048785113e-05,
              "maximum": 0.00010280654532834888
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 165,
              "rgb_channel": 0,
              "reference": 0.00010280654532834888,
              "candidate": 0.0,
              "position": [
                7.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.3469007085189607,
            "cvrmse_percent": 25.113878643561513,
            "rms_normalized_rmse_percent": 1.1643055048733235,
            "reference_energy": 6.805796501107531,
            "candidate_energy": 6.782187144824831,
            "relative_energy_error_percent": 0.34690070851896077,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.967077650988358e-06,
              "p90": 1.3177072105463594e-05,
              "p95": 2.2015568174538158e-05,
              "p99": 5.3761061280965805e-05,
              "maximum": 0.0008064769208431244
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.040587928146123886,
              "candidate": 0.03978145122528076,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.2374918486849141,
            "cvrmse_percent": 9.161134451857816,
            "rms_normalized_rmse_percent": 1.1464462138540241,
            "reference_energy": 18.370891280902136,
            "candidate_energy": 18.327261911579228,
            "relative_energy_error_percent": 0.23749184868489956,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.9680264813359827e-06,
              "p90": 1.2978642189409584e-05,
              "p95": 2.1215400556684453e-05,
              "p99": 5.08833909407258e-05,
              "maximum": 0.0008064769208431244
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.040587928146123886,
              "candidate": 0.03978145122528076,
              "position": [
                5.5,
                0.5,
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
      53,
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
        "identifier": "u_shaped_plan_grid",
        "full_identifier": "u_shaped_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 53,
        "stages": {
          "direct": {
            "nmbe_percent": -0.17310721115045677,
            "cvrmse_percent": 3.2722385765894244,
            "rms_normalized_rmse_percent": 0.7055904830932875,
            "reference_energy": 11.565094779794606,
            "candidate_energy": 11.545074766754396,
            "relative_energy_error_percent": 0.1731072111504568,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.2469764593988233e-07,
              "p99": 1.6958691048785113e-05,
              "maximum": 0.00010280654532834888
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 38,
              "sky_patch_index": 165,
              "rgb_channel": 0,
              "reference": 0.00010280654532834888,
              "candidate": 0.0,
              "position": [
                7.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 93.41067509515086,
            "cvrmse_percent": 1223.856700023308,
            "rms_normalized_rmse_percent": 39.622003830038345,
            "reference_energy": 3.5066250306443774,
            "candidate_energy": 6.782187144824831,
            "relative_energy_error_percent": 93.41067509515085,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.920000254875049e-06,
              "p90": 5.973014049232006e-05,
              "p95": 8.033860322029788e-05,
              "p99": 0.0001604398712515831,
              "maximum": 0.021875660866498947
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03488554060459137,
              "candidate": 0.05676120147109032,
              "position": [
                8.5,
                6.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.600335874645097,
            "cvrmse_percent": 284.7299827657765,
            "rms_normalized_rmse_percent": 39.61982482306094,
            "reference_energy": 15.071719810438983,
            "candidate_energy": 18.327261911579228,
            "relative_energy_error_percent": 21.600335874645104,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.8400001914124e-06,
              "p90": 5.9416741351014934e-05,
              "p95": 7.973618876349058e-05,
              "p99": 0.00015766406431794167,
              "maximum": 0.021875660866498947
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 46,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03488554060459137,
              "candidate": 0.05676120147109032,
              "position": [
                8.5,
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
      "bias_percent": 0.010284855660004113,
      "rms_normalized_error_percent": 0.16450666732928768,
      "absolute_error": {
        "p95": 0.07918074717092764,
        "p99": 0.1318224917102392,
        "maximum": 0.14635125067830046
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.549522931461407,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.16450666732928768
    },
    "overcast": {
      "bias_percent": 0.029657956432618177,
      "rms_normalized_error_percent": 0.1285527924260506,
      "absolute_error": {
        "p95": 0.04357719421386718,
        "p99": 0.07542114257812499,
        "maximum": 0.07636833190917969
      },
      "worst_index": [
        39
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.31730842590332,
      "reference_fraction_of_uniform": 0.6635128259658813,
      "rms_normalized_to_uniform_percent": 0.08982496506386284
    },
    "horizon": {
      "bias_percent": -0.032485783767849184,
      "rms_normalized_error_percent": 1.4035741378314104,
      "absolute_error": {
        "p95": 0.04543946091125854,
        "p99": 0.07167562173578781,
        "maximum": 0.07287818034489657
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3328762631573166,
      "reference_fraction_of_uniform": 0.0857181451181697,
      "rms_normalized_to_uniform_percent": 0.08486404077059169
    },
    "north": {
      "bias_percent": -0.11320183707212202,
      "rms_normalized_error_percent": 0.24550090568896363,
      "absolute_error": {
        "p95": 0.019645673036575315,
        "p99": 0.03132225036621088,
        "maximum": 0.04070091247558594
      },
      "worst_index": [
        39
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.0225021839141846,
      "reference_fraction_of_uniform": 0.13006843626499176,
      "rms_normalized_to_uniform_percent": 0.042069342022121495
    },
    "east": {
      "bias_percent": -0.027097770869704312,
      "rms_normalized_error_percent": 0.22739530049710763,
      "absolute_error": {
        "p95": 0.06294047832489011,
        "p99": 0.08763519287109374,
        "maximum": 0.08906316757202148
      },
      "worst_index": [
        37
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.750888347625732,
      "reference_fraction_of_uniform": 0.36984339356422424,
      "rms_normalized_to_uniform_percent": 0.0982478226054111
    },
    "south": {
      "bias_percent": 0.08328891682577469,
      "rms_normalized_error_percent": 0.19033538342446438,
      "absolute_error": {
        "p95": 0.04567890167236328,
        "p99": 0.058171844482421874,
        "maximum": 0.05865287780761719
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.050959587097168,
      "reference_fraction_of_uniform": 0.38914117217063904,
      "rms_normalized_to_uniform_percent": 0.08186649311364674
    },
    "west": {
      "bias_percent": -0.12669267603151244,
      "rms_normalized_error_percent": 0.31568578324502367,
      "absolute_error": {
        "p95": 0.025638771057128903,
        "p99": 0.06930242538452142,
        "maximum": 0.08105897903442383
      },
      "worst_index": [
        48
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.793484687805176,
      "reference_fraction_of_uniform": 0.17965082824230194,
      "rms_normalized_to_uniform_percent": 0.06090154962720691
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
        "identifier": "u_shaped_plan_grid",
        "sensor_count": 53,
        "illuminance": {
          "nmbe_percent": -0.02836085991430202,
          "cvrmse_percent": 1.7535177015242625,
          "absolute_error_percentiles_lux": {
            "p50": 2.233367919921875,
            "p90": 23.061651611328127,
            "p95": 37.18330078124998,
            "p99": 86.14621093749997
          },
          "maximum_absolute_error_lux": 448.384765625,
          "worst": {
            "sensor_index": 27,
            "position": [
              3.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5243.5,
            "foton_lux": 8174.197265625,
            "radiance_lux": 7725.8125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.13896872576893282,
            "maximum_error_percentage_points": 0.7376712328767141,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.13576613954882966,
            "maximum_error_percentage_points": 0.49880814891434966,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.20068234685965405,
            "maximum_error_percentage_points": 1.423013698630136,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.21062289997415382,
            "maximum_error_percentage_points": 1.423013698630136,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.02157405014215557,
            "maximum_error_percentage_points": 0.25,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 49.056603773584904,
          "radiance_percent": 49.056603773584904,
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
      "maximum_error_percentage_points": 0.004991438356164224,
      "metrics": {
        "da": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004991438356164224,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "u_shaped_plan_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
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
      "study_preparation_seconds": 0.007339000003412366,
      "weather_seconds": 0.08545870799571276,
      "metric_reduction_seconds": 0.14994562498759478,
      "write_seconds": 0.01825199997983873,
      "total_seconds": 0.2538052500458434,
      "cold_end_to_end_seconds": 0.2611442500492558,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002152874949388206,
      "engine_upload_seconds": 0.00098725,
      "engine_acceleration_structure_seconds": 0.003356458,
      "engine_tracing_seconds": 0.08209045825060457,
      "engine_annual_reduction_seconds": 0.0026978333480656147,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.08209045825060457
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007339000003412366,
      "weather_seconds": 0.08038308296818286,
      "metric_reduction_seconds": 0.05204537510871887,
      "write_seconds": 0.018107083975337446,
      "total_seconds": 0.15087866701651365,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15087866701651365,
      "raw_export_seconds": 0.0018447909969836473,
      "engine_upload_seconds": 5.6542e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0023261666065081954,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015627791988663375,
      "full": 0.09077245800290257
    }
  },
  "elapsed_seconds": 1.6535150839481503,
  "result_class": "passed"
}
```
