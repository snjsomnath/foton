# Foton report

Status: **passed**

```json
{
  "scene": "rooflit",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "rooflit",
    "category": "openings",
    "question": "How does a roof opening illuminate the workplane?",
    "interactions": [
      "roof_glazing",
      "zenith_sky"
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
    "aperture_area": 7.200000000000003
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "f351675e958fa96a8bbce384d20971da1be608d27340f921cbc9768bfb843a3b",
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
      "scene_fingerprint": 11178068536730648043,
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
      "solver_version": "0.3.3",
      "scene_fingerprint": 11178068536730648043,
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
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.3)",
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
    "model_sha256": "a39e81d7129668a92127cb23718f3f106a9f08857afb024976ec3e654e6ebf10",
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
          "maximum": 0.00034805084578692913,
          "p95": 6.2123872339725494e-06,
          "p99": 7.330439984798431e-05
        },
        "bias_percent": 0.005897273929929575,
        "identifier": "rooflit_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0832866682158737,
        "worst_index": [
          15,
          466,
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
          "maximum": 0.00030028633773326874,
          "p95": 5.943956784904003e-05,
          "p99": 0.00013447273522615433
        },
        "bias_percent": 0.08946561839884644,
        "identifier": "rooflit_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.9687944977564824,
        "worst_index": [
          10,
          393,
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
          "maximum": 0.00022835982963442802,
          "p95": 4.872120916843414e-05,
          "p99": 0.00010766321793198586
        },
        "bias_percent": -0.039428075088445216,
        "identifier": "rooflit_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.6063064605485735,
        "worst_index": [
          30,
          319,
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
            "identifier": "rooflit_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0008374601602554321,
                  "p50": 0.0,
                  "p90": 3.1297095119953156e-06,
                  "p95": 0.00017364788800477982,
                  "p99": 0.0004412163980305195
                },
                "candidate_energy": 25.53909231480793,
                "cvrmse_percent": 19.982494362600228,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.07696909407022402,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 25.519450225157925,
                "relative_energy_error_percent": 0.07696909407022402,
                "rms_normalized_rmse_percent": 5.976220734584212,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00604751193895936,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.005210051778703928,
                  "rgb_channel": 0,
                  "sky_patch_index": 516
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0014615163672715425,
                  "p50": 4.828850876492652e-06,
                  "p90": 6.499011069536227e-05,
                  "p95": 0.0002303055953234434,
                  "p99": 0.0005552589427679777
                },
                "candidate_energy": 1.8956668947225843,
                "cvrmse_percent": 359.6767479713478,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.5598146452882629,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.9063388588432097,
                "relative_energy_error_percent": 0.5598146452882629,
                "rms_normalized_rmse_percent": 7.893157408837004,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0008195552509278059,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": 0.0006419611163437366,
                  "rgb_channel": 0,
                  "sky_patch_index": 407
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 143.60391697846353,
            "full": 257.5342080090195
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.07345898728818,
            "full": 276.08945895917714
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.66287500504404,
            "full": 268.3454171055928
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.2421250147745,
            "full": 254.99087502248585
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
            "identifier": "rooflit_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003726851427927613,
                  "p50": 0.0,
                  "p90": 2.0922441035509133e-05,
                  "p95": 8.27619805932045e-05,
                  "p99": 0.00018408102914690971
                },
                "candidate_energy": 25.517907648358232,
                "cvrmse_percent": 8.926040058859925,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.07067117443574882,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 25.499886579033046,
                "relative_energy_error_percent": 0.07067117443574882,
                "rms_normalized_rmse_percent": 2.6700131370922278,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004138511139899492,
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "reference": 0.003765825997106731,
                  "rgb_channel": 0,
                  "sky_patch_index": 427
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000625931890681386,
                  "p50": 7.538398676842917e-06,
                  "p90": 4.117665812373171e-05,
                  "p95": 0.00011699739843606949,
                  "p99": 0.00027301954105496407
                },
                "candidate_energy": 5.842487846396526,
                "cvrmse_percent": 58.91873105334644,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.2043256528843869,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.854449989560486,
                "relative_energy_error_percent": 0.2043256528843869,
                "rms_normalized_rmse_percent": 3.8455471900010747,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0003000569995492697,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.0003258748911321163,
                  "rgb_channel": 0,
                  "sky_patch_index": 455
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 199.09241690766066,
            "full": 2563.615292077884
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.87216700427234,
            "full": 2560.0522089516744
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 183.7964579463005,
            "full": 2475.6916250335053
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.03466609865427,
            "full": 2514.323167037219
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
            "identifier": "rooflit_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0004114799667149782,
                  "p50": 0.0,
                  "p90": 2.1751914937340187e-05,
                  "p95": 7.917103357613087e-05,
                  "p99": 0.00018188294779974967
                },
                "candidate_energy": 25.505529005402423,
                "cvrmse_percent": 8.78840647661038,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.030667772901781003,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 25.51335338267745,
                "relative_energy_error_percent": 0.030667772901781003,
                "rms_normalized_rmse_percent": 2.6307111753057417,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.005051193060353398,
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "reference": 0.00463971309363842,
                  "rgb_channel": 0,
                  "sky_patch_index": 499
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005624799523502588,
                  "p50": 7.530301900260383e-06,
                  "p90": 4.1521158709656465e-05,
                  "p95": 0.0001096170162782073,
                  "p99": 0.00026009115390479565
                },
                "candidate_energy": 5.877135893808376,
                "cvrmse_percent": 55.6675094694877,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.03938904007414413,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.874821857872494,
                "relative_energy_error_percent": 0.03938904007414413,
                "rms_normalized_rmse_percent": 3.643456850739984,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00027630850672721863,
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "reference": 0.0008387884590774775,
                  "rgb_channel": 0,
                  "sky_patch_index": 360
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 187.71854089573026,
            "full": 2576.3426249613985
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 193.20362503640354,
            "full": 2596.860417048447
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 181.28620903007686,
            "full": 2602.3330830503255
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 253.6617920268327,
            "full": 2579.0215840097517
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
            "identifier": "rooflit_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001997369108721614,
                  "p50": 0.0,
                  "p90": 1.1021038517355919e-05,
                  "p95": 4.5676715672016144e-05,
                  "p99": 0.00010486016981303692
                },
                "candidate_energy": 25.511334052060192,
                "cvrmse_percent": 5.129692438627586,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.01655637459421,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 25.507110999215,
                "relative_energy_error_percent": 0.016556374594210003,
                "rms_normalized_rmse_percent": 1.5354896974142909,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0029257115675136447,
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "reference": 0.003125448478385806,
                  "rgb_channel": 0,
                  "sky_patch_index": 575
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002971041831187904,
                  "p50": 5.408353899838403e-06,
                  "p90": 2.6773097306431744e-05,
                  "p95": 6.407999899238348e-05,
                  "p99": 0.00014912011101841927
                },
                "candidate_energy": 5.862577524699201,
                "cvrmse_percent": 32.893473583152016,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.04246408342132537,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.865068072098055,
                "relative_energy_error_percent": 0.04246408342132538,
                "rms_normalized_rmse_percent": 2.151105201538199,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00012131110997870564,
                  "global_sensor_index": 2,
                  "local_sensor_index": 2,
                  "reference": 0.00041841529309749603,
                  "rgb_channel": 0,
                  "sky_patch_index": 511
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 298.99016593117267,
            "full": 4562.301041092724
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 297.1316670300439,
            "full": 4617.557541001588
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 298.4266249695793,
            "full": 4467.805707943626
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 283.8357500731945,
            "full": 4536.926375003532
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
    "/Users/ssanjay/GitHub/foton-0.3.3/validation/results/2026-11-04-architectural-v4-metal-0.3.3-release/rooflit/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 3072.2521250136197,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/rooflit/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 11888.783250004053,
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
        "identifier": "rooflit_grid",
        "full_identifier": "rooflit_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0058711399857663445,
            "cvrmse_percent": 1.7582093959146423,
            "rms_normalized_rmse_percent": 0.5263511955886843,
            "reference_energy": 25.51203091638422,
            "candidate_energy": 25.510533069335906,
            "relative_energy_error_percent": 0.0058711399857663445,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.0954757928848267e-09,
              "p95": 3.605615347623825e-06,
              "p99": 3.9703172660665587e-05,
              "maximum": 0.00012203119695186615
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 476,
              "rgb_channel": 0,
              "reference": 0.004308632574975491,
              "candidate": 0.004186601378023624,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.29140442287193263,
            "cvrmse_percent": 18.42949493065848,
            "rms_normalized_rmse_percent": 1.2043634510557213,
            "reference_energy": 5.861014481093829,
            "candidate_energy": 5.878093736516901,
            "relative_energy_error_percent": 0.2914044228719327,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.6160027927253395e-06,
              "p90": 2.3954753851285213e-05,
              "p95": 3.560353070497513e-05,
              "p99": 6.883637979626656e-05,
              "maximum": 0.0001648981124162674
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 542,
              "rgb_channel": 0,
              "reference": 0.0003095280844718218,
              "candidate": 0.0001446299720555544,
              "position": [
                4.5,
                4.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.049664953393435914,
            "cvrmse_percent": 3.3647025430303303,
            "rms_normalized_rmse_percent": 1.1769952063070817,
            "reference_energy": 31.373045397478048,
            "candidate_energy": 31.388626805852805,
            "relative_energy_error_percent": 0.04966495339343026,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.618249244638719e-06,
              "p90": 2.3883884568931563e-05,
              "p95": 3.527291119098663e-05,
              "p99": 6.691087037324905e-05,
              "maximum": 0.000161017756909132
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 561,
              "rgb_channel": 0,
              "reference": 0.006509695202112198,
              "candidate": 0.006348677445203066,
              "position": [
                4.5,
                4.5,
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
        "identifier": "rooflit_grid",
        "full_identifier": "rooflit_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0058711399857663445,
            "cvrmse_percent": 1.7582093959146423,
            "rms_normalized_rmse_percent": 0.5263511955886843,
            "reference_energy": 25.51203091638422,
            "candidate_energy": 25.510533069335906,
            "relative_energy_error_percent": 0.0058711399857663445,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.0954757928848267e-09,
              "p95": 3.605615347623825e-06,
              "p99": 3.9703172660665587e-05,
              "maximum": 0.00012203119695186615
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 476,
              "rgb_channel": 0,
              "reference": 0.004308632574975491,
              "candidate": 0.004186601378023624,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 206.43109501897789,
            "cvrmse_percent": 295.01789308709783,
            "rms_normalized_rmse_percent": 6.515705518370321,
            "reference_energy": 1.9182432305549337,
            "candidate_energy": 5.878093736516901,
            "relative_energy_error_percent": 206.4310950189779,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.277827631289256e-05,
              "p90": 0.00014369358052590542,
              "p95": 0.00019041774794459343,
              "p99": 0.00029138545505702496,
              "maximum": 0.0006741941906511784
            },
            "worst": {
              "global_sensor_index": 1,
              "local_sensor_index": 1,
              "sky_patch_index": 479,
              "rgb_channel": 0,
              "reference": -0.0004743942990899086,
              "candidate": 0.00019979989156126976,
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
            "nmbe_percent": 14.430598242326909,
            "cvrmse_percent": 20.58950462030155,
            "rms_normalized_rmse_percent": 6.502576381783666,
            "reference_energy": 27.430274146939155,
            "candidate_energy": 31.388626805852805,
            "relative_energy_error_percent": 14.430598242326896,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.2794162002101075e-05,
              "p90": 0.00014429722090199005,
              "p95": 0.00019032558202525252,
              "p99": 0.00029268860816955566,
              "maximum": 0.0006727110594511032
            },
            "worst": {
              "global_sensor_index": 1,
              "local_sensor_index": 1,
              "sky_patch_index": 479,
              "rgb_channel": 0,
              "reference": 0.0035391729325056076,
              "candidate": 0.004211883991956711,
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
      "bias_percent": 0.04971746397663137,
      "rms_normalized_error_percent": 0.11807618180522451,
      "absolute_error": {
        "p95": 0.1382771859405203,
        "p99": 0.1487232164233882,
        "maximum": 0.14913903982611387
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 51.997891097935025,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.11807618180522451
    },
    "overcast": {
      "bias_percent": 0.036697395655539346,
      "rms_normalized_error_percent": 0.09638755754013474,
      "absolute_error": {
        "p95": 0.0986323356628418,
        "p99": 0.10608110427856444,
        "maximum": 0.10955047607421875
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 44.18210220336914,
      "reference_fraction_of_uniform": 0.8496902585029602,
      "rms_normalized_to_uniform_percent": 0.08420169701987107
    },
    "horizon": {
      "bias_percent": 1.063668911126611,
      "rms_normalized_error_percent": 5.690050551198925,
      "absolute_error": {
        "p95": 0.011783400095346397,
        "p99": 0.021099447560090412,
        "maximum": 0.02419996060850571
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.12642392708169242,
      "reference_fraction_of_uniform": 0.0024313279714283076,
      "rms_normalized_to_uniform_percent": 0.012676254364331221
    },
    "north": {
      "bias_percent": 0.03655809364992721,
      "rms_normalized_error_percent": 0.20351684333623155,
      "absolute_error": {
        "p95": 0.05183124542236328,
        "p99": 0.07143964767456054,
        "maximum": 0.07419204711914062
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.474392890930176,
      "reference_fraction_of_uniform": 0.18220725655555725,
      "rms_normalized_to_uniform_percent": 0.04513228391443529
    },
    "east": {
      "bias_percent": 0.0153449131818273,
      "rms_normalized_error_percent": 0.18369985727132498,
      "absolute_error": {
        "p95": 0.04736137390136719,
        "p99": 0.0707494735717773,
        "maximum": 0.08022499084472656
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.580970764160156,
      "reference_fraction_of_uniform": 0.184256911277771,
      "rms_normalized_to_uniform_percent": 0.041211242683923587
    },
    "south": {
      "bias_percent": 0.06493278697089537,
      "rms_normalized_error_percent": 0.20772493371093026,
      "absolute_error": {
        "p95": 0.051084280014038086,
        "p99": 0.08169107437133785,
        "maximum": 0.09304046630859375
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.444778442382812,
      "reference_fraction_of_uniform": 0.1816377192735672,
      "rms_normalized_to_uniform_percent": 0.04595562080291539
    },
    "west": {
      "bias_percent": 0.11533074840005088,
      "rms_normalized_error_percent": 0.2355065591269224,
      "absolute_error": {
        "p95": 0.05855727195739746,
        "p99": 0.08232626914978025,
        "maximum": 0.08878135681152344
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.5811128616333,
      "reference_fraction_of_uniform": 0.18425963819026947,
      "rms_normalized_to_uniform_percent": 0.052866431378618586
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
        "identifier": "rooflit_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.1332631328655267,
          "cvrmse_percent": 1.5901855469537252,
          "absolute_error_percentiles_lux": {
            "p50": 4.5794677734375,
            "p90": 40.950866699218764,
            "p95": 63.06453857421873,
            "p99": 145.9721874999991
          },
          "maximum_absolute_error_lux": 609.763671875,
          "worst": {
            "sensor_index": 1,
            "position": [
              0.5,
              4.5,
              0.75
            ],
            "hour_of_year": 2601.5,
            "foton_lux": 30575.6015625,
            "radiance_lux": 31185.365234375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.055041856925418936,
            "maximum_error_percentage_points": 0.26904109589041525,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.017373000889602648,
            "maximum_error_percentage_points": 0.07162455798282963,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.012728310502283118,
            "maximum_error_percentage_points": 0.08054794520547937,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07842846270928246,
            "maximum_error_percentage_points": 0.36013698630137014,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.07344748858447495,
            "maximum_error_percentage_points": 0.3597260273972598,
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
            "identifier": "rooflit_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "rooflit_grid",
            "maximum_error_percentage_points": 0.0048202054794472815,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "rooflit_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "rooflit_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "rooflit_grid",
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
      "study_preparation_seconds": 0.005886042024940252,
      "weather_seconds": 0.08333195897284895,
      "metric_reduction_seconds": 0.1250879579456523,
      "write_seconds": 0.00950225000269711,
      "total_seconds": 0.21804408298339695,
      "cold_end_to_end_seconds": 0.2239301250083372,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0013969580177217722,
      "engine_upload_seconds": 0.000852041,
      "engine_acceleration_structure_seconds": 0.00308675,
      "engine_tracing_seconds": 0.05183749983552843,
      "engine_annual_reduction_seconds": 0.0014783332590013742,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.05183749983552843
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.005886042024940252,
      "weather_seconds": 0.07878583297133446,
      "metric_reduction_seconds": 0.04595112497918308,
      "write_seconds": 0.042172959074378014,
      "total_seconds": 0.1671058750944212,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1671058750944212,
      "raw_export_seconds": 0.00751125009264797,
      "engine_upload_seconds": 6.0417e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0015023750020191073,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.012103417073376477,
      "full": 0.059510499937459826
    }
  },
  "elapsed_seconds": 1.3353094999911264,
  "result_class": "passed"
}
```
