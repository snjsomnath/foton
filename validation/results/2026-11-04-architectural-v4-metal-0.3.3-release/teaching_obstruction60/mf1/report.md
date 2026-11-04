# Foton report

Status: **passed**

```json
{
  "scene": "teaching_obstruction60",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_obstruction60",
    "category": "teaching",
    "question": "How does a 60 degree obstruction angle reduce sky access?",
    "interactions": [
      "multiple_bounces",
      "obstruction",
      "side_glazing"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 6,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "db5625deb8db03a8d7322d6dc9c2644129f561f20f0f70b8c1f45d06525a763c",
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 12158479806775792312,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 12158479806775792312,
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
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "ff22f87a8905b0de061a60a41a433c7fe95b67b5b4fbcb49bbc35529bbe47eb7",
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
          "maximum": 0.000557776540517807,
          "p95": 0.0,
          "p99": 4.568975418806076e-05
        },
        "bias_percent": -0.837493211991913,
        "identifier": "teaching_obstruction60_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.450441784842407,
        "worst_index": [
          11,
          116,
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
          "maximum": 0.0007744058966636658,
          "p95": 4.0046109643299115e-05,
          "p99": 9.753182530403137e-05
        },
        "bias_percent": 0.1401483865792966,
        "identifier": "teaching_obstruction60_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8551078493025219,
        "worst_index": [
          14,
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
          "maximum": 0.0005623176693916321,
          "p95": 3.3387486473657145e-05,
          "p99": 7.735565304756165e-05
        },
        "bias_percent": -0.05115212689802525,
        "identifier": "teaching_obstruction60_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.6920483607852634,
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
            "identifier": "teaching_obstruction60_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005102953873574734,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0001125050475820899
                },
                "candidate_energy": 1.3365488400286267,
                "cvrmse_percent": 26.23295029781,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.30715372339428537,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.340666747862997,
                "relative_energy_error_percent": 0.30715372339428537,
                "rms_normalized_rmse_percent": 2.653559328628327,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013927095104008913,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.01341679971665144,
                  "rgb_channel": 0,
                  "sky_patch_index": 134
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013702362775802612,
                  "p50": 2.845725362021767e-07,
                  "p90": 5.587874511547852e-05,
                  "p95": 9.62377544055923e-05,
                  "p99": 0.00027270906139165163
                },
                "candidate_energy": 3.8878692271803317,
                "cvrmse_percent": 27.8056231377248,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1995921613641542,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.8801248022239463,
                "relative_energy_error_percent": 0.1995921613641542,
                "rms_normalized_rmse_percent": 2.4038359641706966,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05690842494368553,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.05553818866610527,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.056749984622,
            "full": 229.03591697104275
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 108.58262504916638,
            "full": 225.1437499653548
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.92370800301433,
            "full": 227.68279199954122
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 104.55908300355077,
            "full": 227.64162498060614
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
            "identifier": "teaching_obstruction60_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00024468335323035717,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.802050534635782e-05
                },
                "candidate_energy": 1.3394350217158717,
                "cvrmse_percent": 15.13973968812804,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.10008520256889955,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3380957858380498,
                "relative_energy_error_percent": 0.10008520256889955,
                "rms_normalized_rmse_percent": 1.5280185831184938,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004835894331336021,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.004591210978105664,
                  "rgb_channel": 0,
                  "sky_patch_index": 52
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006147474050521851,
                  "p50": 4.768711846736551e-06,
                  "p90": 3.4801407309714705e-05,
                  "p95": 5.8581700250215323e-05,
                  "p99": 0.00017340108752250671
                },
                "candidate_energy": 5.395055093025018,
                "cvrmse_percent": 10.95305716894307,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.09020063410961383,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.390193104664878,
                "relative_energy_error_percent": 0.09020063410961385,
                "rms_normalized_rmse_percent": 1.047461932538343,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06625224277377129,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0656374953687191,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 140.2252089465037,
            "full": 2202.0165419671685
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.71629097592086,
            "full": 2161.8616249179468
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.14408396277577,
            "full": 2208.081375109032
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 128.235875046812,
            "full": 2169.4564589997754
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
            "identifier": "teaching_obstruction60_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002790866419672966,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.3178955568000674e-05
                },
                "candidate_energy": 1.3379155449774771,
                "cvrmse_percent": 13.29292688991043,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0932589239232986,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.33666898186857,
                "relative_energy_error_percent": 0.09325892392329858,
                "rms_normalized_rmse_percent": 1.3419426390091471,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00957233039662242,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.009293243754655123,
                  "rgb_channel": 0,
                  "sky_patch_index": 120
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007974598556756973,
                  "p50": 4.909235258310218e-06,
                  "p90": 3.613119770307094e-05,
                  "p95": 5.6774903168843596e-05,
                  "p99": 0.00013922125799581409
                },
                "candidate_energy": 5.403023755444476,
                "cvrmse_percent": 12.358844410707816,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.01877827832687623,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.404038540842567,
                "relative_energy_error_percent": 0.01877827832687623,
                "rms_normalized_rmse_percent": 1.181404334890293,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.055129149928689,
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "reference": 0.054331690073013306,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.5142919300124,
            "full": 2330.3364579332992
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 139.2088329885155,
            "full": 2355.6877500377595
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.12866699136794,
            "full": 2276.5424590324983
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.06729197129607,
            "full": 2328.960790997371
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
            "identifier": "teaching_obstruction60_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00012566149234771729,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.685078652575612e-05
                },
                "candidate_energy": 1.339779088688374,
                "cvrmse_percent": 6.861655885540278,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.012382828168824092,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.3396132066868631,
                "relative_energy_error_percent": 0.012382828168824092,
                "rms_normalized_rmse_percent": 0.6929060440142852,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004336237441748381,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004210575949400663,
                  "rgb_channel": 0,
                  "sky_patch_index": 93
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0004844311624765396,
                  "p50": 3.4785787192959106e-06,
                  "p90": 2.3790198611095548e-05,
                  "p95": 3.9676020969636696e-05,
                  "p99": 9.571478585712612e-05
                },
                "candidate_energy": 5.39952433327182,
                "cvrmse_percent": 7.88030108919504,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.06839333998030088,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.395833942218946,
                "relative_energy_error_percent": 0.06839333998030088,
                "rms_normalized_rmse_percent": 0.7527715110918498,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.04529908485710621,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.04578351601958275,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 185.00079202931374,
            "full": 4051.5836670529097
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.18024995643646,
            "full": 4133.604542003013
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.43229105509818,
            "full": 4001.9717500545084
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.35045795235783,
            "full": 4045.118041918613
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/teaching_obstruction60/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 788.7283749878407,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_obstruction60/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2808.019708027132,
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
        "identifier": "teaching_obstruction60_grid",
        "full_identifier": "teaching_obstruction60_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.13257707882315467,
            "cvrmse_percent": 13.419859335031074,
            "rms_normalized_rmse_percent": 1.3563262919789376,
            "reference_energy": 1.3416702660251758,
            "candidate_energy": 1.3434490132713108,
            "relative_energy_error_percent": 0.13257707882315467,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.5705586671829224e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.3063845575748223,
            "cvrmse_percent": 21.53655242572843,
            "rms_normalized_rmse_percent": 2.05762663073796,
            "reference_energy": 5.395705028165333,
            "candidate_energy": 5.325216370905093,
            "relative_energy_error_percent": 1.3063845575748223,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.801632141810842e-06,
              "p90": 2.6159135813941248e-05,
              "p95": 3.753479104489087e-05,
              "p99": 9.297917131334543e-05,
              "maximum": 0.0018349960446357727
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05120617523789406,
              "candidate": 0.049371179193258286,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.0198320119312954,
            "cvrmse_percent": 17.20643969389606,
            "rms_normalized_rmse_percent": 2.052692739449149,
            "reference_energy": 6.7373752941905085,
            "candidate_energy": 6.668665384176403,
            "relative_energy_error_percent": 1.0198320119312954,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.801632141810842e-06,
              "p90": 2.604226756375283e-05,
              "p95": 3.768406058952671e-05,
              "p99": 9.208079427480698e-05,
              "maximum": 0.0018349960446357727
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05120617523789406,
              "candidate": 0.049371179193258286,
              "position": [
                3.5,
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
        "identifier": "teaching_obstruction60_grid",
        "full_identifier": "teaching_obstruction60_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.13257707882315467,
            "cvrmse_percent": 13.419859335031074,
            "rms_normalized_rmse_percent": 1.3563262919789376,
            "reference_energy": 1.3416702660251758,
            "candidate_energy": 1.3434490132713108,
            "relative_energy_error_percent": 0.13257707882315467,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 4.5705586671829224e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 37.214794543456286,
            "cvrmse_percent": 330.2842925745894,
            "rms_normalized_rmse_percent": 28.585679468558705,
            "reference_energy": 3.88093455128017,
            "candidate_energy": 5.325216370905093,
            "relative_energy_error_percent": 37.21479454345629,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.8804480532708112e-05,
              "p90": 7.108625140972435e-05,
              "p95": 9.525907630631988e-05,
              "p99": 0.00022104824893176556,
              "maximum": 0.011562742292881012
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02404932677745819,
              "candidate": 0.0356120690703392,
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
            "nmbe_percent": 27.688492954310245,
            "cvrmse_percent": 245.423515007299,
            "rms_normalized_rmse_percent": 28.584303696840596,
            "reference_energy": 5.222604817305346,
            "candidate_energy": 6.668665384176403,
            "relative_energy_error_percent": 27.688492954310238,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.8774498130369466e-05,
              "p90": 7.108000136213377e-05,
              "p95": 9.471444557220813e-05,
              "p99": 0.00022704689763486385,
              "maximum": 0.011562742292881012
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02404932677745819,
              "candidate": 0.0356120690703392,
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
      "bias_percent": 0.13556870562071296,
      "rms_normalized_error_percent": 0.36155893390042526,
      "absolute_error": {
        "p95": 0.05162957243445501,
        "p99": 0.08466572242500087,
        "maximum": 0.09689121587480187
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.2002721063496855,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.36155893390042526
    },
    "overcast": {
      "bias_percent": 0.1721399341441913,
      "rms_normalized_error_percent": 0.3657249700998912,
      "absolute_error": {
        "p95": 0.039460375905036926,
        "p99": 0.07571182250976558,
        "maximum": 0.08780288696289062
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.040983200073242,
      "reference_fraction_of_uniform": 0.7239966988563538,
      "rms_normalized_to_uniform_percent": 0.2829268057148623
    },
    "horizon": {
      "bias_percent": -0.5151570008719045,
      "rms_normalized_error_percent": 1.7622902412251706,
      "absolute_error": {
        "p95": 0.023050736123990237,
        "p99": 0.03252386492446897,
        "maximum": 0.03713756708538596
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.47453800613999914,
      "reference_fraction_of_uniform": 0.11297792003109153,
      "rms_normalized_to_uniform_percent": 0.13815539747897762
    },
    "north": {
      "bias_percent": 0.19179031386006098,
      "rms_normalized_error_percent": 0.6935578510206656,
      "absolute_error": {
        "p95": 0.019698157906532288,
        "p99": 0.020396947860717773,
        "maximum": 0.02070319652557373
      },
      "worst_index": [
        19
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.071606993675232,
      "reference_fraction_of_uniform": 0.25512799620628357,
      "rms_normalized_to_uniform_percent": 0.12811244766955968
    },
    "east": {
      "bias_percent": 0.1220281127502278,
      "rms_normalized_error_percent": 0.4651253955447809,
      "absolute_error": {
        "p95": 0.01682722568511963,
        "p99": 0.02169944047927856,
        "maximum": 0.022580385208129883
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0162842273712158,
      "reference_fraction_of_uniform": 0.24195675551891327,
      "rms_normalized_to_uniform_percent": 0.11818629853184785
    },
    "south": {
      "bias_percent": 0.23532355984274933,
      "rms_normalized_error_percent": 0.476607649782569,
      "absolute_error": {
        "p95": 0.020260006189346313,
        "p99": 0.03746895790100096,
        "maximum": 0.042441368103027344
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9041883945465088,
      "reference_fraction_of_uniform": 0.21526899933815002,
      "rms_normalized_to_uniform_percent": 0.1303376479916649
    },
    "west": {
      "bias_percent": -0.03786045747175667,
      "rms_normalized_error_percent": 0.6171528420772265,
      "absolute_error": {
        "p95": 0.02301279455423355,
        "p99": 0.033883288502693155,
        "maximum": 0.03892648220062256
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9713560938835144,
      "reference_fraction_of_uniform": 0.231260284781456,
      "rms_normalized_to_uniform_percent": 0.14951202625524723
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
        "identifier": "teaching_obstruction60_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.21148527801375616,
          "cvrmse_percent": 3.7174393692780376,
          "absolute_error_percentiles_lux": {
            "p50": 1.2296934127807617,
            "p90": 9.647503662109381,
            "p95": 15.364794921874996,
            "p99": 34.71766265869116
          },
          "maximum_absolute_error_lux": 278.08251953125,
          "worst": {
            "sensor_index": 23,
            "position": [
              3.5,
              0.5,
              0.75
            ],
            "hour_of_year": 3827.5,
            "foton_lux": 7534.8330078125,
            "radiance_lux": 7256.75048828125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.28889269406392715,
            "maximum_error_percentage_points": 1.2300000000000004,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4258731408307523,
            "maximum_error_percentage_points": 1.1149723794688526,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5820433789954341,
            "maximum_error_percentage_points": 2.543287671232875,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.587667427701674,
            "maximum_error_percentage_points": 2.5432876712328785,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.007583713850837202,
            "maximum_error_percentage_points": 0.11260273972602874,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 11.11111111111111,
          "radiance_percent": 11.11111111111111,
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
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.004803349743148999,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_obstruction60_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
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
      "study_preparation_seconds": 0.006012332974933088,
      "weather_seconds": 0.07603120896965265,
      "metric_reduction_seconds": 0.03716199996415526,
      "write_seconds": 0.010671457974240184,
      "total_seconds": 0.1239810410188511,
      "cold_end_to_end_seconds": 0.1299933739937842,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.002107082982547581,
      "engine_upload_seconds": 0.000259167,
      "engine_acceleration_structure_seconds": 0.002904417,
      "engine_tracing_seconds": 0.014396583312191069,
      "engine_annual_reduction_seconds": 0.00034870835952460766,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.014396583312191069
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006012332974933088,
      "weather_seconds": 0.07330699998419732,
      "metric_reduction_seconds": 0.013469666941091418,
      "write_seconds": 0.009574000025168061,
      "total_seconds": 0.09645987499970943,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.09645987499970943,
      "raw_export_seconds": 0.0014068341115489602,
      "engine_upload_seconds": 4.775e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003726249560713768,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.05893691605888307,
      "full": 0.024149166070856154
    }
  },
  "elapsed_seconds": 0.7733082909835503,
  "result_class": "passed"
}
```
