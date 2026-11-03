# Foton report

Status: **passed**

```json
{
  "scene": "teaching_wwr40",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_wwr40",
    "category": "teaching",
    "question": "How does a 40% window-to-wall ratio light the base room?",
    "interactions": [
      "multiple_bounces",
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
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 7.1982
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "f4666ba38197355bc650bd2c364e575ce217b58507dddbe0ffa930ae9c4f63b3",
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
      "scene_fingerprint": 16461150684353540723,
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
      "scene_fingerprint": 16461150684353540723,
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
    "model_sha256": "35c7034ddfdcfdc2eb85ea4eeffc1d9f1a8f8b74af4e3f732a6dc5204314c196",
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
          "maximum": 0.0003813905641436577,
          "p95": 2.1857209503650665e-05,
          "p99": 0.00014092877972871065
        },
        "bias_percent": 0.060445426886030613,
        "identifier": "teaching_wwr40_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9460755466048233,
        "worst_index": [
          16,
          76,
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
          "maximum": 0.0005989968776702881,
          "p95": 9.357290109619495e-05,
          "p99": 0.00020458875223994255
        },
        "bias_percent": 0.050549028831366735,
        "identifier": "teaching_wwr40_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8272022853471744,
        "worst_index": [
          34,
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
          "maximum": 0.0006936416029930115,
          "p95": 8.122536819428201e-05,
          "p99": 0.0001649465411901474
        },
        "bias_percent": -0.007080013457806842,
        "identifier": "teaching_wwr40_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6773532389526411,
        "worst_index": [
          9,
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
            "identifier": "teaching_wwr40_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0012309905141592026,
                  "p50": 0.0,
                  "p90": 9.485287591814995e-05,
                  "p95": 0.00027625898364931276,
                  "p99": 0.00054233951959759
                },
                "candidate_energy": 14.10381218314069,
                "cvrmse_percent": 12.479802329923247,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.07236666999657208,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 14.09361310465465,
                "relative_energy_error_percent": 0.0723666699965721,
                "rms_normalized_rmse_percent": 3.7918269557086304,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.018709100782871246,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.017478110268712044,
                  "rgb_channel": 0,
                  "sky_patch_index": 118
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0016849804669618607,
                  "p50": 0.0,
                  "p90": 0.0001818779855966568,
                  "p95": 0.00039698380278423395,
                  "p99": 0.0007863288701628335
                },
                "candidate_energy": 4.841920510895221,
                "cvrmse_percent": 52.38083581896755,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.23028075480268834,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.853096257588497,
                "relative_energy_error_percent": 0.23028075480268836,
                "rms_normalized_rmse_percent": 3.649994694744231,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0333094596862793,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.031624479219317436,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.78070794045925,
            "full": 240.89837505016476
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.3213339690119,
            "full": 241.64200003724545
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.54908300098032,
            "full": 241.11170799005777
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.3323749480769,
            "full": 227.0219170022756
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
            "identifier": "teaching_wwr40_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00041026994585990906,
                  "p50": 0.0,
                  "p90": 6.352143827825785e-05,
                  "p95": 0.00011654244735836983,
                  "p99": 0.00021085154730826616
                },
                "candidate_energy": 14.107012920952911,
                "cvrmse_percent": 5.265812381721969,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.005997571154540826,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 14.106166893556292,
                "relative_energy_error_percent": 0.0059975711545408265,
                "rms_normalized_rmse_percent": 1.6017226216424745,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013862079940736294,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.013451809994876385,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013109669089317322,
                  "p50": 3.8072417396506353e-07,
                  "p90": 8.65524634718895e-05,
                  "p95": 0.00018351419130340215,
                  "p99": 0.00036958756390959024
                },
                "candidate_energy": 8.667765267066258,
                "cvrmse_percent": 14.488336231456405,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.10435268931438958,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.658729649816213,
                "relative_energy_error_percent": 0.1043526893143896,
                "rms_normalized_rmse_percent": 1.4382679441667103,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06943225115537643,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0681212842464447,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.94920797552913,
            "full": 2201.471332926303
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.20000000670552,
            "full": 2170.878541073762
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.9703749800101,
            "full": 2163.6771250050515
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.90220791473985,
            "full": 2209.487249958329
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
            "identifier": "teaching_wwr40_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00043725455179810524,
                  "p50": 0.0,
                  "p90": 5.63210342079401e-05,
                  "p95": 0.00011704210191965103,
                  "p99": 0.00025553442537784576
                },
                "candidate_energy": 14.10043370099811,
                "cvrmse_percent": 5.991113379386133,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0031347266502860876,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 14.100875724907382,
                "relative_energy_error_percent": 0.003134726650286087,
                "rms_normalized_rmse_percent": 1.8208550010235987,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013471905142068863,
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "reference": 0.013909159693866968,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011863354593515396,
                  "p50": 3.353325297439369e-07,
                  "p90": 9.022606536746025e-05,
                  "p95": 0.00019638884696178093,
                  "p99": 0.0003953941632062197
                },
                "candidate_energy": 8.683189144303778,
                "cvrmse_percent": 15.583577025968832,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.057537957831393975,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.678195887613438,
                "relative_energy_error_percent": 0.057537957831393975,
                "rms_normalized_rmse_percent": 1.549443439571935,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04762043058872223,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.04643409512937069,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.35724999569356,
            "full": 2288.221082999371
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.79037502780557,
            "full": 2301.793875056319
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.8852079277858,
            "full": 2307.4501249939203
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.78512493893504,
            "full": 2347.9913749033585
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
            "identifier": "teaching_wwr40_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003039245493710041,
                  "p50": 0.0,
                  "p90": 3.2273936085402966e-05,
                  "p95": 6.818398833274841e-05,
                  "p99": 0.0001333367545157671
                },
                "candidate_energy": 14.10328723038674,
                "cvrmse_percent": 3.067922022943651,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.011093216625918247,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 14.104851912164122,
                "relative_energy_error_percent": 0.011093216625918247,
                "rms_normalized_rmse_percent": 0.93245803910697,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0022788289934396744,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0019749044440686703,
                  "rgb_channel": 0,
                  "sky_patch_index": 17
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0009945407509803772,
                  "p50": 2.255983417853713e-07,
                  "p90": 5.107336619403213e-05,
                  "p95": 0.00011363640660420058,
                  "p99": 0.00022085942327976227
                },
                "candidate_energy": 8.6811349388196,
                "cvrmse_percent": 9.419966899419911,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1261836018082264,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.670194575021057,
                "relative_energy_error_percent": 0.1261836018082264,
                "rms_normalized_rmse_percent": 0.9361048715585384,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06844403967261314,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.06943858042359352,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 228.2611250411719,
            "full": 4061.0474169952795
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.81733400654048,
            "full": 4091.241457965225
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 239.00391696952283,
            "full": 4089.9677500128746
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 231.52916692197323,
            "full": 4081.7387090064585
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/teaching_wwr40/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 797.995415981859,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr40/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2795.1629580929875,
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
        "identifier": "teaching_wwr40_grid",
        "full_identifier": "teaching_wwr40_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.025828271503773346,
            "cvrmse_percent": 2.2120250387640974,
            "rms_normalized_rmse_percent": 0.6723882460492632,
            "reference_energy": 14.100017698235206,
            "candidate_energy": 14.096375907382026,
            "relative_energy_error_percent": 0.025828271503773346,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.726492524147034e-07,
              "p95": 1.5122193826755193e-05,
              "p99": 8.302740752696991e-05,
              "maximum": 0.0003454405814409256
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.009064365178346634,
              "candidate": 0.00940980575978756,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1795962616760916,
            "cvrmse_percent": 20.017037016391853,
            "rms_normalized_rmse_percent": 1.9905827371900162,
            "reference_energy": 8.679716682345157,
            "candidate_energy": 8.577331068836138,
            "relative_energy_error_percent": 1.1795962616760913,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.125665335166559e-06,
              "p90": 5.5230455473065376e-05,
              "p95": 8.133056107908484e-05,
              "p99": 0.0001874854788184166,
              "maximum": 0.0027474910020828247
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06894131004810333,
              "candidate": 0.06619381904602051,
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
            "nmbe_percent": -0.46544618383517133,
            "cvrmse_percent": 7.629853223065236,
            "rms_normalized_rmse_percent": 1.9913139257553625,
            "reference_energy": 22.779734380580365,
            "candidate_energy": 22.673706976218163,
            "relative_energy_error_percent": 0.46544618383517916,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1488227755762637e-06,
              "p90": 5.4135220125317574e-05,
              "p95": 8.150871144607659e-05,
              "p99": 0.00018992461264133453,
              "maximum": 0.0027474910020828247
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06894131004810333,
              "candidate": 0.06619381904602051,
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
        "identifier": "teaching_wwr40_grid",
        "full_identifier": "teaching_wwr40_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.025828271503773346,
            "cvrmse_percent": 2.2120250387640974,
            "rms_normalized_rmse_percent": 0.6723882460492632,
            "reference_energy": 14.100017698235206,
            "candidate_energy": 14.096375907382026,
            "relative_energy_error_percent": 0.025828271503773346,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.726492524147034e-07,
              "p95": 1.5122193826755193e-05,
              "p99": 8.302740752696991e-05,
              "maximum": 0.0003454405814409256
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.009064365178346634,
              "candidate": 0.00940980575978756,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 76.99074062096085,
            "cvrmse_percent": 421.14212634226413,
            "rms_normalized_rmse_percent": 29.289948108084417,
            "reference_energy": 4.846203275235254,
            "candidate_energy": 8.577331068836138,
            "relative_energy_error_percent": 76.99074062096084,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.3999999737279722e-07,
              "p90": 0.0004797973670065403,
              "p95": 0.0006236559615672372,
              "p99": 0.0010222575510852039,
              "maximum": 0.017256420105695724
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.039299070835113525,
              "candidate": 0.05655549094080925,
              "position": [
                5.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.674034246550455,
            "cvrmse_percent": 107.7108058321296,
            "rms_normalized_rmse_percent": 29.286681437257425,
            "reference_energy": 18.94622097347046,
            "candidate_energy": 22.673706976218163,
            "relative_energy_error_percent": 19.674034246550452,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3999999737279722e-07,
              "p90": 0.0004798932932317257,
              "p95": 0.0006185421021655201,
              "p99": 0.0010264304000884295,
              "maximum": 0.017256420105695724
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.039299070835113525,
              "candidate": 0.05655549094080925,
              "position": [
                5.5,
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
      "bias_percent": 0.026752385584080742,
      "rms_normalized_error_percent": 0.17950601314963546,
      "absolute_error": {
        "p95": 0.12975508280867643,
        "p99": 0.14112317398641624,
        "maximum": 0.14624631733839877
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 28.07343608779499,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.17950601314963546
    },
    "overcast": {
      "bias_percent": 8.282688206132572e-05,
      "rms_normalized_error_percent": 0.14534512975647595,
      "absolute_error": {
        "p95": 0.0653078556060791,
        "p99": 0.08369870185852048,
        "maximum": 0.09261512756347656
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.91876983642578,
      "reference_fraction_of_uniform": 0.6382820010185242,
      "rms_normalized_to_uniform_percent": 0.0999504898214416
    },
    "horizon": {
      "bias_percent": 0.6840343044852443,
      "rms_normalized_error_percent": 1.6956367928704728,
      "absolute_error": {
        "p95": 0.10998976974975205,
        "p99": 0.1254504311658658,
        "maximum": 0.12568095689832326
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7453148860198433,
      "reference_fraction_of_uniform": 0.09779048341052121,
      "rms_normalized_to_uniform_percent": 0.1193364269519259
    },
    "north": {
      "bias_percent": -44.870614598248686,
      "rms_normalized_error_percent": 121.35297010690181,
      "absolute_error": {
        "p95": 8.979520816865261e-05,
        "p99": 0.00012865679691458347,
        "maximum": 0.0001440560954506509
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.4938264687079936e-05,
      "reference_fraction_of_uniform": 8.883224609235185e-07,
      "rms_normalized_to_uniform_percent": 9.738448105120901e-05
    },
    "east": {
      "bias_percent": -0.11759013751144268,
      "rms_normalized_error_percent": 0.29418946959607645,
      "absolute_error": {
        "p95": 0.041475459933280945,
        "p99": 0.06386389732360835,
        "maximum": 0.0755300521850586
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.569021224975586,
      "reference_fraction_of_uniform": 0.19837333261966705,
      "rms_normalized_to_uniform_percent": 0.06339137765125125
    },
    "south": {
      "bias_percent": 0.041139993298348665,
      "rms_normalized_error_percent": 0.23682778311822578,
      "absolute_error": {
        "p95": 0.12606143951416016,
        "p99": 0.1365127086639404,
        "maximum": 0.1400752067565918
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 19.553373336791992,
      "reference_fraction_of_uniform": 0.69650799036026,
      "rms_normalized_to_uniform_percent": 0.1528834218237937
    },
    "west": {
      "bias_percent": 0.1068934995794126,
      "rms_normalized_error_percent": 0.2530997200721627,
      "absolute_error": {
        "p95": 0.038431644439697266,
        "p99": 0.049708130955696095,
        "maximum": 0.05194026231765747
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.376743316650391,
      "reference_fraction_of_uniform": 0.1915242224931717,
      "rms_normalized_to_uniform_percent": 0.052270140025597496
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
        "identifier": "teaching_wwr40_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.0716355042696838,
          "cvrmse_percent": 0.9671669599040625,
          "absolute_error_percentiles_lux": {
            "p50": 4.041748046875,
            "p90": 35.0240905761719,
            "p95": 51.53079833984374,
            "p99": 96.53743530273435
          },
          "maximum_absolute_error_lux": 429.54296875,
          "worst": {
            "sensor_index": 4,
            "position": [
              0.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2603.5,
            "foton_lux": 17598.041015625,
            "radiance_lux": 18027.583984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.08460806697108107,
            "maximum_error_percentage_points": 0.4399999999999977,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.044503197809979786,
            "maximum_error_percentage_points": 0.17775349553865283,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.03270547945205498,
            "maximum_error_percentage_points": 0.22068493150684887,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.05688356164383536,
            "maximum_error_percentage_points": 0.19383561643834923,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.06178843226788452,
            "maximum_error_percentage_points": 0.2184931506849317,
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
      "maximum_error_percentage_points": 0.004977525684935813,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004977525684935813,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_wwr40_grid",
            "maximum_error_percentage_points": 0.004520547945205511,
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
      "study_preparation_seconds": 0.005667082965373993,
      "weather_seconds": 0.09251849993597716,
      "metric_reduction_seconds": 0.03746054193470627,
      "write_seconds": 0.040772583917714655,
      "total_seconds": 0.17086891608778387,
      "cold_end_to_end_seconds": 0.17653599905315787,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.012648000032640994,
      "engine_upload_seconds": 0.000280417,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01925749983638525,
      "engine_annual_reduction_seconds": 0.00037883338518440723,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01925749983638525
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.005667082965373993,
      "weather_seconds": 0.09127541701309383,
      "metric_reduction_seconds": 0.011404666933231056,
      "write_seconds": 0.03781879204325378,
      "total_seconds": 0.14130037499126047,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14130037499126047,
      "raw_export_seconds": 0.009829582995735109,
      "engine_upload_seconds": 5.075e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00035254168324172497,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01403479091823101,
      "full": 0.03009429096709937
    }
  },
  "elapsed_seconds": 0.6971530420705676,
  "result_class": "passed"
}
```
