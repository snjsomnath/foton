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
  "model_sha256": "b602ef53923f277cdfffe204e08df43f30e0cc3f96dde775d6c9138b843e98e4",
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
      "scene_fingerprint": 13137537828487568414,
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
      "scene_fingerprint": 13137537828487568414,
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
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/low_transmittance/mf2/oracle/scene.rad"
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
            "nmbe_percent": -0.024879539482594252,
            "cvrmse_percent": 2.063138792390137,
            "rms_normalized_rmse_percent": 0.4026570336448628,
            "reference_energy": 1.7389257586189615,
            "candidate_energy": 1.7384931218982729,
            "relative_energy_error_percent": 0.024879539482594252,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.2281816452741623e-08,
              "p99": 1.8527935026213527e-06,
              "maximum": 1.6924022929742932e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 407,
              "rgb_channel": 0,
              "reference": 0.0002574886893853545,
              "candidate": 0.00027441271231509745,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.155669360845878,
            "cvrmse_percent": 46.2736776939744,
            "rms_normalized_rmse_percent": 2.5007610187696003,
            "reference_energy": 1.1125264182187706,
            "candidate_energy": 1.0996692912721002,
            "relative_energy_error_percent": 1.155669360845878,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.1438992664334405e-06,
              "p95": 5.106983735458925e-06,
              "p99": 1.4648780052084476e-05,
              "maximum": 0.00035593751817941666
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009283257648348808,
              "candidate": 0.008927320130169392,
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
            "nmbe_percent": -0.46607001777239665,
            "cvrmse_percent": 18.03993429480004,
            "rms_normalized_rmse_percent": 2.498784968544431,
            "reference_energy": 2.851452176837732,
            "candidate_energy": 2.838162413170373,
            "relative_energy_error_percent": 0.4660700177723967,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.1427895692104402e-06,
              "p95": 5.063817297923379e-06,
              "p99": 1.4541437849402428e-05,
              "maximum": 0.00035593751817941666
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.009283257648348808,
              "candidate": 0.008927320130169392,
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
            "nmbe_percent": -0.024879539482594252,
            "cvrmse_percent": 2.063138792390137,
            "rms_normalized_rmse_percent": 0.4026570336448628,
            "reference_energy": 1.7389257586189615,
            "candidate_energy": 1.7384931218982729,
            "relative_energy_error_percent": 0.024879539482594252,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.2281816452741623e-08,
              "p99": 1.8527935026213527e-06,
              "maximum": 1.6924022929742932e-05
            },
            "worst": {
              "global_sensor_index": 16,
              "local_sensor_index": 16,
              "sky_patch_index": 407,
              "rgb_channel": 0,
              "reference": 0.0002574886893853545,
              "candidate": 0.00027441271231509745,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.20192854257344,
            "cvrmse_percent": 853.007091166864,
            "rms_normalized_rmse_percent": 32.54285387408762,
            "reference_energy": 0.6068750482496839,
            "candidate_energy": 1.0996692912721002,
            "relative_energy_error_percent": 81.20192854257344,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.697594680081244e-05,
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
            "nmbe_percent": 20.989062876100284,
            "cvrmse_percent": 220.67368959298702,
            "rms_normalized_rmse_percent": 32.542086898391936,
            "reference_energy": 2.3458008068686453,
            "candidate_energy": 2.838162413170373,
            "relative_energy_error_percent": 20.989062876100284,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.6960000721155666e-05,
              "p95": 2.390000008745119e-05,
              "p99": 5.33436395926401e-05,
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
      "bias_percent": 0.17019661900079702,
      "rms_normalized_error_percent": 0.22018539048674157,
      "absolute_error": {
        "p95": 0.026614329565268102,
        "p99": 0.03947552352037657,
        "maximum": 0.04494387760122054
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.482043090676586,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.22018539048674157
    },
    "overcast": {
      "bias_percent": 0.1084175731104489,
      "rms_normalized_error_percent": 0.14927357438508695,
      "absolute_error": {
        "p95": 0.012720957398414612,
        "p99": 0.0179289162158966,
        "maximum": 0.020084798336029053
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.198194742202759,
      "reference_fraction_of_uniform": 0.6312945485115051,
      "rms_normalized_to_uniform_percent": 0.10463760916738636
    },
    "horizon": {
      "bias_percent": 1.1488978362539968,
      "rms_normalized_error_percent": 1.9581969548775098,
      "absolute_error": {
        "p95": 0.019473196889980435,
        "p99": 0.02679303749717778,
        "maximum": 0.028590298602687858
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.4438751458684904,
      "reference_fraction_of_uniform": 0.12747548904750697,
      "rms_normalized_to_uniform_percent": 0.15041319699908473
    },
    "north": {
      "bias_percent": -78.73674964680205,
      "rms_normalized_error_percent": 100.75206720008741,
      "absolute_error": {
        "p95": 1.3921332538302522e-05,
        "p99": 3.400643745408157e-05,
        "maximum": 4.249349149176851e-05
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.664653948158957e-06,
      "reference_fraction_of_uniform": 7.652558906556806e-07,
      "rms_normalized_to_uniform_percent": 0.0001344430634961794
    },
    "east": {
      "bias_percent": 0.03407160713457601,
      "rms_normalized_error_percent": 0.22557782965068038,
      "absolute_error": {
        "p95": 0.005190394818782806,
        "p99": 0.007684110105037684,
        "maximum": 0.008855938911437988
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6371594667434692,
      "reference_fraction_of_uniform": 0.1829843819141388,
      "rms_normalized_to_uniform_percent": 0.04379553936070944
    },
    "south": {
      "bias_percent": 0.23120185528805998,
      "rms_normalized_error_percent": 0.300072231346262,
      "absolute_error": {
        "p95": 0.026973038911819458,
        "p99": 0.03633297085762022,
        "maximum": 0.041173577308654785
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4878969192504883,
      "reference_fraction_of_uniform": 0.714493453502655,
      "rms_normalized_to_uniform_percent": 0.20196595103463155
    },
    "west": {
      "bias_percent": 0.10650329648133028,
      "rms_normalized_error_percent": 0.19277067638125092,
      "absolute_error": {
        "p95": 0.00522632896900177,
        "p99": 0.006171929836273193,
        "maximum": 0.00631403923034668
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.645766019821167,
      "reference_fraction_of_uniform": 0.1854560673236847,
      "rms_normalized_to_uniform_percent": 0.03777167415902878
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
          "nmbe_percent": 0.03636156595156411,
          "cvrmse_percent": 1.8672922972895187,
          "absolute_error_percentiles_lux": {
            "p50": 0.6801881790161133,
            "p90": 7.4117355346679705,
            "p95": 11.489562988281236,
            "p99": 23.646463623046852
          },
          "maximum_absolute_error_lux": 101.9581298828125,
          "worst": {
            "sensor_index": 18,
            "position": [
              3.5,
              5.5,
              0.75
            ],
            "hour_of_year": 8604.5,
            "foton_lux": 1608.44384765625,
            "radiance_lux": 1506.4857177734375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.15607305936073018,
            "maximum_error_percentage_points": 0.37972602739726025,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.18360770214123986,
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
      "maximum_error_percentage_points": 0.004978060787678373,
      "metrics": {
        "da": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "low_transmittance_grid",
            "maximum_error_percentage_points": 0.004978060787678373,
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
      "study_preparation_seconds": 0.008082250016741455,
      "weather_seconds": 0.0869849999435246,
      "metric_reduction_seconds": 0.11708783300127834,
      "write_seconds": 0.018317666021175683,
      "total_seconds": 0.22254600003361702,
      "cold_end_to_end_seconds": 0.23062825005035847,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.00313874997664243,
      "engine_upload_seconds": 0.000901875,
      "engine_acceleration_structure_seconds": 0.003357125,
      "engine_tracing_seconds": 0.05224858329165727,
      "engine_annual_reduction_seconds": 0.002655874937772751,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.05224858329165727
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008082250016741455,
      "weather_seconds": 0.0795586669119075,
      "metric_reduction_seconds": 0.050891665974631906,
      "write_seconds": 0.025063249981030822,
      "total_seconds": 0.15599050000309944,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15599050000309944,
      "raw_export_seconds": 0.002395707997493446,
      "engine_upload_seconds": 5.0208e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0025636249920353293,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.020123291993513703,
      "full": 0.07572216598782688
    }
  },
  "elapsed_seconds": 1.3926471669692546,
  "result_class": "passed"
}
```
