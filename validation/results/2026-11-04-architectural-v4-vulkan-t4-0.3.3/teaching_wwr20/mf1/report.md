# Foton report

Status: **passed**

```json
{
  "scene": "teaching_wwr20",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_wwr20",
    "category": "teaching",
    "question": "How does a 20% window-to-wall ratio light the base room?",
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
    "aperture_area": 3.6018000000000003
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "faa046c6774f3d3baf87bf4e611318cbb8af308ca7f631005c47ca76daf5a564",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 1765380858695198131,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 1765380858695198131,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "97042f26c1eaa8818393fd2c3cfb3f6fdbddb22b0a625cebd3cdebc8a3301077",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "42ebbd5873d9863a0ad3aca60e92d9e55c1ae842623c6cc1f4949849ae92cd10",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 8
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.000839495100080967,
          "p95": 1.385388895869255e-05,
          "p99": 0.00012764893472194672
        },
        "bias_percent": 0.12710287061951422,
        "identifier": "teaching_wwr20_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.2992380823772811,
        "worst_index": [
          5,
          119,
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
          "maximum": 0.0005334988236427307,
          "p95": 6.979510653764002e-05,
          "p99": 0.00017477769870311022
        },
        "bias_percent": 0.05974743297939245,
        "identifier": "teaching_wwr20_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1617589350994924,
        "worst_index": [
          9,
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
          "maximum": 0.00042052753269672394,
          "p95": 5.7496939552947846e-05,
          "p99": 0.00013876194134354591
        },
        "bias_percent": 0.0013124769537545156,
        "identifier": "teaching_wwr20_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9482894977488934,
        "worst_index": [
          26,
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
            "identifier": "teaching_wwr20_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0006187772378325462,
                  "p50": 0.0,
                  "p90": 2.325075911357999e-05,
                  "p95": 0.00015711965679656706,
                  "p99": 0.0003705359995365143
                },
                "candidate_energy": 7.801907313320044,
                "cvrmse_percent": 14.269166098636738,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.11824396110222737,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.792692924529547,
                "relative_energy_error_percent": 0.11824396110222736,
                "rms_normalized_rmse_percent": 3.411930272159409,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01505244243890047,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.015671219676733017,
                  "rgb_channel": 0,
                  "sky_patch_index": 97
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008730771951377392,
                  "p50": 0.0,
                  "p90": 4.545331285044085e-05,
                  "p95": 0.00020294193382142104,
                  "p99": 0.00045022007543593645
                },
                "candidate_energy": 2.2102836410618423,
                "cvrmse_percent": 64.3992009862343,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5526076814398673,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.222565709899797,
                "relative_energy_error_percent": 0.5526076814398673,
                "rms_normalized_rmse_percent": 3.475397504583114,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0003898274153470993,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0004832497797906399,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.04758404288441,
            "full": 231.43245896790177
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.58429198339581,
            "full": 233.51175000425428
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.6745420563966,
            "full": 252.52583296969533
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.22041696682572,
            "full": 230.78912496566772
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.68787498679012,
            "full": 241.85037496499717
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.13079097494483,
            "full": 244.03470801189542
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 115.64116599038243,
            "full": 223.8582910504192
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 117.12645797524601,
            "full": 226.04650002904236
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
            "identifier": "teaching_wwr20_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005525778979063034,
                  "p50": 0.0,
                  "p90": 2.0744744688272476e-05,
                  "p95": 8.374499157071114e-05,
                  "p99": 0.00020720716565847397
                },
                "candidate_energy": 7.790782553949612,
                "cvrmse_percent": 8.46372643394673,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.012898034852140541,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.791787541422309,
                "relative_energy_error_percent": 0.012898034852140541,
                "rms_normalized_rmse_percent": 2.0243367542840085,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006979732075706124,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.007532309973612428,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008020901586860418,
                  "p50": 2.2694325352290434e-07,
                  "p90": 4.309602081775665e-05,
                  "p95": 0.00013530972282751447,
                  "p99": 0.0003171800635755062
                },
                "candidate_energy": 4.2954314360152175,
                "cvrmse_percent": 23.55302260081481,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.07375160616954983,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.29226582103114,
                "relative_energy_error_percent": 0.07375160616954982,
                "rms_normalized_rmse_percent": 2.03243238230052,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0005553595256060362,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": -0.00024673063308000565,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.09383295848966,
            "full": 2292.303916066885
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.13979200273752,
            "full": 2279.5516659971327
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.8316250294447,
            "full": 2247.2667089896277
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.74187505058944,
            "full": 2288.6319999815896
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
            "identifier": "teaching_wwr20_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003696344792842865,
                  "p50": 0.0,
                  "p90": 1.7807004041969776e-05,
                  "p95": 8.074608049355441e-05,
                  "p99": 0.00020287511870265007
                },
                "candidate_energy": 7.7880516433051525,
                "cvrmse_percent": 7.871536923114593,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.01960945313766875,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.789579137175679,
                "relative_energy_error_percent": 0.01960945313766875,
                "rms_normalized_rmse_percent": 1.8839480632030456,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006035211030393839,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.006404845509678125,
                  "rgb_channel": 0,
                  "sky_patch_index": 51
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007757935672998428,
                  "p50": 2.8288295794709484e-07,
                  "p90": 4.45834593847394e-05,
                  "p95": 0.00012848325131926687,
                  "p99": 0.0002965470775961876
                },
                "candidate_energy": 4.306252584582175,
                "cvrmse_percent": 22.773045283039078,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1261975113375084,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.300825050401588,
                "relative_energy_error_percent": 0.1261975113375084,
                "rms_normalized_rmse_percent": 1.968337574790782,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.03209882415831089,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.03132303059101105,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.63999995961785,
            "full": 2451.756375026889
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.59408303163946,
            "full": 2416.4658749941736
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 150.71304095909,
            "full": 2427.922709030099
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 147.74516690522432,
            "full": 2395.6889580003917
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
            "identifier": "teaching_wwr20_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00022779044229537249,
                  "p50": 0.0,
                  "p90": 1.1012667528120801e-05,
                  "p95": 4.6689895680174214e-05,
                  "p99": 0.00011697650188580155
                },
                "candidate_energy": 7.789368129480863,
                "cvrmse_percent": 4.679978056827989,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.00547978437173903,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 7.7897949934495045,
                "relative_energy_error_percent": 0.005479784371739031,
                "rms_normalized_rmse_percent": 1.1197566241208057,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.002401118981651962,
                  "global_sensor_index": 35,
                  "local_sensor_index": 35,
                  "reference": 0.0021733285393565893,
                  "rgb_channel": 0,
                  "sky_patch_index": 20
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005940841510891914,
                  "p50": 1.6986712125799386e-07,
                  "p90": 2.792361192405224e-05,
                  "p95": 7.777053979225455e-05,
                  "p99": 0.0001828569802455604
                },
                "candidate_energy": 4.301913678943492,
                "cvrmse_percent": 14.343763847035452,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.047289899418185934,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.303949012102326,
                "relative_energy_error_percent": 0.047289899418185934,
                "rms_normalized_rmse_percent": 1.2389060797424671,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.02656612452119589,
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "reference": 0.025972040370106697,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 235.23895896505564,
            "full": 4205.009792000055
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 219.9860829859972,
            "full": 4248.877834063023
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 214.70808307640254,
            "full": 4166.525000007823
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 212.4631250044331,
            "full": 4150.094208074734
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
    "/content/suite-vulkan-0.3.3/teaching_wwr20/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 779.9637919524685,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_wwr20/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2863.8502499088645,
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
        "identifier": "teaching_wwr20_grid",
        "full_identifier": "teaching_wwr20_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.14887642449386634,
            "cvrmse_percent": 2.921787998258796,
            "rms_normalized_rmse_percent": 0.6988582936460392,
            "reference_energy": 7.798894989354267,
            "candidate_energy": 7.787284273344085,
            "relative_energy_error_percent": 0.14887642449386637,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.8079375624656677e-07,
              "p95": 9.478069841861725e-06,
              "p99": 6.590614793822169e-05,
              "maximum": 0.0002804058603942394
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 119,
              "rgb_channel": 0,
              "reference": 0.005756907165050507,
              "candidate": 0.005476501304656267,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.7498486560127137,
            "cvrmse_percent": 20.920068260645895,
            "rms_normalized_rmse_percent": 1.8033776750159736,
            "reference_energy": 4.293617923700914,
            "candidate_energy": 4.261422287405722,
            "relative_energy_error_percent": 0.7498486560127137,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.698419383610599e-07,
              "p90": 4.082407394889742e-05,
              "p95": 6.276523345150048e-05,
              "p99": 0.00014551309868693352,
              "maximum": 0.001230316236615181
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030715815722942352,
              "candidate": 0.02948549948632717,
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
            "nmbe_percent": -0.3622601242631752,
            "cvrmse_percent": 7.3904887123537355,
            "rms_normalized_rmse_percent": 1.794278752546018,
            "reference_energy": 12.092512913055181,
            "candidate_energy": 12.048706560749807,
            "relative_energy_error_percent": 0.36226012426317533,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.894127864143229e-07,
              "p90": 4.0091254049912095e-05,
              "p95": 6.125695072114466e-05,
              "p99": 0.00014071259647607803,
              "maximum": 0.001230316236615181
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.030715815722942352,
              "candidate": 0.02948549948632717,
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
        "identifier": "teaching_wwr20_grid",
        "full_identifier": "teaching_wwr20_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.14887642449386634,
            "cvrmse_percent": 2.921787998258796,
            "rms_normalized_rmse_percent": 0.6988582936460392,
            "reference_energy": 7.798894989354267,
            "candidate_energy": 7.787284273344085,
            "relative_energy_error_percent": 0.14887642449386637,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.8079375624656677e-07,
              "p95": 9.478069841861725e-06,
              "p99": 6.590614793822169e-05,
              "maximum": 0.0002804058603942394
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 119,
              "rgb_channel": 0,
              "reference": 0.005756907165050507,
              "candidate": 0.005476501304656267,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 92.4040500159624,
            "cvrmse_percent": 518.2121360815665,
            "rms_normalized_rmse_percent": 27.86341847658182,
            "reference_energy": 2.214829826634201,
            "candidate_energy": 4.261422287405722,
            "relative_energy_error_percent": 92.40405001596243,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002654499839991331,
              "p95": 0.00034074739087373005,
              "p99": 0.0005051050102338195,
              "maximum": 0.009642095305025578
            },
            "worst": {
              "global_sensor_index": 1,
              "local_sensor_index": 1,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013418263755738735,
              "candidate": 0.023060359060764313,
              "position": [
                0.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.321925978155242,
            "cvrmse_percent": 114.59171817023798,
            "rms_normalized_rmse_percent": 27.857063767719957,
            "reference_energy": 10.013724815988468,
            "candidate_energy": 12.048706560749807,
            "relative_energy_error_percent": 20.321925978155246,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00026296000578440726,
              "p95": 0.00033832405952125553,
              "p99": 0.0005015479400753975,
              "maximum": 0.009642095305025578
            },
            "worst": {
              "global_sensor_index": 1,
              "local_sensor_index": 1,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.013418263755738735,
              "candidate": 0.023060359060764313,
              "position": [
                0.5,
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
  "controlled_skies": {
    "uniform": {
      "bias_percent": 0.02085097917911525,
      "rms_normalized_error_percent": 0.215102563335649,
      "absolute_error": {
        "p95": 0.0977296293341241,
        "p99": 0.11425019100710898,
        "maximum": 0.1148377319735765
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.068990866856703,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.215102563335649
    },
    "overcast": {
      "bias_percent": 0.005216503074223215,
      "rms_normalized_error_percent": 0.21294232263755242,
      "absolute_error": {
        "p95": 0.06657731533050537,
        "p99": 0.07309347391128539,
        "maximum": 0.074859619140625
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.191654205322266,
      "reference_fraction_of_uniform": 0.6099714636802673,
      "rms_normalized_to_uniform_percent": 0.1388020968348127
    },
    "horizon": {
      "bias_percent": 0.145800243179265,
      "rms_normalized_error_percent": 1.0677763346236588,
      "absolute_error": {
        "p95": 0.04274472028423046,
        "p99": 0.04769992259804687,
        "maximum": 0.050298902078041774
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.8361035706771338,
      "reference_fraction_of_uniform": 0.12184648506991454,
      "rms_normalized_to_uniform_percent": 0.0843505070477614
    },
    "north": {
      "bias_percent": -70.6280187473142,
      "rms_normalized_error_percent": 103.28188991232736,
      "absolute_error": {
        "p95": 6.760063752153656e-05,
        "p99": 0.00032058628621598427,
        "maximum": 0.0004388924571685493
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.4768027287791483e-05,
      "reference_fraction_of_uniform": 1.6436421219623298e-06,
      "rms_normalized_to_uniform_percent": 0.000305015031146056
    },
    "east": {
      "bias_percent": 0.20983538271786925,
      "rms_normalized_error_percent": 0.4240719006005201,
      "absolute_error": {
        "p95": 0.05460560321807861,
        "p99": 0.055932688713073726,
        "maximum": 0.056209564208984375
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.0414609909057617,
      "reference_fraction_of_uniform": 0.2018357515335083,
      "rms_normalized_to_uniform_percent": 0.09050468290135102
    },
    "south": {
      "bias_percent": 0.030360306361010534,
      "rms_normalized_error_percent": 0.22724528906129762,
      "absolute_error": {
        "p95": 0.07610109448432922,
        "p99": 0.09661101102828978,
        "maximum": 0.09794139862060547
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.97412109375,
      "reference_fraction_of_uniform": 0.7282585501670837,
      "rms_normalized_to_uniform_percent": 0.15786077252651026
    },
    "west": {
      "bias_percent": -0.11955070687505301,
      "rms_normalized_error_percent": 0.36404130928559936,
      "absolute_error": {
        "p95": 0.032584138214588165,
        "p99": 0.0411635473370552,
        "maximum": 0.043862342834472656
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.9474945068359375,
      "reference_fraction_of_uniform": 0.1955999881029129,
      "rms_normalized_to_uniform_percent": 0.07589717860395609
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
        "identifier": "teaching_wwr20_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.02101157406844495,
          "cvrmse_percent": 1.4954825262477969,
          "absolute_error_percentiles_lux": {
            "p50": 2.9221038818359375,
            "p90": 27.76226501464844,
            "p95": 41.029663085937415,
            "p99": 80.43747680664056
          },
          "maximum_absolute_error_lux": 302.7763671875,
          "worst": {
            "sensor_index": 29,
            "position": [
              4.5,
              0.5,
              0.75
            ],
            "hour_of_year": 3829.5,
            "foton_lux": 14294.701171875,
            "radiance_lux": 14597.4775390625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.49955098934550957,
            "maximum_error_percentage_points": 2.4917808219178106,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.18035712668762413,
            "maximum_error_percentage_points": 0.6560985380001512,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.11121765601217698,
            "maximum_error_percentage_points": 0.5171232876712324,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.12000380517503927,
            "maximum_error_percentage_points": 0.5171232876712395,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.022861491628614852,
            "maximum_error_percentage_points": 0.0871232876712329,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 63.888888888888886,
          "radiance_percent": 63.888888888888886,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_wwr20_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_wwr20_grid",
            "maximum_error_percentage_points": 0.004831175085598716,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_wwr20_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_wwr20_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_wwr20_grid",
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
      "study_preparation_seconds": 0.37225341199996365,
      "weather_seconds": 0.2258516409999629,
      "metric_reduction_seconds": 0.15797945499980415,
      "write_seconds": 0.012565023999968616,
      "total_seconds": 0.3967716269999073,
      "cold_end_to_end_seconds": 0.769025038999871,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0015867800000251009,
      "engine_upload_seconds": 0.013708577,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01061566,
      "engine_annual_reduction_seconds": 0.008954067,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01061566
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.37225341199996365,
      "weather_seconds": 0.22205072599990672,
      "metric_reduction_seconds": 0.15361134899990248,
      "write_seconds": 0.011771884999916438,
      "total_seconds": 0.38777118300004076,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.38777118300004076,
      "raw_export_seconds": 0.0013856820000910375,
      "engine_upload_seconds": 0.013892946,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 1.49e-07,
      "engine_annual_reduction_seconds": 0.009475527,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01425137100000029,
      "full": 0.02151810099985596
    }
  },
  "elapsed_seconds": 2.7824682549999125,
  "result_class": "passed"
}
```
