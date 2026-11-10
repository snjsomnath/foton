# Foton report

Status: **passed**

```json
{
  "scene": "low_transmittance",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "low_transmittance",
    "category": "materials",
    "question": "Does low-transmittance glass attenuate light without turning opaque?",
    "interactions": [
      "glazing_attenuation"
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
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "caac92cf1cdd3445b0d027461a8e13f5b4220bb94f8401e2c986f430600f7d20",
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 13137537828487568414,
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
      "solver_version": "0.3.7",
      "scene_fingerprint": 13137537828487568414,
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
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/rcalc",
      "-e",
      "MF:2",
      "-f",
      "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/lib/reinhart.cal",
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
      "gendaymtx": "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/gendaymtx",
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
    "model_sha256": "be5131aca161898e7aec5d894595ac294d20221c42adb5b2f90f827262a09658",
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
          "maximum": 3.515087882988155e-05,
          "p95": 1.0477378964424133e-08,
          "p99": 2.097252945532091e-06
        },
        "bias_percent": -0.022820322745299697,
        "identifier": "low_transmittance_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7097819662012287,
        "worst_index": [
          22,
          407,
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
          "maximum": 0.00025138258934020996,
          "p95": 6.443216989282519e-06,
          "p99": 3.0062918085604906e-05
        },
        "bias_percent": 0.08239566984079057,
        "identifier": "low_transmittance_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.8993997793645374,
        "worst_index": [
          21,
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
          "maximum": 0.00013589300215244293,
          "p95": 5.370922735892236e-06,
          "p99": 2.641818718984723e-05
        },
        "bias_percent": -0.01898155442335028,
        "identifier": "low_transmittance_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.5619395153422513,
        "worst_index": [
          21,
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
            "identifier": "low_transmittance_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00011870110029121861,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.474496331065893e-06,
                  "p99": 4.5817141653969884e-05
                },
                "candidate_energy": 1.7394459193239982,
                "cvrmse_percent": 31.120952066410638,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.11134563651414978,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7413848753976708,
                "relative_energy_error_percent": 0.11134563651414979,
                "rms_normalized_rmse_percent": 6.064917966994511,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0002657669028849341,
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "reference": 0.0003844680031761527,
                  "rgb_channel": 0,
                  "sky_patch_index": 87
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00023281799803953618,
                  "p50": 0.0,
                  "p90": 1.4288604575085681e-06,
                  "p95": 1.3428703823592514e-05,
                  "p99": 7.933448068797588e-05
                },
                "candidate_energy": 0.6079687696988572,
                "cvrmse_percent": 151.97437303286898,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.8571189663469313,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 0.6028020390922713,
                "relative_energy_error_percent": 0.8571189663469314,
                "rms_normalized_rmse_percent": 5.770980593676265,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -7.721238944213837e-05,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.0001556056085973978,
                  "rgb_channel": 0,
                  "sky_patch_index": 151
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 113.22066700085998,
            "full": 232.78470896184444
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.49716698471457,
            "full": 238.23629203252494
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.51645800378174,
            "full": 225.43183306697756
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.9861250044778,
            "full": 230.01479101367295
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
            "identifier": "low_transmittance_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0001151012402260676,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.359943654388189e-06,
                  "p99": 4.598800296662375e-05
                },
                "candidate_energy": 1.7371640149962104,
                "cvrmse_percent": 28.037585269202598,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.021278402988276376,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.737533734426279,
                "relative_energy_error_percent": 0.021278402988276376,
                "rms_normalized_rmse_percent": 5.4693126489608845,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0004821983020519838,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0005972995422780514,
                  "rgb_channel": 0,
                  "sky_patch_index": 151
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00020038103684782982,
                  "p50": 0.0,
                  "p90": 3.8803563256806376e-06,
                  "p95": 1.1243566405028105e-05,
                  "p99": 6.15036697126925e-05
                },
                "candidate_energy": 1.1129068633712507,
                "cvrmse_percent": 65.51710111009722,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.1097789795960131,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1116864653133227,
                "relative_energy_error_percent": 0.10977897959601308,
                "rms_normalized_rmse_percent": 3.5440330643375795,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.009754790924489498,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.009554409887641668,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.61866703722626,
            "full": 2229.4746671104804
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.7350420532748,
            "full": 2247.0751659711823
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.10075001697987,
            "full": 2247.09662492387
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.50249991286546,
            "full": 2247.9925830848515
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
            "identifier": "low_transmittance_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 9.243565727956593e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.819871487095952e-06,
                  "p99": 3.824000305030495e-05
                },
                "candidate_energy": 1.7386554035350628,
                "cvrmse_percent": 25.179091349814097,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.0032547567066964402,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.73871199438031,
                "relative_energy_error_percent": 0.0032547567066964402,
                "rms_normalized_rmse_percent": 4.91054833857372,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0006634976889472455,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.0007559333462268114,
                  "rgb_channel": 0,
                  "sky_patch_index": 215
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0002097755204886198,
                  "p50": 0.0,
                  "p90": 3.7590103602269686e-06,
                  "p95": 1.040817005559802e-05,
                  "p99": 5.701917689293623e-05
                },
                "candidate_energy": 1.1126395184204974,
                "cvrmse_percent": 60.601519440048406,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.12034655237093195,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1139801551312942,
                "relative_energy_error_percent": 0.12034655237093195,
                "rms_normalized_rmse_percent": 3.28053100497753,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.006731970002874732,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.006522194482386112,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 149.05837504193187,
            "full": 2372.9592909803614
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.17549998871982,
            "full": 2410.993790952489
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.41058297920972,
            "full": 2402.667584014125
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 144.10816598683596,
            "full": 2399.196083075367
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
            "identifier": "low_transmittance_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 5.6435790611431e-05,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.36606171913445e-06,
                  "p99": 2.2390740923583508e-05
                },
                "candidate_energy": 1.7386989505329211,
                "cvrmse_percent": 13.739787258364,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.01042434837146576,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.7385177213891438,
                "relative_energy_error_percent": 0.01042434837146576,
                "rms_normalized_rmse_percent": 2.6800659412188996,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0005124670860823244,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.0005689028766937554,
                  "rgb_channel": 0,
                  "sky_patch_index": 153
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.000128462677821517,
                  "p50": 0.0,
                  "p90": 2.712777154556536e-06,
                  "p95": 6.657321137026884e-06,
                  "p99": 3.311566251795739e-05
                },
                "candidate_energy": 1.1130121924379246,
                "cvrmse_percent": 34.698011862228846,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.030259856396213463,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.1126754984299438,
                "relative_energy_error_percent": 0.030259856396213466,
                "rms_normalized_rmse_percent": 1.8765723245060146,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.005417332518845797,
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "reference": 0.005545795196667314,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 215.16883291769773,
            "full": 4239.2924999585375
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 202.87095790263265,
            "full": 4156.298166955821
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 211.88745799008757,
            "full": 4139.627458062023
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 226.46533302031457,
            "full": 4223.465125076473
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
    "/content/radiance-5.4.b268408ad5-Linux/usr/local/radiance/bin/oconv",
    "/content/suite-vulkan-0.3.7/low_transmittance/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2618.3829170186073,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/low_transmittance/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 10735.722290934063,
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
        "identifier": "low_transmittance_grid",
        "full_identifier": "low_transmittance_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.024893110230215728,
            "cvrmse_percent": 2.063141183236931,
            "rms_normalized_rmse_percent": 0.4026575002597515,
            "reference_energy": 1.7389257586189615,
            "candidate_energy": 1.7384928859130468,
            "relative_energy_error_percent": 0.024893110230215724,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.2223608791828156e-08,
              "p99": 1.8527935026213527e-06,
              "maximum": 1.692396472208202e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 407,
              "rgb_channel": 0,
              "reference": 0.0002574886893853545,
              "candidate": 0.00027441265410743654,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1559715647384028,
            "cvrmse_percent": 46.2757760508553,
            "rms_normalized_rmse_percent": 2.500874419937451,
            "reference_energy": 1.1125264182187706,
            "candidate_energy": 1.099665929173959,
            "relative_energy_error_percent": 1.1559715647384028,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.1438992664334405e-06,
              "p95": 5.123700248077512e-06,
              "p99": 1.4648780052084476e-05,
              "maximum": 0.0003559477627277374
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009283257648348808,
              "candidate": 0.00892730988562107,
              "position": [
                2.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.4661962020162174,
            "cvrmse_percent": 18.04071990368155,
            "rms_normalized_rmse_percent": 2.498893786438786,
            "reference_energy": 2.851452176837732,
            "candidate_energy": 2.838158815087006,
            "relative_energy_error_percent": 0.4661962020162174,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.1427488238478005e-06,
              "p95": 5.063817297923379e-06,
              "p99": 1.4541670680046082e-05,
              "maximum": 0.0003559477627277374
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009283257648348808,
              "candidate": 0.00892730988562107,
              "position": [
                2.5,
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
        "identifier": "low_transmittance_grid",
        "full_identifier": "low_transmittance_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.024893110230215728,
            "cvrmse_percent": 2.063141183236931,
            "rms_normalized_rmse_percent": 0.4026575002597515,
            "reference_energy": 1.7389257586189615,
            "candidate_energy": 1.7384928859130468,
            "relative_energy_error_percent": 0.024893110230215724,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.2223608791828156e-08,
              "p99": 1.8527935026213527e-06,
              "maximum": 1.692396472208202e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 407,
              "rgb_channel": 0,
              "reference": 0.0002574886893853545,
              "candidate": 0.00027441265410743654,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.20137454086405,
            "cvrmse_percent": 852.9860951497245,
            "rms_normalized_rmse_percent": 32.54205286044449,
            "reference_energy": 0.6068750482496839,
            "candidate_energy": 1.099665929173959,
            "relative_energy_error_percent": 81.20137454086404,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.69869997989736e-05,
              "p95": 2.390999907220248e-05,
              "p99": 5.2677394705824554e-05,
              "maximum": 0.0022645345889031887
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0034285355359315872,
              "candidate": 0.005693070124834776,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 20.988909492089295,
            "cvrmse_percent": 220.66825159444159,
            "rms_normalized_rmse_percent": 32.54128497306253,
            "reference_energy": 2.3458008068686453,
            "candidate_energy": 2.838158815087006,
            "relative_energy_error_percent": 20.988909492089302,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.6963553844107105e-05,
              "p95": 2.390000008745119e-05,
              "p99": 5.334359593689442e-05,
              "maximum": 0.0022645345889031887
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0034285355359315872,
              "candidate": 0.005693070124834776,
              "position": [
                2.5,
                5.5,
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
      "bias_percent": 0.17025961544815116,
      "rms_normalized_error_percent": 0.22019116485451204,
      "absolute_error": {
        "p95": 0.026614262329052063,
        "p99": 0.03947546676845198,
        "maximum": 0.04494381834218286
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.482043090676586,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.22019116485451204
    },
    "overcast": {
      "bias_percent": 0.10846939070361833,
      "rms_normalized_error_percent": 0.1492883897022376,
      "absolute_error": {
        "p95": 0.01272381842136383,
        "p99": 0.0179289162158966,
        "maximum": 0.020084798336029053
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.198194980621338,
      "reference_fraction_of_uniform": 0.6312946081161499,
      "rms_normalized_to_uniform_percent": 0.10464799494954272
    },
    "horizon": {
      "bias_percent": 1.1485644212584019,
      "rms_normalized_error_percent": 1.957830238953785,
      "absolute_error": {
        "p95": 0.019473177028435026,
        "p99": 0.026793018221710613,
        "maximum": 0.02859027385715568
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4438751458684904,
      "reference_fraction_of_uniform": 0.12747548904750697,
      "rms_normalized_to_uniform_percent": 0.15038502878324694
    },
    "north": {
      "bias_percent": -78.73674932746934,
      "rms_normalized_error_percent": 100.75206722995691,
      "absolute_error": {
        "p95": 1.3921332083555171e-05,
        "p99": 3.400643681743528e-05,
        "maximum": 4.249349149176851e-05
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.6646537207852816e-06,
      "reference_fraction_of_uniform": 7.652558338122617e-07,
      "rms_normalized_to_uniform_percent": 0.0001344430634961794
    },
    "east": {
      "bias_percent": 0.033914947541371976,
      "rms_normalized_error_percent": 0.22556036276922548,
      "absolute_error": {
        "p95": 0.005190424621105194,
        "p99": 0.007684050500392909,
        "maximum": 0.008855879306793213
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6371594667434692,
      "reference_fraction_of_uniform": 0.1829843819141388,
      "rms_normalized_to_uniform_percent": 0.043792142825285714
    },
    "south": {
      "bias_percent": 0.23125110912555513,
      "rms_normalized_error_percent": 0.30009387364232604,
      "absolute_error": {
        "p95": 0.026972874999046326,
        "p99": 0.036332991719245894,
        "maximum": 0.041173577308654785
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.487896680831909,
      "reference_fraction_of_uniform": 0.7144933938980103,
      "rms_normalized_to_uniform_percent": 0.2019805065159944
    },
    "west": {
      "bias_percent": 0.10689736966537816,
      "rms_normalized_error_percent": 0.19268819211548346,
      "absolute_error": {
        "p95": 0.005226351320743561,
        "p99": 0.00618370771408081,
        "maximum": 0.0063321590423583984
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.645766019821167,
      "reference_fraction_of_uniform": 0.1854560673236847,
      "rms_normalized_to_uniform_percent": 0.03775551465131068
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
        "identifier": "low_transmittance_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.03635860178078068,
          "cvrmse_percent": 1.8672985730986813,
          "absolute_error_percentiles_lux": {
            "p50": 0.68017578125,
            "p90": 7.412086486816406,
            "p95": 11.48934326171873,
            "p99": 23.646727294921856
          },
          "maximum_absolute_error_lux": 101.9578857421875,
          "worst": {
            "sensor_index": 18,
            "position": [
              3.5,
              5.5,
              0.75
            ],
            "hour_of_year": 8604.5,
            "foton_lux": 1608.443603515625,
            "radiance_lux": 1506.4857177734375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.15523972602739722,
            "maximum_error_percentage_points": 0.37972602739726025,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.18332992436346204,
            "maximum_error_percentage_points": 0.9046919764095662,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.3242770167427691,
            "maximum_error_percentage_points": 1.4556164383561594,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.3299162861491619,
            "maximum_error_percentage_points": 1.4556164383561594,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.013242009132420142,
            "maximum_error_percentage_points": 0.08616438356164391,
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
      "maximum_error_percentage_points": 0.00498140517979806,
      "metrics": {
        "da": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.00498140517979806,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.004383561643835632,
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
      "study_preparation_seconds": 0.3761825169999611,
      "weather_seconds": 0.25702585299995917,
      "metric_reduction_seconds": 0.30986495499996636,
      "write_seconds": 0.012172804000101678,
      "total_seconds": 0.5793846859999121,
      "cold_end_to_end_seconds": 0.9555672029998732,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0015422649998981797,
      "engine_upload_seconds": 0.065036008,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.029616472,
      "engine_annual_reduction_seconds": 0.007538213,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.029616472
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3761825169999611,
      "weather_seconds": 0.24592382700006965,
      "metric_reduction_seconds": 0.28358882199995605,
      "write_seconds": 0.011719769999899654,
      "total_seconds": 0.5414983150001262,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.5414983150001262,
      "raw_export_seconds": 0.0014815810000072815,
      "engine_upload_seconds": 0.063035367,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 3.8e-08,
      "engine_annual_reduction_seconds": 0.007307151,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02726077100010116,
      "full": 0.05537518400001318
    }
  },
  "elapsed_seconds": 4.997453456999892,
  "result_class": "passed"
}
```
