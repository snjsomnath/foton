# Foton report

Status: **passed**

```json
{
  "scene": "shallow_plan",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "shallow_plan",
    "category": "form",
    "question": "How evenly does side lighting illuminate a shallow room?",
    "interactions": [
      "shallow_plan",
      "daylight_penetration"
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
    "sensors": 24,
    "floor_area": 24.0,
    "aperture_area": 2.9999999999999987
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "5ab4bde3be656db4ab96bb7286f27166e82d2ab138b8f4e9b0d49c32a91360de",
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 1786167869922741379,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 1786167869922741379,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.7)",
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "29dd1cb729988861b01d9c279904ca7b5421cc8b2287041945f494d12c1eb0a3",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "6c88af558bce1a42e600f067e4c484531c274a7df792ca0c76f1c07e92171d91",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 7.683411240577698e-08,
          "p99": 7.605081191286265e-06
        },
        "bias_percent": -0.052080622609088335,
        "identifier": "shallow_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7618511234918872,
        "worst_index": [
          11,
          543,
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
          "maximum": 0.0005163215100765228,
          "p95": 3.2000942155718803e-05,
          "p99": 0.00011107027676189246
        },
        "bias_percent": 0.06433780937536913,
        "identifier": "shallow_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5800990822850633,
        "worst_index": [
          12,
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
          "maximum": 0.00040520355105400085,
          "p95": 2.5348970666527748e-05,
          "p99": 9.347465238533872e-05
        },
        "bias_percent": -0.005245499571293332,
        "identifier": "shallow_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2860441729510455,
        "worst_index": [
          11,
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
            "identifier": "shallow_plan_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006353104836307466,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 5.003577098250389e-05,
                  "p99": 0.00021558193184318826
                },
                "candidate_energy": 5.457864085614801,
                "cvrmse_percent": 30.540550123403804,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.025204040475677883,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.459240034682807,
                "relative_energy_error_percent": 0.025204040475677886,
                "rms_normalized_rmse_percent": 6.679748862743634,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002233721490483731,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.0015984110068529844,
                  "rgb_channel": 0,
                  "sky_patch_index": 152
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010221628472208977,
                  "p50": 0.0,
                  "p90": 9.676248737378046e-06,
                  "p95": 8.500838885083795e-05,
                  "p99": 0.0003068354941206051
                },
                "candidate_energy": 1.7710426872525815,
                "cvrmse_percent": 136.57095998718734,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.11583530856302258,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.773096559122962,
                "relative_energy_error_percent": 0.1158353085630226,
                "rms_normalized_rmse_percent": 5.427985290169062,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.019398417323827744,
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "reference": 0.02042058017104864,
                  "rgb_channel": 0,
                  "sky_patch_index": 0
                }
              }
            },
            "start_sensor_index": 0
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 103.72458293568343,
            "full": 178.01516596227884
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 99.9974999576807,
            "full": 193.51666700094938
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.74933389481157,
            "full": 184.19966602232307
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.98220910411328,
            "full": 191.29791599698365
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.58570805191994,
            "full": 193.62212496344
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 96.4095420204103,
            "full": 186.87729199882597
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 101.57916601747274,
            "full": 190.91583404224366
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 99.5442089624703,
            "full": 175.81754201091826
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
            "identifier": "shallow_plan_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00027935224352404475,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.98347619920969e-05,
                  "p99": 0.00013718152185901986
                },
                "candidate_energy": 5.4572571391631755,
                "cvrmse_percent": 18.587405224010602,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.02730104850694477,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.455767657388606,
                "relative_energy_error_percent": 0.02730104850694477,
                "rms_normalized_rmse_percent": 4.068201992916337,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0008376154582947493,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.001116967701818794,
                  "rgb_channel": 0,
                  "sky_patch_index": 94
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006927121430635452,
                  "p50": 4.1287583130156236e-08,
                  "p90": 1.657695247558877e-05,
                  "p95": 5.1260110922157764e-05,
                  "p99": 0.00021313517063390377
                },
                "candidate_energy": 3.1991199222830673,
                "cvrmse_percent": 52.33429002669728,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0021058154016219627,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.199052556141634,
                "relative_energy_error_percent": 0.002105815401621963,
                "rms_normalized_rmse_percent": 2.852302091156837,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.041903115808963776,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.04121040366590023,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 138.2663749391213,
            "full": 1582.71662495099
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.9617080045864,
            "full": 1573.6927089747041
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.1165420981124,
            "full": 1524.5260420488194
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.66979199275374,
            "full": 1570.8788329502568
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
            "identifier": "shallow_plan_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003278054064139724,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.063162487000227e-05,
                  "p99": 0.00014908751472830772
                },
                "candidate_energy": 5.46206542779737,
                "cvrmse_percent": 20.78040057140745,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.07943279284138274,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.457730200273545,
                "relative_energy_error_percent": 0.07943279284138276,
                "rms_normalized_rmse_percent": 4.547947762993317,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0009126286022365093,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.0012404340086504817,
                  "rgb_channel": 0,
                  "sky_patch_index": 89
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00044834497384727,
                  "p50": 4.1202227407666214e-08,
                  "p90": 1.6770649381214753e-05,
                  "p95": 5.544986925087869e-05,
                  "p99": 0.00022443765628849934
                },
                "candidate_energy": 3.1999027174283583,
                "cvrmse_percent": 52.5380442528047,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.08536216164021584,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2026365572230837,
                "relative_energy_error_percent": 0.08536216164021583,
                "rms_normalized_rmse_percent": 2.8649032592960233,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.00027117051649838686,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.00017717445734888315,
                  "rgb_channel": 0,
                  "sky_patch_index": 310
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.29474997427315,
            "full": 1653.0679169809446
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.10875002387911,
            "full": 1633.6745419539511
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 131.46729208528996,
            "full": 1660.4635419789702
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.06708393245935,
            "full": 1638.6230000061914
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
            "identifier": "shallow_plan_grid",
            "sensor_count": 24,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00016113615129143,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.0742532797157764e-05,
                  "p99": 8.25260067358613e-05
                },
                "candidate_energy": 5.458472714172785,
                "cvrmse_percent": 11.395434962557252,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.015825866657759095,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.457609000249704,
                "relative_energy_error_percent": 0.015825866657759095,
                "rms_normalized_rmse_percent": 2.49513826423557,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003942229086533189,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.003781092935241759,
                  "rgb_channel": 0,
                  "sky_patch_index": 407
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004863198846578598,
                  "p50": 4.231073091887083e-08,
                  "p90": 1.1337648174958304e-05,
                  "p95": 3.302376717329025e-05,
                  "p99": 0.00012332618352956982
                },
                "candidate_energy": 3.204432836924248,
                "cvrmse_percent": 30.83659037073612,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.11000520965751116,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.2009116673336457,
                "relative_energy_error_percent": 0.11000520965751116,
                "rms_normalized_rmse_percent": 1.6778139475382958,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04159840568900108,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.04208472557365894,
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 184.9117079982534,
            "full": 2883.4930829470977
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.05954193603247,
            "full": 2883.6783749284223
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.10083400644362,
            "full": 2831.844749976881
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 177.25520895328373,
            "full": 2905.1647920859978
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub/7fb068ed-087d-41c3-b9b3-215cbbd36098/scratchpad/suite-metal-0.3.7/shallow_plan/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 1514.6619159495458,
      "invocation_count": 2,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/shallow_plan/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 5762.5814999919385,
      "invocation_count": 2,
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
      24,
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
        "identifier": "shallow_plan_grid",
        "full_identifier": "shallow_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.016809412332837798,
            "cvrmse_percent": 1.9093973711406045,
            "rms_normalized_rmse_percent": 0.4181404568921618,
            "reference_energy": 5.458718650273795,
            "candidate_energy": 5.457801071747781,
            "relative_energy_error_percent": 0.016809412332837795,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.51925802230835e-08,
              "p99": 6.890505210321787e-06,
              "maximum": 7.347748032771051e-05
            },
            "worst": {
              "global_sensor_index": 1,
              "local_sensor_index": 1,
              "sky_patch_index": 257,
              "rgb_channel": 0,
              "reference": 0.0004673888615798205,
              "candidate": 0.00039391138125211,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.27190319053231715,
            "cvrmse_percent": 22.45399426257976,
            "rms_normalized_rmse_percent": 1.2223996858455406,
            "reference_energy": 3.201994489517846,
            "candidate_energy": 3.210700814695514,
            "relative_energy_error_percent": 0.2719031905323172,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.1782976798713207e-05,
              "p95": 2.040620893239975e-05,
              "p99": 5.335296737030105e-05,
              "maximum": 0.0006718821823596954
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042951490730047226,
              "candidate": 0.04227960854768753,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.08993193200070991,
            "cvrmse_percent": 8.268417355564052,
            "rms_normalized_rmse_percent": 1.2175171463806367,
            "reference_energy": 8.66071313979164,
            "candidate_energy": 8.668501886443295,
            "relative_energy_error_percent": 0.08993193200070991,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.1670796084217727e-05,
              "p95": 2.019453313550912e-05,
              "p99": 5.352316657081223e-05,
              "maximum": 0.0006718821823596954
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.042951490730047226,
              "candidate": 0.04227960854768753,
              "position": [
                3.5,
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
      24,
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
        "identifier": "shallow_plan_grid",
        "full_identifier": "shallow_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.016809412332837798,
            "cvrmse_percent": 1.9093973711406045,
            "rms_normalized_rmse_percent": 0.4181404568921618,
            "reference_energy": 5.458718650273795,
            "candidate_energy": 5.457801071747781,
            "relative_energy_error_percent": 0.016809412332837795,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 6.51925802230835e-08,
              "p99": 6.890505210321787e-06,
              "maximum": 7.347748032771051e-05
            },
            "worst": {
              "global_sensor_index": 1,
              "local_sensor_index": 1,
              "sky_patch_index": 257,
              "rgb_channel": 0,
              "reference": 0.0004673888615798205,
              "candidate": 0.00039391138125211,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.20070338814692,
            "cvrmse_percent": 933.1230517219435,
            "rms_normalized_rmse_percent": 37.113177398224295,
            "reference_energy": 1.7719030636530846,
            "candidate_energy": 3.210700814695514,
            "relative_energy_error_percent": 81.20070338814692,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.780999683542177e-05,
              "p95": 9.251000301446766e-05,
              "p99": 0.00016948039992712395,
              "maximum": 0.01144474372267723
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03086133673787117,
              "candidate": 0.0423060804605484,
              "position": [
                4.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.885982553158854,
            "cvrmse_percent": 228.66469177402354,
            "rms_normalized_rmse_percent": 37.112824795482936,
            "reference_energy": 7.23062171392688,
            "candidate_energy": 8.668501886443295,
            "relative_energy_error_percent": 19.885982553158858,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.768997627659701e-05,
              "p95": 9.244843386113644e-05,
              "p99": 0.0001679010107181955,
              "maximum": 0.01144474372267723
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03086133673787117,
              "candidate": 0.0423060804605484,
              "position": [
                4.5,
                2.5,
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
      "bias_percent": 0.33448021136339895,
      "rms_normalized_error_percent": 0.3689489461927724,
      "absolute_error": {
        "p95": 0.24658671755692727,
        "p99": 0.2833919486157275,
        "maximum": 0.291661086973793
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.293713521955244,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.3689489461927724
    },
    "overcast": {
      "bias_percent": 0.22028821686174674,
      "rms_normalized_error_percent": 0.23972895423984672,
      "absolute_error": {
        "p95": 0.11465272903442378,
        "p99": 0.12550529479980468,
        "maximum": 0.1276092529296875
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.642370223999023,
      "reference_fraction_of_uniform": 0.6531580686569214,
      "rms_normalized_to_uniform_percent": 0.1699504055650219
    },
    "horizon": {
      "bias_percent": 2.3701697767671925,
      "rms_normalized_error_percent": 3.330735631957537,
      "absolute_error": {
        "p95": 0.14495329414770697,
        "p99": 0.1797600017564372,
        "maximum": 0.1878087415996328
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.6741284431913712,
      "reference_fraction_of_uniform": 0.1027468932073427,
      "rms_normalized_to_uniform_percent": 0.23386261078319245
    },
    "north": {
      "bias_percent": -86.11674085041898,
      "rms_normalized_error_percent": 99.2371971678146,
      "absolute_error": {
        "p95": 0.00014394760046343427,
        "p99": 0.0002884661307938784,
        "maximum": 0.0003298836042731068
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 3.167845352436416e-05,
      "reference_fraction_of_uniform": 1.9442134089331375e-06,
      "rms_normalized_to_uniform_percent": 0.00029758483509849517
    },
    "east": {
      "bias_percent": 0.28360474439208244,
      "rms_normalized_error_percent": 0.3632312678626896,
      "absolute_error": {
        "p95": 0.031602835655212394,
        "p99": 0.05403429985046385,
        "maximum": 0.060579776763916016
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.206794500350952,
      "reference_fraction_of_uniform": 0.19681178033351898,
      "rms_normalized_to_uniform_percent": 0.07304746831844378
    },
    "south": {
      "bias_percent": 0.4505641552293149,
      "rms_normalized_error_percent": 0.5098489147809188,
      "absolute_error": {
        "p95": 0.22961540222167953,
        "p99": 0.2589790630340576,
        "maximum": 0.26470375061035156
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.96057415008545,
      "reference_fraction_of_uniform": 0.6726873517036438,
      "rms_normalized_to_uniform_percent": 0.3343063434297279
    },
    "west": {
      "bias_percent": 0.1440027104008953,
      "rms_normalized_error_percent": 0.24906001664820404,
      "absolute_error": {
        "p95": 0.028467416763305643,
        "p99": 0.03532936096191406,
        "maximum": 0.03698015213012695
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.24345326423645,
      "reference_fraction_of_uniform": 0.19906164705753326,
      "rms_normalized_to_uniform_percent": 0.05049048787389182
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
        "identifier": "shallow_plan_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 0.22077882633332066,
          "cvrmse_percent": 1.6580936224467553,
          "absolute_error_percentiles_lux": {
            "p50": 2.6274795532226562,
            "p90": 28.38282470703125,
            "p95": 44.569921874999864,
            "p99": 104.14144531249963
          },
          "maximum_absolute_error_lux": 477.828125,
          "worst": {
            "sensor_index": 12,
            "position": [
              4.5,
              2.5,
              0.75
            ],
            "hour_of_year": 8604.5,
            "foton_lux": 6986.576171875,
            "radiance_lux": 6508.748046875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2696061643835616,
            "maximum_error_percentage_points": 0.6878082191780877,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09702076883848676,
            "maximum_error_percentage_points": 0.27340719076585174,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07472602739726053,
            "maximum_error_percentage_points": 0.40986301369862943,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07449771689497837,
            "maximum_error_percentage_points": 0.4371232876712412,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03556506849315091,
            "maximum_error_percentage_points": 0.1331506849315076,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 66.66666666666667,
          "radiance_percent": 66.66666666666667,
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
      "maximum_error_percentage_points": 0.004816994863020341,
      "metrics": {
        "da": [
          {
            "identifier": "shallow_plan_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "shallow_plan_grid",
            "maximum_error_percentage_points": 0.004816994863020341,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "shallow_plan_grid",
            "maximum_error_percentage_points": 0.004520547945212172,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "shallow_plan_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "shallow_plan_grid",
            "maximum_error_percentage_points": 0.004520547945197961,
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
      "study_preparation_seconds": 0.005991125013679266,
      "weather_seconds": 0.08154245815239847,
      "metric_reduction_seconds": 0.09482366708107293,
      "write_seconds": 0.026735999854281545,
      "total_seconds": 0.2032373750116676,
      "cold_end_to_end_seconds": 0.20922850002534688,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.009606916923075914,
      "engine_upload_seconds": 0.000813125,
      "engine_acceleration_structure_seconds": 0.003037875,
      "engine_tracing_seconds": 0.03221437521278858,
      "engine_annual_reduction_seconds": 0.0009942499455064535,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03221437521278858
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.005991125013679266,
      "weather_seconds": 0.07877545896917582,
      "metric_reduction_seconds": 0.0470424999948591,
      "write_seconds": 0.012705374974757433,
      "total_seconds": 0.138652834109962,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.138652834109962,
      "raw_export_seconds": 0.0038381670601665974,
      "engine_upload_seconds": 5.2083e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0009775417856872082,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.016106874914839864,
      "full": 0.038679291028529406
    }
  },
  "elapsed_seconds": 1.110751000000164,
  "result_class": "passed"
}
```
