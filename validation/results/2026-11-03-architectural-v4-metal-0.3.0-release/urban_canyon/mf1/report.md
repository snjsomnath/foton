# Foton report

Status: **passed**

```json
{
  "scene": "urban_canyon",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "urban_canyon",
    "category": "context",
    "question": "How do tall buildings on both sides restrict side lighting?",
    "interactions": [
      "closed_context",
      "urban_canyon",
      "horizon_mask"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 12,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "b0577d9234103d2f24b57710b0006252bb582436e11db56129d728a76ab5c05c",
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
      "scene_fingerprint": 16492840263789467644,
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
      "scene_fingerprint": 16492840263789467644,
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
    "model_sha256": "0ca7aed254d8850ba56d3a9797b257881c8482afcb8b4028c46586296d7f632b",
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
          "maximum": 0.00024879956617951393,
          "p95": 0.0,
          "p99": 8.12462531030178e-06
        },
        "bias_percent": -0.33462912721299126,
        "identifier": "urban_canyon_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.387723890750364,
        "worst_index": [
          23,
          121,
          0
        ]
      }
    ],
    "passed": true,
    "samples_per_patch": [
      1024,
      4096
    ]
  },
  "depth_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.0004527289420366287,
          "p95": 2.4170536198653238e-05,
          "p99": 7.478545012418181e-05
        },
        "bias_percent": 0.22404797417609473,
        "identifier": "urban_canyon_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0644484662301916,
        "worst_index": [
          15,
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
          "maximum": 0.0004007052630186081,
          "p95": 2.074219974019793e-05,
          "p99": 5.3551048040390015e-05
        },
        "bias_percent": -0.13320211231552775,
        "identifier": "urban_canyon_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7827662533054944,
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
            "identifier": "urban_canyon_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00041193608194589615,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.090414899517782e-05
                },
                "candidate_energy": 0.4054710759737645,
                "cvrmse_percent": 61.506435487763945,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.5691336780138085,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.4077919573392137,
                "relative_energy_error_percent": 0.5691336780138085,
                "rms_normalized_rmse_percent": 5.238417284601472,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0018617829773575068,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002273719059303403,
                  "rgb_channel": 0,
                  "sky_patch_index": 93
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010658688843250275,
                  "p50": 0.0,
                  "p90": 3.484576154733077e-05,
                  "p95": 5.665670250891701e-05,
                  "p99": 0.00020691848476417363
                },
                "candidate_energy": 1.9433385542203894,
                "cvrmse_percent": 39.94310088435851,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.024026459138001367,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.9438055818742406,
                "relative_energy_error_percent": 0.024026459138001367,
                "rms_normalized_rmse_percent": 3.3028812422664515,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02307060919702053,
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "reference": 0.022004740312695503,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.69166606850922,
            "full": 229.42758293356746
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 99.11741595715284,
            "full": 223.2423749519512
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.11487499531358,
            "full": 237.63316695112735
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.87104089185596,
            "full": 225.62691709026694
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
            "identifier": "urban_canyon_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024611642584204674,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.700760913081467e-05
                },
                "candidate_energy": 0.40631440696779464,
                "cvrmse_percent": 36.57291952340787,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.46669500832722727,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.40442696650279686,
                "relative_energy_error_percent": 0.46669500832722727,
                "rms_normalized_rmse_percent": 3.093361254161375,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0059745339676737785,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.005728417541831732,
                  "rgb_channel": 0,
                  "sky_patch_index": 134
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004905052483081818,
                  "p50": 3.0352468911587493e-06,
                  "p90": 2.1493164240382612e-05,
                  "p95": 3.597747327148677e-05,
                  "p99": 0.00011218548752367496
                },
                "candidate_energy": 2.8325455529937003,
                "cvrmse_percent": 14.658834577553074,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.07724489372329331,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.834735241218116,
                "relative_energy_error_percent": 0.0772448937232933,
                "rms_normalized_rmse_percent": 1.3587638261463064,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.020828355103731155,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.020337849855422974,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.92062503751367,
            "full": 2294.192707980983
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.16512501053512,
            "full": 2299.0402500145137
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.83204207476228,
            "full": 2427.1905419882387
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.46012499276549,
            "full": 2271.8641669489443
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
            "identifier": "urban_canyon_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002667855005711317,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.8724531400948763e-05
                },
                "candidate_energy": 0.40493863841220445,
                "cvrmse_percent": 31.575317526402138,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.39396199203157345,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.4065402524893216,
                "relative_energy_error_percent": 0.3939619920315734,
                "rms_normalized_rmse_percent": 2.6744583893349954,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005716250045225024,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.005983035545796156,
                  "rgb_channel": 0,
                  "sky_patch_index": 132
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006337445229291916,
                  "p50": 3.0525616807608458e-06,
                  "p90": 2.0987828065699432e-05,
                  "p95": 3.498928981571218e-05,
                  "p99": 0.00010943040251731873
                },
                "candidate_energy": 2.8424335022518648,
                "cvrmse_percent": 15.65165627895429,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.13421224950994043,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.8386237215001167,
                "relative_energy_error_percent": 0.13421224950994043,
                "rms_normalized_rmse_percent": 1.4503469957493216,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.020834609866142273,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.02020086534321308,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.87154204770923,
            "full": 2479.905499960296
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.16895805858076,
            "full": 2396.2499590124935
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.1357499845326,
            "full": 2419.050958007574
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.38650003261864,
            "full": 2399.467166978866
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
            "identifier": "urban_canyon_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 8.947611786425114e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.715964552015066e-06
                },
                "candidate_energy": 0.4070763141353382,
                "cvrmse_percent": 15.57330647277505,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.012867887150539594,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.40712870299739734,
                "relative_energy_error_percent": 0.012867887150539594,
                "rms_normalized_rmse_percent": 1.3185290368384592,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0024367235600948334,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0023472474422305822,
                  "rgb_channel": 0,
                  "sky_patch_index": 78
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007822960615158081,
                  "p50": 2.181796503464284e-06,
                  "p90": 1.5187061080723652e-05,
                  "p95": 2.5041812750714582e-05,
                  "p99": 7.324991747736931e-05
                },
                "candidate_energy": 2.832824743745018,
                "cvrmse_percent": 13.265590291765179,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1421759127258703,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.836858072602478,
                "relative_energy_error_percent": 0.1421759127258703,
                "rms_normalized_rmse_percent": 1.2278145562250211,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.050473643466830254,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.05125593952834606,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 189.11708297673613,
            "full": 4234.932874911465
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 182.28295806329697,
            "full": 4315.234667039476
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 188.1107920780778,
            "full": 4211.168875102885
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 180.6508330628276,
            "full": 4274.317833012901
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/urban_canyon/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 732.8436659881845,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2802.2283340105787,
      "invocation_count": 3,
      "sample_count": 1024,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/urban_canyon/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11008.634499972686,
      "invocation_count": 3,
      "sample_count": 4096,
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
        "identifier": "urban_canyon_grid",
        "full_identifier": "urban_canyon_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.13016962237368804,
            "cvrmse_percent": 26.459575738552843,
            "rms_normalized_rmse_percent": 2.2402257166817203,
            "reference_energy": 0.40769193591404473,
            "candidate_energy": 0.408222626967472,
            "relative_energy_error_percent": 0.130169622373688,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 6.37053744867444e-06,
              "maximum": 0.00015742098912596703
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 132,
              "rgb_channel": 0,
              "reference": 0.005838992074131966,
              "candidate": 0.005996413063257933,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.576114901505203,
            "cvrmse_percent": 25.2433134688231,
            "rms_normalized_rmse_percent": 2.338676348398146,
            "reference_energy": 2.8342520026050977,
            "candidate_energy": 2.789580934445829,
            "relative_energy_error_percent": 1.576114901505203,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.6101558862355887e-06,
              "p90": 1.7693833797238767e-05,
              "p95": 2.4992756607389304e-05,
              "p99": 5.469055031426251e-05,
              "maximum": 0.001283278688788414
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01979757845401764,
              "candidate": 0.018514299765229225,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.3615404196657317,
            "cvrmse_percent": 22.186077880047893,
            "rms_normalized_rmse_percent": 2.3511012625901673,
            "reference_energy": 3.2419439385191424,
            "candidate_energy": 3.197803561413301,
            "relative_energy_error_percent": 1.361540419665732,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.6221749724063557e-06,
              "p90": 1.7954647773876786e-05,
              "p95": 2.528918375901412e-05,
              "p99": 6.907712668180466e-05,
              "maximum": 0.001283278688788414
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01979757845401764,
              "candidate": 0.018514299765229225,
              "position": [
                3.5,
                3.5,
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
        "identifier": "urban_canyon_grid",
        "full_identifier": "urban_canyon_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.13016962237368804,
            "cvrmse_percent": 26.459575738552843,
            "rms_normalized_rmse_percent": 2.2402257166817203,
            "reference_energy": 0.40769193591404473,
            "candidate_energy": 0.408222626967472,
            "relative_energy_error_percent": 0.130169622373688,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 6.37053744867444e-06,
              "maximum": 0.00015742098912596703
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 132,
              "rgb_channel": 0,
              "reference": 0.005838992074131966,
              "candidate": 0.005996413063257933,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 43.606909088048276,
            "cvrmse_percent": 385.3410709385268,
            "rms_normalized_rmse_percent": 31.7565507851933,
            "reference_energy": 1.9425116466614298,
            "candidate_energy": 2.789580934445829,
            "relative_energy_error_percent": 43.606909088048276,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0009999641624745e-05,
              "p90": 4.2226797475564126e-05,
              "p95": 5.605237756753922e-05,
              "p99": 0.0001391253317706287,
              "maximum": 0.006993060000240803
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013271120376884937,
              "candidate": 0.02026418037712574,
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
            "nmbe_percent": 36.064959866539844,
            "cvrmse_percent": 318.5244407335566,
            "rms_normalized_rmse_percent": 31.759425669143763,
            "reference_energy": 2.3502035825754746,
            "candidate_energy": 3.197803561413301,
            "relative_energy_error_percent": 36.06495986653985,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.989375939767342e-06,
              "p90": 4.21000240748981e-05,
              "p95": 5.605237756753922e-05,
              "p99": 0.0001391253317706287,
              "maximum": 0.006993060000240803
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013271120376884937,
              "candidate": 0.02026418037712574,
              "position": [
                5.5,
                1.5,
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
      "bias_percent": -0.12838817399797592,
      "rms_normalized_error_percent": 0.5782860331368317,
      "absolute_error": {
        "p95": 0.03743998908455781,
        "p99": 0.038978578136022436,
        "maximum": 0.0393354948803708
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.704581757737256,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.5782860331368317
    },
    "overcast": {
      "bias_percent": -0.09691470374167024,
      "rms_normalized_error_percent": 0.642791392342671,
      "absolute_error": {
        "p95": 0.02742403745651245,
        "p99": 0.04436569213867185,
        "maximum": 0.04993724822998047
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1982061862945557,
      "reference_fraction_of_uniform": 0.7029326558113098,
      "rms_normalized_to_uniform_percent": 0.47391528512821235
    },
    "horizon": {
      "bias_percent": -0.20505209157732565,
      "rms_normalized_error_percent": 2.7732554707296373,
      "absolute_error": {
        "p95": 0.01391362130984257,
        "p99": 0.017549548447007242,
        "maximum": 0.019204532554645104
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.19461432061968886,
      "reference_fraction_of_uniform": 0.11417130315769031,
      "rms_normalized_to_uniform_percent": 0.24468455404880485
    },
    "north": {
      "bias_percent": -0.39026227208159764,
      "rms_normalized_error_percent": 1.0898727429542516,
      "absolute_error": {
        "p95": 0.016369305551052094,
        "p99": 0.021686717867851247,
        "maximum": 0.024160385131835938
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.44944655895233154,
      "reference_fraction_of_uniform": 0.2636696994304657,
      "rms_normalized_to_uniform_percent": 0.26298116390845355
    },
    "east": {
      "bias_percent": 0.014968661798804737,
      "rms_normalized_error_percent": 0.7844420525851313,
      "absolute_error": {
        "p95": 0.01445256918668747,
        "p99": 0.017332776635885238,
        "maximum": 0.01767638325691223
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4782004952430725,
      "reference_fraction_of_uniform": 0.28053832054138184,
      "rms_normalized_to_uniform_percent": 0.23662789793166025
    },
    "south": {
      "bias_percent": 0.17910200759799458,
      "rms_normalized_error_percent": 1.078363707421706,
      "absolute_error": {
        "p95": 0.013898640871047974,
        "p99": 0.025113880634307854,
        "maximum": 0.027263879776000977
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.2655318081378937,
      "reference_fraction_of_uniform": 0.15577533841133118,
      "rms_normalized_to_uniform_percent": 0.20386365708168203
    },
    "west": {
      "bias_percent": -0.26348935029886617,
      "rms_normalized_error_percent": 1.0203782843175542,
      "absolute_error": {
        "p95": 0.022471092641353607,
        "p99": 0.02561487704515457,
        "maximum": 0.026161670684814453
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4795849025249481,
      "reference_fraction_of_uniform": 0.2813504934310913,
      "rms_normalized_to_uniform_percent": 0.3097064346160596
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
        "identifier": "urban_canyon_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.6412618960138429,
          "cvrmse_percent": 4.444119656873852,
          "absolute_error_percentiles_lux": {
            "p50": 0.8819446563720703,
            "p90": 5.835910797119141,
            "p95": 8.814011764526363,
            "p99": 19.058373260498016
          },
          "maximum_absolute_error_lux": 130.1572265625,
          "worst": {
            "sensor_index": 11,
            "position": [
              1.5,
              0.5,
              0.75
            ],
            "hour_of_year": 3824.5,
            "foton_lux": 6431.0556640625,
            "radiance_lux": 6561.212890625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.01934931506849314,
            "maximum_error_percentage_points": 0.33287671232876903,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3186899234360473,
            "maximum_error_percentage_points": 0.9534536645047496,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.7170319634703204,
            "maximum_error_percentage_points": 3.0176712328767223,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.718801369863014,
            "maximum_error_percentage_points": 3.0176712328767135,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0061910197869101975,
            "maximum_error_percentage_points": 0.11356164383561662,
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
      "maximum_error_percentage_points": 0.00497826145119884,
      "metrics": {
        "da": [
          {
            "identifier": "urban_canyon_grid",
            "maximum_error_percentage_points": 0.004520547945205511,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "urban_canyon_grid",
            "maximum_error_percentage_points": 0.00497826145119884,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "urban_canyon_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "urban_canyon_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "urban_canyon_grid",
            "maximum_error_percentage_points": 0.003972602739725772,
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
      "study_preparation_seconds": 0.00668200000654906,
      "weather_seconds": 0.09141829202417284,
      "metric_reduction_seconds": 0.044714792049489915,
      "write_seconds": 0.04684550000820309,
      "total_seconds": 0.1830999170197174,
      "cold_end_to_end_seconds": 0.18978191702626646,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01768216595519334,
      "engine_upload_seconds": 0.000287209,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.025686874985694885,
      "engine_annual_reduction_seconds": 0.00035674998071044683,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.025686874985694885
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.00668200000654906,
      "weather_seconds": 0.08958224998787045,
      "metric_reduction_seconds": 0.012102541979402304,
      "write_seconds": 0.03874991601333022,
      "total_seconds": 0.14057879196479917,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14057879196479917,
      "raw_export_seconds": 0.017386707942932844,
      "engine_upload_seconds": 4.9208e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003838749835267663,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.021897958009503782,
      "full": 0.02918974997010082
    }
  },
  "elapsed_seconds": 0.7087345409672707,
  "result_class": "passed"
}
```
