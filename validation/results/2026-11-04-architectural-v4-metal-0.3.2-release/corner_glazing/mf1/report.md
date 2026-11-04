# Foton report

Status: **passed**

```json
{
  "scene": "corner_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "corner_glazing",
    "category": "openings",
    "question": "How do windows on adjacent facades combine at a corner?",
    "interactions": [
      "two_aspects",
      "corner_lighting"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 2,
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 5.999999999999998
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "768d9a431a37283f3285abb5319bf98fde235e368ce501eefff9417997e48337",
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
      "scene_fingerprint": 13042834898063816899,
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
      "scene_fingerprint": 13042834898063816899,
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
    "model_sha256": "cbd6b4ef01b0472e470b62f9bd8c33b231781ef08c97ee0eb5b9ecff9b2dddfb",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0005308212712407112,
          "p95": 3.067571960855274e-05,
          "p99": 0.0001428311225026846
        },
        "bias_percent": -0.07382717386617164,
        "identifier": "corner_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1803376929732607,
        "worst_index": [
          32,
          131,
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
          "maximum": 0.0006344355642795563,
          "p95": 8.637374266982068e-05,
          "p99": 0.00016922177746891975
        },
        "bias_percent": 0.04320586121394456,
        "identifier": "corner_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.874069349129269,
        "worst_index": [
          19,
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
          "maximum": 0.0005565546452999115,
          "p95": 6.873151287436478e-05,
          "p99": 0.00014585396274924278
        },
        "bias_percent": -0.0027720248510661907,
        "identifier": "corner_glazing_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7052609278911836,
        "worst_index": [
          28,
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
            "identifier": "corner_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006986994412727654,
                  "p50": 0.0,
                  "p90": 5.847081774845719e-05,
                  "p95": 0.0001416335260728374,
                  "p99": 0.00031144730746746063
                },
                "candidate_energy": 12.033824406966914,
                "cvrmse_percent": 8.387334839324081,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.14072984832815275,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.050783456247245,
                "relative_energy_error_percent": 0.14072984832815277,
                "rms_normalized_rmse_percent": 2.4286826091350258,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0017190810176543891,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0024177804589271545,
                  "rgb_channel": 0,
                  "sky_patch_index": 18
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013528559356927872,
                  "p50": 0.0,
                  "p90": 0.00011510343756526709,
                  "p95": 0.0002454780624248086,
                  "p99": 0.0004996703937649727
                },
                "candidate_energy": 3.9805609342888033,
                "cvrmse_percent": 42.230580210293034,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.5386577915566204,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.9592342107267484,
                "relative_energy_error_percent": 0.5386577915566204,
                "rms_normalized_rmse_percent": 2.7577994462936437,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03467286005616188,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.03602571599185467,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.76562500745058,
            "full": 243.9313749782741
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.9847080539912,
            "full": 233.5063749924302
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.93820799700916,
            "full": 231.64841602556407
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.61045900452882,
            "full": 235.46004109084606
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
            "identifier": "corner_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004000975750386715,
                  "p50": 0.0,
                  "p90": 4.5302556827664375e-05,
                  "p95": 9.740258101373875e-05,
                  "p99": 0.00020696455612778664
                },
                "candidate_energy": 12.047416679766002,
                "cvrmse_percent": 5.534749132690472,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.07316183920927756,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.056237244673639,
                "relative_energy_error_percent": 0.07316183920927756,
                "rms_normalized_rmse_percent": 1.6037277550027507,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004547426011413336,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.004147328436374664,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009285062551498413,
                  "p50": 5.675744432664942e-06,
                  "p90": 7.687800098210573e-05,
                  "p95": 0.00015991894797480195,
                  "p99": 0.0003429139032959938
                },
                "candidate_energy": 7.193627484976776,
                "cvrmse_percent": 16.59538129566869,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.17034993509158408,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.181393984984684,
                "relative_energy_error_percent": 0.1703499350915841,
                "rms_normalized_rmse_percent": 1.604271471810324,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04455246962606907,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.04548097588121891,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.09545807819813,
            "full": 2326.3497090665624
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.2159579526633,
            "full": 2321.130166994408
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 163.0870410008356,
            "full": 2288.5116250254214
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.42179204244167,
            "full": 2278.474749997258
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
            "identifier": "corner_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00043545011430978775,
                  "p50": 0.0,
                  "p90": 4.386965883895755e-05,
                  "p95": 0.00011264503700658678,
                  "p99": 0.0002209572121500969
                },
                "candidate_energy": 12.04670414016914,
                "cvrmse_percent": 6.002311503993656,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.022224390941809027,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.044027428428308,
                "relative_energy_error_percent": 0.02222439094180903,
                "rms_normalized_rmse_percent": 1.7368240646224176,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013932545203715563,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.013497095089405775,
                  "rgb_channel": 0,
                  "sky_patch_index": 67
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00097610242664814,
                  "p50": 5.458680789161008e-06,
                  "p90": 8.111295755952597e-05,
                  "p95": 0.00017742727650329467,
                  "p99": 0.0003539430908858776
                },
                "candidate_energy": 7.202445563199465,
                "cvrmse_percent": 16.776121103429602,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.004473164101267798,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.202123400400989,
                "relative_energy_error_percent": 0.004473164101267798,
                "rms_normalized_rmse_percent": 1.6261929450676909,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05541192926466465,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.05638803169131279,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.37616701517254,
            "full": 2417.2305420506746
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.73220791481435,
            "full": 2425.040042027831
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.64941707998514,
            "full": 2419.8596250498667
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.59200005233288,
            "full": 2395.168749964796
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
            "identifier": "corner_glazing_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024473387748003006,
                  "p50": 0.0,
                  "p90": 2.309249248355627e-05,
                  "p95": 4.984652623534191e-05,
                  "p99": 0.00010548694990575314
                },
                "candidate_energy": 12.050058527556303,
                "cvrmse_percent": 2.9391082511750035,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.047228706103687915,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 12.044370127386799,
                "relative_energy_error_percent": 0.047228706103687915,
                "rms_normalized_rmse_percent": 0.850922337847277,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.018231329508125782,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.017986595630645752,
                  "rgb_channel": 0,
                  "sky_patch_index": 133
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008538383990526199,
                  "p50": 4.019063453597482e-06,
                  "p90": 4.266174073563889e-05,
                  "p95": 9.036999399540943e-05,
                  "p99": 0.00019304396118968725
                },
                "candidate_energy": 7.193661620338535,
                "cvrmse_percent": 9.617812119851477,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.17320542093191318,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.206143050742529,
                "relative_energy_error_percent": 0.17320542093191318,
                "rms_normalized_rmse_percent": 0.9324298029760302,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05598290637135506,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.05683674477040768,
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 252.23679200280458,
            "full": 4277.415250078775
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 230.59595795348287,
            "full": 4213.604832999408
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 247.14966700412333,
            "full": 4277.189415995963
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
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "36",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.66408298816532,
            "full": 4220.520792063326
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/corner_glazing/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 794.1484169568866,
      "invocation_count": 3,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/corner_glazing/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2828.448042040691,
      "invocation_count": 3,
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
      36,
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
        "identifier": "corner_glazing_grid",
        "full_identifier": "corner_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1398484167863429,
            "cvrmse_percent": 2.895029389142856,
            "rms_normalized_rmse_percent": 0.8379967975365538,
            "reference_energy": 12.048124969367564,
            "candidate_energy": 12.031275857345463,
            "relative_energy_error_percent": 0.1398484167863429,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.495253622531891e-06,
              "p95": 2.6565384177956724e-05,
              "p99": 0.00011620577424764633,
              "maximum": 0.00035939039662480354
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.0009222719818353653,
              "candidate": 0.0012816623784601688,
              "position": [
                4.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.570086434537777,
            "cvrmse_percent": 16.715149010228558,
            "rms_normalized_rmse_percent": 1.6191473876633198,
            "reference_energy": 7.198991734585055,
            "candidate_energy": 7.15795125928269,
            "relative_energy_error_percent": 0.570086434537777,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 9.801038686418906e-06,
              "p90": 5.686760414391756e-05,
              "p95": 8.169795328285531e-05,
              "p99": 0.00021562259644269943,
              "maximum": 0.0015279054641723633
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05602768436074257,
              "candidate": 0.054499778896570206,
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
            "nmbe_percent": -0.30077017880074214,
            "cvrmse_percent": 6.086491868845643,
            "rms_normalized_rmse_percent": 1.5762938524835826,
            "reference_energy": 19.24711670395262,
            "candidate_energy": 19.189227116628153,
            "relative_energy_error_percent": 0.3007701788007514,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.614477676223032e-06,
              "p90": 5.5603450164198875e-05,
              "p95": 7.795074488967648e-05,
              "p99": 0.00017098896205425262,
              "maximum": 0.0015279054641723633
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05602768436074257,
              "candidate": 0.054499778896570206,
              "position": [
                2.5,
                1.5,
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
      36,
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
        "identifier": "corner_glazing_grid",
        "full_identifier": "corner_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.1398484167863429,
            "cvrmse_percent": 2.895029389142856,
            "rms_normalized_rmse_percent": 0.8379967975365538,
            "reference_energy": 12.048124969367564,
            "candidate_energy": 12.031275857345463,
            "relative_energy_error_percent": 0.1398484167863429,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.495253622531891e-06,
              "p95": 2.6565384177956724e-05,
              "p99": 0.00011620577424764633,
              "maximum": 0.00035939039662480354
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 94,
              "rgb_channel": 0,
              "reference": 0.0009222719818353653,
              "candidate": 0.0012816623784601688,
              "position": [
                4.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.57046045337506,
            "cvrmse_percent": 427.1216558176636,
            "rms_normalized_rmse_percent": 27.94555912649558,
            "reference_energy": 3.964076539047724,
            "candidate_energy": 7.15795125928269,
            "relative_energy_error_percent": 80.57046045337506,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.348000144702382e-05,
              "p90": 0.0003137800085823983,
              "p95": 0.0003880336085785529,
              "p99": 0.0006507132202386856,
              "maximum": 0.01484513096511364
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022629039362072945,
              "candidate": 0.037474170327186584,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.84127920538075,
            "cvrmse_percent": 105.70101697320634,
            "rms_normalized_rmse_percent": 27.93504614984884,
            "reference_energy": 16.012201508415288,
            "candidate_energy": 19.189227116628153,
            "relative_energy_error_percent": 19.841279205380747,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.306684346986003e-05,
              "p90": 0.0003108587407041341,
              "p95": 0.000383367390895728,
              "p99": 0.0006097257137298584,
              "maximum": 0.01484513096511364
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022629039362072945,
              "candidate": 0.037474170327186584,
              "position": [
                5.5,
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
      "bias_percent": 0.0659127314909749,
      "rms_normalized_error_percent": 0.23140123160176732,
      "absolute_error": {
        "p95": 0.14168778129058546,
        "p99": 0.1651360223428175,
        "maximum": 0.1775180948031192
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 23.72755595868,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23140123160176732
    },
    "overcast": {
      "bias_percent": 0.04338790150280118,
      "rms_normalized_error_percent": 0.19028942998267648,
      "absolute_error": {
        "p95": 0.0817720890045166,
        "p99": 0.10200824737548823,
        "maximum": 0.11267471313476562
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.141298294067383,
      "reference_fraction_of_uniform": 0.6381313800811768,
      "rms_normalized_to_uniform_percent": 0.13089485543678775
    },
    "horizon": {
      "bias_percent": 0.35017276739245934,
      "rms_normalized_error_percent": 1.5057262285471478,
      "absolute_error": {
        "p95": 0.08510331017317285,
        "p99": 0.09198268469335284,
        "maximum": 0.0926254728897864
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.5246984121837572,
      "reference_fraction_of_uniform": 0.10640364378785391,
      "rms_normalized_to_uniform_percent": 0.11879941233162991
    },
    "north": {
      "bias_percent": -0.4151747738392734,
      "rms_normalized_error_percent": 0.5710183869621007,
      "absolute_error": {
        "p95": 0.05008399486541748,
        "p99": 0.056247323751449585,
        "maximum": 0.05680537223815918
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2235522270202637,
      "reference_fraction_of_uniform": 0.09371180832386017,
      "rms_normalized_to_uniform_percent": 0.0737096117149063
    },
    "east": {
      "bias_percent": 0.16745674145056652,
      "rms_normalized_error_percent": 0.3079148907389964,
      "absolute_error": {
        "p95": 0.10022217035293579,
        "p99": 0.12228263616561885,
        "maximum": 0.13137054443359375
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.739001274108887,
      "reference_fraction_of_uniform": 0.45259618759155273,
      "rms_normalized_to_uniform_percent": 0.14202306049960567
    },
    "south": {
      "bias_percent": 0.1284970118005295,
      "rms_normalized_error_percent": 0.326103208593756,
      "absolute_error": {
        "p95": 0.0984334945678711,
        "p99": 0.12193140983581542,
        "maximum": 0.12466144561767578
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.4730806350708,
      "reference_fraction_of_uniform": 0.44138893485069275,
      "rms_normalized_to_uniform_percent": 0.14866509950105997
    },
    "west": {
      "bias_percent": -0.466475618149054,
      "rms_normalized_error_percent": 0.5611497082087984,
      "absolute_error": {
        "p95": 0.04343082010746002,
        "p99": 0.08109136819839477,
        "maximum": 0.0840911865234375
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2944483757019043,
      "reference_fraction_of_uniform": 0.09669973701238632,
      "rms_normalized_to_uniform_percent": 0.07322600334341173
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
        "identifier": "corner_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.02031795370810971,
          "cvrmse_percent": 1.2395682421299643,
          "absolute_error_percentiles_lux": {
            "p50": 4.8816070556640625,
            "p90": 34.05162963867191,
            "p95": 48.42431030273429,
            "p99": 83.64113525390619
          },
          "maximum_absolute_error_lux": 374.96875,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5509.95654296875,
            "radiance_lux": 5884.92529296875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.183032724505327,
            "maximum_error_percentage_points": 1.0384931506849284,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.07378032947573408,
            "maximum_error_percentage_points": 0.4578615138084956,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06014079147640751,
            "maximum_error_percentage_points": 0.2721917808219203,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.11722602739726007,
            "maximum_error_percentage_points": 0.4667123287671302,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.06636225266362251,
            "maximum_error_percentage_points": 0.4702739726027403,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 97.22222222222223,
          "radiance_percent": 97.22222222222223,
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
      "maximum_error_percentage_points": 0.004931506849302991,
      "metrics": {
        "da": [
          {
            "identifier": "corner_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "corner_glazing_grid",
            "maximum_error_percentage_points": 0.004910370291099753,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "corner_glazing_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "corner_glazing_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "corner_glazing_grid",
            "maximum_error_percentage_points": 0.0045205479452086195,
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
      "study_preparation_seconds": 0.006414833944290876,
      "weather_seconds": 0.07489166699815542,
      "metric_reduction_seconds": 0.03647624992299825,
      "write_seconds": 0.020457665901631117,
      "total_seconds": 0.13197624997701496,
      "cold_end_to_end_seconds": 0.13839108392130584,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.008374708006158471,
      "engine_upload_seconds": 0.000326375,
      "engine_acceleration_structure_seconds": 0.003181083,
      "engine_tracing_seconds": 0.01470812491606921,
      "engine_annual_reduction_seconds": 0.0003591666463762522,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01470812491606921
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006414833944290876,
      "weather_seconds": 0.07215629203710705,
      "metric_reduction_seconds": 0.013723624986596406,
      "write_seconds": 0.011072875000536442,
      "total_seconds": 0.09707920800428838,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.09707920800428838,
      "raw_export_seconds": 0.0014027089346200228,
      "engine_upload_seconds": 4.3875e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003751249751076102,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015446041012182832,
      "full": 0.02421716705430299
    }
  },
  "elapsed_seconds": 0.7121052079601213,
  "result_class": "passed"
}
```
