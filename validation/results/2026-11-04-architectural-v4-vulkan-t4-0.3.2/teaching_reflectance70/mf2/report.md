# Foton report

Status: **passed**

```json
{
  "scene": "teaching_reflectance70",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_reflectance70",
    "category": "teaching",
    "question": "How much does 0.7 surface reflectance add at the back of the room?",
    "interactions": [
      "multiple_bounces",
      "reflectance",
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
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "a5931ee8f597e16d585b8999dc55ac54d2265dc4b6f387c64199bdcfbf093612",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 18345719022415901050,
      "basis": "ReinhartMf2",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 18345719022415901050,
      "basis": "ReinhartMf2",
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
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "604bce1ee9039eb5453e17b9f49feda721ce1a628c0bae6531660592d3375aa4",
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
          "maximum": 0.00014028436271473765,
          "p95": 1.1152587831020355e-07,
          "p99": 1.1820709914900362e-05
        },
        "bias_percent": -0.02181882161705929,
        "identifier": "teaching_reflectance70_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7580187937848226,
        "worst_index": [
          17,
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
          "maximum": 0.0015106871724128723,
          "p95": 4.76206187158823e-05,
          "p99": 0.00012187310494482517
        },
        "bias_percent": 0.7691581691183266,
        "identifier": "teaching_reflectance70_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5153828620458238,
        "worst_index": [
          10,
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
          "maximum": 0.0009623691439628601,
          "p95": 3.732158802449703e-05,
          "p99": 0.00010250811465084553
        },
        "bias_percent": -0.032935747186264026,
        "identifier": "teaching_reflectance70_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8913074398778963,
        "worst_index": [
          16,
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
            "identifier": "teaching_reflectance70_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005537210963666439,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 8.295249426737428e-05,
                  "p99": 0.00022256825104705058
                },
                "candidate_energy": 8.948120656017636,
                "cvrmse_percent": 27.9451585792222,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.0934454823181137,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.939766847768624,
                "relative_energy_error_percent": 0.09344548231811367,
                "rms_normalized_rmse_percent": 6.536398729404459,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003261498990468681,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.0038152200868353248,
                  "rgb_channel": 0,
                  "sky_patch_index": 267
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012021753937005997,
                  "p50": 0.0,
                  "p90": 1.540557195767185e-05,
                  "p95": 0.0001111826113628922,
                  "p99": 0.0003386774333193898
                },
                "candidate_energy": 4.373810785187281,
                "cvrmse_percent": 92.8921657746052,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.4501953948267082,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.39359052740922,
                "relative_energy_error_percent": 0.45019539482670823,
                "rms_normalized_rmse_percent": 3.9888221705771074,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.05019214376807213,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.04898996837437153,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.63287496939301,
            "full": 239.46974996943027
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.8497500307858,
            "full": 234.75949990097433
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 122.55179195199162,
            "full": 245.2042909571901
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 123.80058295093477,
            "full": 243.18537500221282
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
            "identifier": "teaching_reflectance70_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00039394403574988246,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6212386223487556e-05,
                  "p99": 0.00014771654969081283
                },
                "candidate_energy": 8.946392409148757,
                "cvrmse_percent": 19.57413789294796,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.06275813631375626,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.952010524116304,
                "relative_energy_error_percent": 0.06275813631375626,
                "rms_normalized_rmse_percent": 4.58496770029666,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.001667345524765551,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.0012734014890156686,
                  "rgb_channel": 0,
                  "sky_patch_index": 148
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0013951696455478668,
                  "p50": 8.55979305214305e-08,
                  "p90": 3.849379791063265e-05,
                  "p95": 8.15398816484958e-05,
                  "p99": 0.00023164739832282066
                },
                "candidate_energy": 11.775113097473383,
                "cvrmse_percent": 25.985779521921625,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.1466976137376574,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.792412284897434,
                "relative_energy_error_percent": 0.1466976137376574,
                "rms_normalized_rmse_percent": 1.6937941742767348,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0690617710351944,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.07045694068074226,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 164.74458307493478,
            "full": 2422.11895796936
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.3186249481514,
            "full": 2431.0175830032676
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.391291026026,
            "full": 2440.5440830159932
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 160.87750007864088,
            "full": 2404.8937499755993
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
            "identifier": "teaching_reflectance70_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003795464290305972,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.704465391114354e-05,
                  "p99": 0.00016256853996310383
                },
                "candidate_energy": 8.952862549572274,
                "cvrmse_percent": 20.507737676384302,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.12024981147869317,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.942109679540408,
                "relative_energy_error_percent": 0.12024981147869315,
                "rms_normalized_rmse_percent": 4.799433373126681,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003477180958725512,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.003097634529694915,
                  "rgb_channel": 0,
                  "sky_patch_index": 269
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011758580803871155,
                  "p50": 9.001168876920929e-08,
                  "p90": 3.873466739605649e-05,
                  "p95": 8.369967690669e-05,
                  "p99": 0.00023026089183986187
                },
                "candidate_energy": 11.937391428756158,
                "cvrmse_percent": 25.0104754064169,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.12643325923990664,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.952503368325491,
                "relative_energy_error_percent": 0.12643325923990667,
                "rms_normalized_rmse_percent": 1.6354350952631413,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07125576958060265,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.07243162766098976,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.27020797971636,
            "full": 2795.927166007459
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 169.36433303635567,
            "full": 2720.6527090165764
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 192.98270798753947,
            "full": 2761.0020840074867
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.2144590318203,
            "full": 2700.2822919748724
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
            "identifier": "teaching_reflectance70_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00018381845438852906,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.5026645744219422e-05,
                  "p99": 8.774048183113337e-05
                },
                "candidate_energy": 8.950327236961584,
                "cvrmse_percent": 11.167448764668844,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0030620566267701545,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.950053181265048,
                "relative_energy_error_percent": 0.003062056626770154,
                "rms_normalized_rmse_percent": 2.6167263573819666,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016413070261478424,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.0018251254805363715,
                  "rgb_channel": 0,
                  "sky_patch_index": 155
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010080337524414062,
                  "p50": 6.80648497564107e-08,
                  "p90": 2.530807760194883e-05,
                  "p95": 4.9471971578896046e-05,
                  "p99": 0.00013770309669780545
                },
                "candidate_energy": 11.9412813047634,
                "cvrmse_percent": 16.796697461137516,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.09923643747334014,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.929442950568841,
                "relative_energy_error_percent": 0.09923643747334014,
                "rms_normalized_rmse_percent": 1.098489282064436,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.08286995813250542,
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "reference": 0.08186192438006401,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 220.87629104498774,
            "full": 5200.895791989751
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 228.87970798183233,
            "full": 5306.577124982141
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 222.3488329909742,
            "full": 5330.273834057152
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 225.95474997069687,
            "full": 5152.777541079558
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
    "/content/suite-vulkan-0.3.2/teaching_reflectance70/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2803.247750038281,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10581.924041965976,
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
        "identifier": "teaching_reflectance70_grid",
        "full_identifier": "teaching_reflectance70_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.023782393569865962,
            "cvrmse_percent": 1.8290363870868471,
            "rms_normalized_rmse_percent": 0.4286464035961141,
            "reference_energy": 8.950874704563375,
            "candidate_energy": 8.94874597231319,
            "relative_energy_error_percent": 0.023782393569865966,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.1059455573558807e-07,
              "p99": 8.547503966838121e-06,
              "maximum": 5.949428305029869e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052888810634613,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -2.073158646707601,
            "cvrmse_percent": 40.74666692766661,
            "rms_normalized_rmse_percent": 2.6655577295325084,
            "reference_energy": 11.934677725472254,
            "candidate_energy": 11.68725292224994,
            "relative_energy_error_percent": 2.073158646707601,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.196967858163589e-07,
              "p90": 2.5396880300831984e-05,
              "p95": 3.763509448617697e-05,
              "p99": 7.159588858485222e-05,
              "maximum": 0.003156319260597229
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07841566205024719,
              "candidate": 0.07525934278964996,
              "position": [
                1.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.1948620287084892,
            "cvrmse_percent": 23.278562016791476,
            "rms_normalized_rmse_percent": 2.664939926061735,
            "reference_energy": 20.88555243003563,
            "candidate_energy": 20.63599889456313,
            "relative_energy_error_percent": 1.194862028708498,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.194818892713556e-07,
              "p90": 2.5202718097716778e-05,
              "p95": 3.756815567612648e-05,
              "p99": 7.127707067411393e-05,
              "maximum": 0.003156319260597229
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07841566205024719,
              "candidate": 0.07525934278964996,
              "position": [
                1.5,
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
        "identifier": "teaching_reflectance70_grid",
        "full_identifier": "teaching_reflectance70_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.023782393569865962,
            "cvrmse_percent": 1.8290363870868471,
            "rms_normalized_rmse_percent": 0.4286464035961141,
            "reference_energy": 8.950874704563375,
            "candidate_energy": 8.94874597231319,
            "relative_energy_error_percent": 0.023782393569865966,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.1059455573558807e-07,
              "p99": 8.547503966838121e-06,
              "maximum": 5.949428305029869e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052888810634613,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 167.0291923057146,
            "cvrmse_percent": 1855.988686045313,
            "rms_normalized_rmse_percent": 79.38696176297664,
            "reference_energy": 4.376769753649075,
            "candidate_energy": 11.68725292224994,
            "relative_energy_error_percent": 167.0291923057146,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002225536973128332,
              "p95": 0.0002875881300496985,
              "p99": 0.000417979434132576,
              "maximum": 0.03479411266744137
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025910725817084312,
              "candidate": 0.06070483848452568,
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
            "nmbe_percent": 54.83605493277768,
            "cvrmse_percent": 609.4985833847683,
            "rms_normalized_rmse_percent": 79.38642692493798,
            "reference_energy": 13.32764445821245,
            "candidate_energy": 20.63599889456313,
            "relative_energy_error_percent": 54.83605493277768,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022210095921764157,
              "p95": 0.00028698204368993174,
              "p99": 0.00041911681182682514,
              "maximum": 0.03479411266744137
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025910725817084312,
              "candidate": 0.06070483848452568,
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
      "bias_percent": -0.46576157848423033,
      "rms_normalized_error_percent": 0.39946420312589365,
      "absolute_error": {
        "p95": 0.19550927838984755,
        "p99": 0.2382942388780756,
        "maximum": 0.2593990120683909
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 22.515436810004925,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.39946420312589365
    },
    "overcast": {
      "bias_percent": -0.4582312680480446,
      "rms_normalized_error_percent": 0.3530541281935759,
      "absolute_error": {
        "p95": 0.11829853057861328,
        "p99": 0.1389632701873779,
        "maximum": 0.14690303802490234
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 14.202991485595703,
      "reference_fraction_of_uniform": 0.6308112740516663,
      "rms_normalized_to_uniform_percent": 0.24281833761577734
    },
    "horizon": {
      "bias_percent": -0.6141970247862945,
      "rms_normalized_error_percent": 1.5287745636740082,
      "absolute_error": {
        "p95": 0.09954977040440605,
        "p99": 0.10868554796520224,
        "maximum": 0.10953004774993547
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.24873547731746,
      "reference_fraction_of_uniform": 0.14428924940394036,
      "rms_normalized_to_uniform_percent": 0.1620368997952188
    },
    "north": {
      "bias_percent": -69.90858998769711,
      "rms_normalized_error_percent": 85.41015037908043,
      "absolute_error": {
        "p95": 8.526317833457142e-05,
        "p99": 0.00015005277336967984,
        "maximum": 0.00016934783343458548
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 3.01122654491337e-05,
      "reference_fraction_of_uniform": 1.3374053651205031e-06,
      "rms_normalized_to_uniform_percent": 0.00013830572101025123
    },
    "east": {
      "bias_percent": -0.577802423459288,
      "rms_normalized_error_percent": 0.5021074269702497,
      "absolute_error": {
        "p95": 0.05219903588294983,
        "p99": 0.08689626455307002,
        "maximum": 0.09944987297058105
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.304692268371582,
      "reference_fraction_of_uniform": 0.1911884844303131,
      "rms_normalized_to_uniform_percent": 0.10713244519512749
    },
    "south": {
      "bias_percent": -0.42351954531333924,
      "rms_normalized_error_percent": 0.4300377715953151,
      "absolute_error": {
        "p95": 0.1467726230621338,
        "p99": 0.17141788005828854,
        "maximum": 0.18409490585327148
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.741655349731445,
      "reference_fraction_of_uniform": 0.699149489402771,
      "rms_normalized_to_uniform_percent": 0.2813411677364259
    },
    "west": {
      "bias_percent": -0.4006492549104199,
      "rms_normalized_error_percent": 0.3665202463697562,
      "absolute_error": {
        "p95": 0.04466548562049866,
        "p99": 0.05051103830337524,
        "maximum": 0.05128884315490723
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.353138446807861,
      "reference_fraction_of_uniform": 0.19334018230438232,
      "rms_normalized_to_uniform_percent": 0.07887218151339431
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
        "identifier": "teaching_reflectance70_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.5041816011095702,
          "cvrmse_percent": 1.9591710562436782,
          "absolute_error_percentiles_lux": {
            "p50": 7.04364013671875,
            "p90": 60.56148071289064,
            "p95": 87.80078735351563,
            "p99": 154.8793945312496
          },
          "maximum_absolute_error_lux": 453.5859375,
          "worst": {
            "sensor_index": 29,
            "position": [
              4.5,
              0.5,
              0.75
            ],
            "hour_of_year": 2725.5,
            "foton_lux": 38610.609375,
            "radiance_lux": 39064.1953125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.13192541856925524,
            "maximum_error_percentage_points": 0.38219178082191263,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.0743577948480202,
            "maximum_error_percentage_points": 0.1672407135897629,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.06567732115677306,
            "maximum_error_percentage_points": 0.35657534246575295,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.15384322678843215,
            "maximum_error_percentage_points": 0.38013698630136616,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.14218036529680383,
            "maximum_error_percentage_points": 0.41178082191780874,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.004911708047941943,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
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
      "study_preparation_seconds": 0.39487075199986066,
      "weather_seconds": 0.2390008699999271,
      "metric_reduction_seconds": 1.0001999810001507,
      "write_seconds": 0.011713368999608065,
      "total_seconds": 1.251240820000021,
      "cold_end_to_end_seconds": 1.6461115719998816,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.001441961999717023,
      "engine_upload_seconds": 0.044619016,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.033005419,
      "engine_annual_reduction_seconds": 0.019133377,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.033005419
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.39487075199986066,
      "weather_seconds": 0.24868062399991686,
      "metric_reduction_seconds": 0.9587854870001138,
      "write_seconds": 0.016411191999850416,
      "total_seconds": 1.2241428899997118,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 1.2241428899997118,
      "raw_export_seconds": 0.0017589620001672301,
      "engine_upload_seconds": 0.046062598,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 4.3e-08,
      "engine_annual_reduction_seconds": 0.017738298,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.019100319999779458,
      "full": 0.051381892999870615
    }
  },
  "elapsed_seconds": 5.697079772000052,
  "result_class": "passed"
}
```
