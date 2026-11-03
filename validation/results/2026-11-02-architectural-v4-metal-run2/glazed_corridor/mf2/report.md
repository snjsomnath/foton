# Foton report

Status: **failed**

```json
{
  "scene": "glazed_corridor",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "glazed_corridor",
    "category": "connections",
    "question": "Does a glazed corridor feed an office and an adjoining meeting room?",
    "interactions": [
      "borrowed_light",
      "turning_light_path",
      "paired_apertures"
    ],
    "room_count": 3,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 3,
    "apertures": 5,
    "shades": 0,
    "sensors": 90,
    "floor_area": 90.0,
    "aperture_area": 20.699999999999996
  },
  "sky_density": 2,
  "status": "failed",
  "passed": false,
  "model_sha256": "8d515fa74e6c4fcfb91d0c61393c38040ee5c13adfcaf12af479c004eb335aa7",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 706269953697064074,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 706269953697064074,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": 0.02337873394768215,
        "rms_normalized_error_percent": 0.6002617852188632,
        "absolute_error": {
          "p95": 4.6589411795139313e-07,
          "p99": 3.271352034062147e-05,
          "maximum": 8.967035682871938e-05
        },
        "worst_index": [
          10,
          355,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": -0.053123394412030185,
        "rms_normalized_error_percent": 1.0204786029343236,
        "absolute_error": {
          "p95": 0.0,
          "p99": 1.9874132703989744e-06,
          "maximum": 3.489520167931914e-05
        },
        "worst_index": [
          17,
          215,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "bias_percent": -0.988769369831759,
        "rms_normalized_error_percent": 3.4742097341224922,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 7.67746678320691e-06
        },
        "worst_index": [
          12,
          98,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      256,
      1024
    ]
  },
  "depth_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": -0.03736871840894164,
        "rms_normalized_error_percent": 1.0734479795348209,
        "absolute_error": {
          "p95": 7.716205436736345e-05,
          "p99": 0.00014825980179011822,
          "maximum": 0.0009110644459724426
        },
        "worst_index": [
          1,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": 0.04577612169967921,
        "rms_normalized_error_percent": 2.7463155030965294,
        "absolute_error": {
          "p95": 5.273202987154946e-06,
          "p99": 3.4598750062286854e-05,
          "maximum": 0.00029428862035274506
        },
        "worst_index": [
          17,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "bias_percent": 0.7036115019533139,
        "rms_normalized_error_percent": 8.699995815307666,
        "absolute_error": {
          "p95": 7.198387095286307e-07,
          "p99": 2.007519697144744e-06,
          "maximum": 4.725949838757515e-05
        },
        "worst_index": [
          3,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": 0.09310694877653179,
        "rms_normalized_error_percent": 0.9020413828663786,
        "absolute_error": {
          "p95": 6.301375105977058e-05,
          "p99": 0.00011689565144479275,
          "maximum": 0.0006065294146537781
        },
        "worst_index": [
          1,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": -0.05039683190205709,
        "rms_normalized_error_percent": 2.264524611092791,
        "absolute_error": {
          "p95": 4.663021172746085e-06,
          "p99": 2.9528921004384756e-05,
          "maximum": 0.00015806080773472786
        },
        "worst_index": [
          29,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "bias_percent": 0.5236152142627452,
        "rms_normalized_error_percent": 6.64615045988119,
        "absolute_error": {
          "p95": 5.994556886435021e-07,
          "p99": 1.6763658550189575e-06,
          "maximum": 3.776141966227442e-05
        },
        "worst_index": [
          16,
          0,
          0
        ],
        "passed": true
      }
    ]
  },
  "oracle_levels": [
    {
      "samples": 20000,
      "material_bounces": 1,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": 0.002732404628933407,
                "cvrmse_percent": 23.370308664688768,
                "rms_normalized_rmse_percent": 8.240083592438104,
                "reference_energy": 11.020097189503076,
                "candidate_energy": 11.020398303148795,
                "relative_energy_error_percent": 0.0027324046289334066,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 9.660025534685701e-05,
                  "p95": 0.0002035844954662025,
                  "p99": 0.00037464092019945383,
                  "maximum": 0.0007395449792966247
                },
                "worst": {
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "sky_patch_index": 211,
                  "rgb_channel": 0,
                  "reference": 0.0019032889977097511,
                  "candidate": 0.002642833977006376
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.3295504326221821,
                "cvrmse_percent": 93.94980812045813,
                "rms_normalized_rmse_percent": 4.204368232204126,
                "reference_energy": 3.3392960402964995,
                "candidate_energy": 3.328291375749167,
                "relative_energy_error_percent": 0.3295504326221821,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0001330318336840719,
                  "p95": 0.0002487215679138899,
                  "p99": 0.0004603894194588065,
                  "maximum": 0.0011512599885463715
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04631415940821171,
                  "candidate": 0.04516289941966534
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "start_sensor_index": 18,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.31839662121286116,
                "cvrmse_percent": 150.64748797911943,
                "rms_normalized_rmse_percent": 18.311455306117608,
                "reference_energy": 0.6260562788529569,
                "candidate_energy": 0.6240629368141981,
                "relative_energy_error_percent": 0.31839662121286116,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.06605694378959e-05,
                  "maximum": 0.00033284009259659797
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 88,
                  "rgb_channel": 0,
                  "reference": 0.0004171133477939293,
                  "candidate": 0.0007499534403905272
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.41121862836242234,
                "cvrmse_percent": 334.42919616940657,
                "rms_normalized_rmse_percent": 12.475047140354386,
                "reference_energy": 0.44076304330923577,
                "candidate_energy": 0.43895054356821106,
                "relative_energy_error_percent": 0.4112186283624224,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1771235196865746e-06,
                  "p99": 0.00011409258877392858,
                  "maximum": 0.0008161603473126888
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.011478370055556297,
                  "candidate": 0.010662209708243608
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -4.740897127566537,
                "cvrmse_percent": 1380.551763738593,
                "rms_normalized_rmse_percent": 34.23231123305062,
                "reference_energy": 0.004324519226429402,
                "candidate_energy": 0.004119498218642548,
                "relative_energy_error_percent": 4.740897127566537,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 8.285920375783462e-05
                },
                "worst": {
                  "global_sensor_index": 66,
                  "local_sensor_index": 12,
                  "sky_patch_index": 38,
                  "rgb_channel": 0,
                  "reference": 9.66671941569075e-05,
                  "candidate": 1.3807990399072878e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -4.960338811139285,
                "cvrmse_percent": 846.3048835151214,
                "rms_normalized_rmse_percent": 24.42391132201364,
                "reference_energy": 0.01150913693078337,
                "candidate_energy": 0.010938244744778558,
                "relative_energy_error_percent": 4.960338811139285,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 8.28257961984491e-05
                },
                "worst": {
                  "global_sensor_index": 66,
                  "local_sensor_index": 12,
                  "sky_patch_index": 38,
                  "rgb_channel": 0,
                  "reference": -1.6739832062739879e-06,
                  "candidate": 8.115181299217511e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 165.73408397380263,
            "full": 494.88825001753867
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 161.71691694762558,
            "full": 493.213374982588
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.42999999970198,
            "full": 482.4025420239195
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 163.84229203686118,
            "full": 500.9077920112759
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 8,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": -0.00298514431187713,
                "cvrmse_percent": 11.979510974386647,
                "rms_normalized_rmse_percent": 4.232122349995135,
                "reference_energy": 11.022532164754352,
                "candidate_energy": 11.022203126262411,
                "relative_energy_error_percent": 0.0029851443118771304,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.33214770257473e-05,
                  "p95": 0.00010718600242398679,
                  "p99": 0.00019788858480751514,
                  "maximum": 0.0003863009624183178
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 150,
                  "rgb_channel": 0,
                  "reference": 0.0016294484958052635,
                  "candidate": 0.0020157494582235813
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.0771154123098597,
                "cvrmse_percent": 34.447413693477586,
                "rms_normalized_rmse_percent": 1.9461123839800325,
                "reference_energy": 5.65047315539109,
                "candidate_energy": 5.646115769719852,
                "relative_energy_error_percent": 0.07711541230985972,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.393506974371576e-08,
                  "p90": 7.857315358705819e-05,
                  "p95": 0.00015097830328159034,
                  "p99": 0.0002872259356081486,
                  "maximum": 0.0007691644132137299
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.08292898163199425,
                  "candidate": 0.08369814604520798
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "start_sensor_index": 18,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.13719437156776523,
                "cvrmse_percent": 93.032018506504,
                "rms_normalized_rmse_percent": 11.41992923041928,
                "reference_energy": 0.625619056507503,
                "candidate_energy": 0.6264773706404867,
                "relative_energy_error_percent": 0.1371943715677652,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.198333772365004e-05,
                  "maximum": 0.00019609846640378237
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 8,
                  "sky_patch_index": 89,
                  "rgb_channel": 0,
                  "reference": 0.0005994224920868874,
                  "candidate": 0.0007955209584906697
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.19037213526189425,
                "cvrmse_percent": 98.49225334046258,
                "rms_normalized_rmse_percent": 5.372761593405904,
                "reference_energy": 0.9231133679049606,
                "candidate_energy": 0.9213560172755919,
                "relative_energy_error_percent": 0.19037213526189425,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.209688506762181e-06,
                  "p95": 8.050474662013585e-06,
                  "p99": 7.274993549799547e-05,
                  "maximum": 0.00037476373836398125
                },
                "worst": {
                  "global_sensor_index": 31,
                  "local_sensor_index": 13,
                  "sky_patch_index": 90,
                  "rgb_channel": 0,
                  "reference": 0.00027264884556643665,
                  "candidate": -0.0001021148927975446
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 4.309193666891773,
                "cvrmse_percent": 998.977288136239,
                "rms_normalized_rmse_percent": 24.732886123947527,
                "reference_energy": 0.00413997980831482,
                "candidate_energy": 0.00431837955602532,
                "relative_energy_error_percent": 4.309193666891773,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.619164974428713e-05
                },
                "worst": {
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 0.0001709316493361257,
                  "candidate": 0.00021712329908041283
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.07562493182133923,
                "cvrmse_percent": 280.68570831561226,
                "rms_normalized_rmse_percent": 14.17583866851718,
                "reference_energy": 0.03178400312208751,
                "candidate_energy": 0.03175996649139634,
                "relative_energy_error_percent": 0.07562493182133923,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.486780020267605e-07,
                  "p95": 8.976000067661971e-07,
                  "p99": 2.877474351237197e-06,
                  "maximum": 8.604492177255452e-05
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.000744082877645269,
                  "candidate": 0.0006580379558727145
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 246.82933290023357,
            "full": 6685.558708035387
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 248.31129191443324,
            "full": 6775.447207968682
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 240.59679196216166,
            "full": 6866.706375032663
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 242.9673750884831,
            "full": 6742.9371669422835
          }
        }
      ]
    },
    {
      "samples": 40000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": -0.044649336386607036,
                "cvrmse_percent": 12.105071038446187,
                "rms_normalized_rmse_percent": 4.273541344288967,
                "reference_energy": 11.026973223896334,
                "candidate_energy": 11.022049753528336,
                "relative_energy_error_percent": 0.04464933638660704,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.997884389013052e-05,
                  "p95": 0.00010020844638347626,
                  "p99": 0.0002062841085717082,
                  "maximum": 0.0003608135157264769
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 217,
                  "rgb_channel": 0,
                  "reference": 0.002403856022283435,
                  "candidate": 0.002043042506556958
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.02256698073617748,
                "cvrmse_percent": 34.77263332687186,
                "rms_normalized_rmse_percent": 1.966202992911157,
                "reference_energy": 5.6392847679752975,
                "candidate_energy": 5.640557384282545,
                "relative_energy_error_percent": 0.02256698073617748,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.166292460501154e-08,
                  "p90": 7.721781730651855e-05,
                  "p95": 0.0001523527316749096,
                  "p99": 0.00028469995595514774,
                  "maximum": 0.0006570629775524139
                },
                "worst": {
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07810432091355324,
                  "candidate": 0.07744725793600082
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "start_sensor_index": 18,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.09307853746660426,
                "cvrmse_percent": 84.52827873728961,
                "rms_normalized_rmse_percent": 10.375024439178807,
                "reference_energy": 0.6261053746505922,
                "candidate_energy": 0.6266881443763168,
                "relative_energy_error_percent": 0.09307853746660427,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.17494447901845e-05,
                  "maximum": 0.00021013550576753914
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 8,
                  "sky_patch_index": 89,
                  "rgb_channel": 0,
                  "reference": 0.000739768089260906,
                  "candidate": 0.0005296325834933668
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.2993999227452393,
                "cvrmse_percent": 97.7882052296689,
                "rms_normalized_rmse_percent": 5.310499158536872,
                "reference_energy": 0.9212158254950715,
                "candidate_energy": 0.9239739449649207,
                "relative_energy_error_percent": 0.29939992274523936,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.184116858141359e-06,
                  "p95": 8.014520062715746e-06,
                  "p99": 7.017157622613013e-05,
                  "maximum": 0.00052647665143013
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 16,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.007666802033782005,
                  "candidate": 0.008193278685212135
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 5.390901754803201,
                "cvrmse_percent": 1059.200272030829,
                "rms_normalized_rmse_percent": 24.506621610321652,
                "reference_energy": 0.004098322040135827,
                "candidate_energy": 0.004319258554914995,
                "relative_energy_error_percent": 5.390901754803202,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.2516254072543234e-05
                },
                "worst": {
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 0.00018474824901204556,
                  "candidate": 0.0002372645030845888
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.1001676857125475,
                "cvrmse_percent": 216.59654007774864,
                "rms_normalized_rmse_percent": 10.637770705115301,
                "reference_energy": 0.03187036875048577,
                "candidate_energy": 0.03222099624879604,
                "relative_energy_error_percent": 1.1001676857125475,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.4451780095423654e-07,
                  "p95": 8.79603483383562e-07,
                  "p99": 2.8655394999077544e-06,
                  "maximum": 7.593655027449131e-05
                },
                "worst": {
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "sky_patch_index": 96,
                  "rgb_channel": 0,
                  "reference": 3.456130070844665e-05,
                  "candidate": -4.137524956604466e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 239.43574994336814,
            "full": 7098.714375053532
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 250.50300010479987,
            "full": 7145.601416938007
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 240.6203339342028,
            "full": 7129.635916906409
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 237.2508329572156,
            "full": 7116.419458063319
          }
        }
      ]
    },
    {
      "samples": 80000,
      "material_bounces": 12,
      "repeatability": {
        "schema_version": 1,
        "run_count": 4,
        "half_run_count": 2,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": 0.000622729821251249,
                "cvrmse_percent": 6.459886329539471,
                "rms_normalized_rmse_percent": 2.2824576946853017,
                "reference_energy": 11.025120011622562,
                "candidate_energy": 11.025188668332703,
                "relative_energy_error_percent": 0.0006227298212512489,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.979877172037959e-05,
                  "p95": 5.5014039389789104e-05,
                  "p99": 0.00010725019092205912,
                  "maximum": 0.0002291100681759417
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 150,
                  "rgb_channel": 0,
                  "reference": 0.0020079115638509393,
                  "candidate": 0.0017788014956749976
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.020919007408272156,
                "cvrmse_percent": 20.450911650926205,
                "rms_normalized_rmse_percent": 1.1565734074222318,
                "reference_energy": 5.655385488171522,
                "candidate_energy": 5.654202437662285,
                "relative_energy_error_percent": 0.02091900740827216,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 4.5162043534219265e-05,
                  "p95": 8.076830999925733e-05,
                  "p99": 0.00015962915495038033,
                  "maximum": 0.00068645179271698
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.08305169269442558,
                  "candidate": 0.08373814448714256
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "start_sensor_index": 18,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.20264051586939652,
                "cvrmse_percent": 49.313847515048295,
                "rms_normalized_rmse_percent": 6.077400680839544,
                "reference_energy": 0.6264084004039887,
                "candidate_energy": 0.6251390431899608,
                "relative_energy_error_percent": 0.2026405158693965,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 2.5342058506794274e-05,
                  "maximum": 0.00012171838898211718
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 26,
                  "sky_patch_index": 95,
                  "rgb_channel": 0,
                  "reference": 0.0005629207007586956,
                  "candidate": 0.0006846390897408128
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.008727331664882394,
                "cvrmse_percent": 57.72401164261734,
                "rms_normalized_rmse_percent": 3.1343154170748537,
                "reference_energy": 0.9224775455851209,
                "candidate_energy": 0.9223970379101836,
                "relative_energy_error_percent": 0.008727331664882394,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.9393831823654235e-06,
                  "p95": 5.392599632614292e-06,
                  "p99": 3.800370541284792e-05,
                  "maximum": 0.0003100251778960228
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.015658104792237282,
                  "candidate": 0.015968129970133305
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.19180248575506387,
                "cvrmse_percent": 724.245284073799,
                "rms_normalized_rmse_percent": 17.310928988799315,
                "reference_energy": 0.004364276816886559,
                "candidate_energy": 0.004372647608306579,
                "relative_energy_error_percent": 0.19180248575506387,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 2.7182502890354954e-05
                },
                "worst": {
                  "global_sensor_index": 60,
                  "local_sensor_index": 6,
                  "sky_patch_index": 37,
                  "rgb_channel": 0,
                  "reference": 6.146020132291596e-05,
                  "candidate": 8.864270421327092e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.3540664357613739,
                "cvrmse_percent": 216.00014832252242,
                "rms_normalized_rmse_percent": 10.781490375936086,
                "reference_energy": 0.0321327300958707,
                "candidate_energy": 0.03201895888370743,
                "relative_energy_error_percent": 0.3540664357613739,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.046548911811458e-07,
                  "p95": 7.062897111609345e-07,
                  "p99": 1.9753328501792566e-06,
                  "maximum": 0.00010343248140998185
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0006983221683185548,
                  "candidate": 0.0008017546497285366
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          }
        ]
      },
      "runs": [
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 414.1030419850722,
            "full": 12443.794124992564
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 406.5533339744434,
            "full": 12346.459291991778
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 405.1817499566823,
            "full": 12457.624832983129
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "90",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 396.9945840071887,
            "full": 12426.674583926797
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 15118.600375019014,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 59731.324665946886,
      "worker_pool_size": 12,
      "invocation_count": 6
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      90,
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
        "identifier": "glazed_corridor_corridor_grid",
        "full_identifier": "glazed_corridor_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 18,
        "stages": {
          "direct": {
            "nmbe_percent": -0.46142144161544796,
            "cvrmse_percent": 3.283675275246353,
            "rms_normalized_rmse_percent": 1.1633019529258022,
            "reference_energy": 11.02544060250679,
            "candidate_energy": 10.974566855534249,
            "relative_energy_error_percent": 0.46142144161544796,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.1918170861899853e-07,
              "p95": 6.418791599571705e-06,
              "p99": 6.387694884324446e-05,
              "maximum": 0.00013667577877640724
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 181,
              "rgb_channel": 0,
              "reference": 0.00013667577877640724,
              "candidate": 0.0,
              "position": [
                2.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.6797528791130802,
            "cvrmse_percent": 28.905313008737842,
            "rms_normalized_rmse_percent": 1.634376126892844,
            "reference_energy": 5.654507646715185,
            "candidate_energy": 5.616070968186969,
            "relative_energy_error_percent": 0.6797528791130802,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.0839470355203957e-07,
              "p90": 2.7973734177066945e-05,
              "p95": 5.112032522447407e-05,
              "p99": 0.00010280629066983238,
              "maximum": 0.0019925162196159363
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08339491486549377,
              "candidate": 0.08140239864587784,
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
            "nmbe_percent": -0.535435866864415,
            "cvrmse_percent": 9.569233845574292,
            "rms_normalized_rmse_percent": 1.5960680507711567,
            "reference_energy": 16.679948249221976,
            "candidate_energy": 16.590637823721217,
            "relative_energy_error_percent": 0.5354358668644258,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 9.012019219767353e-08,
              "p90": 2.3045577108860016e-05,
              "p95": 4.029308911412954e-05,
              "p99": 8.534104563295841e-05,
              "maximum": 0.0019925162196159363
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08339491486549377,
              "candidate": 0.08140239864587784,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "full_identifier": "glazed_corridor_office_grid",
        "start_sensor_index": 18,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0838132214777485,
            "cvrmse_percent": 7.243940256281459,
            "rms_normalized_rmse_percent": 0.8940165578980909,
            "reference_energy": 0.6264557174576453,
            "candidate_energy": 0.6259306647397125,
            "relative_energy_error_percent": 0.0838132214777485,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1505471775308251e-06,
              "maximum": 4.912434087600559e-05
            },
            "worst": {
              "global_sensor_index": 49,
              "local_sensor_index": 31,
              "sky_patch_index": 86,
              "rgb_channel": 0,
              "reference": 4.912434087600559e-05,
              "candidate": 0.0,
              "position": [
                5.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.19741058656591623,
            "cvrmse_percent": 42.01222024854372,
            "rms_normalized_rmse_percent": 2.2775505635576208,
            "reference_energy": 0.9217552845250463,
            "candidate_energy": 0.9235749270389295,
            "relative_energy_error_percent": 0.19741058656591623,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.1220392202158137e-06,
              "p95": 5.453275662148371e-06,
              "p99": 1.9290950149297714e-05,
              "maximum": 0.00031542684882879257
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005361683201044798,
              "candidate": 0.0056771100498735905,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.08361843406955084,
            "cvrmse_percent": 24.826637807387634,
            "rms_normalized_rmse_percent": 2.2606056851695056,
            "reference_energy": 1.5482110019826916,
            "candidate_energy": 1.549505591778642,
            "relative_energy_error_percent": 0.08361843406955084,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.096522232226575e-06,
              "p95": 5.361887815524824e-06,
              "p99": 1.8662074580788612e-05,
              "maximum": 0.00031542684882879257
            },
            "worst": {
              "global_sensor_index": 30,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.005361683201044798,
              "candidate": 0.0056771100498735905,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "full_identifier": "glazed_corridor_meeting_grid",
        "start_sensor_index": 54,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03640350793459441,
            "cvrmse_percent": 77.2188377553826,
            "rms_normalized_rmse_percent": 1.8444680473091102,
            "reference_energy": 0.004285219445932853,
            "candidate_energy": 0.004283659475731838,
            "relative_energy_error_percent": 0.036403507934594403,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.8080582928378135e-06
            },
            "worst": {
              "global_sensor_index": 66,
              "local_sensor_index": 12,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": 3.326051592011936e-05,
              "candidate": 3.8068574212957174e-05,
              "position": [
                8.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.7878564094236135,
            "cvrmse_percent": 124.95240531514138,
            "rms_normalized_rmse_percent": 6.18667805311383,
            "reference_energy": 0.032159087171512724,
            "candidate_energy": 0.031905719742019834,
            "relative_energy_error_percent": 0.7878564094236135,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.5455288180941354e-07,
              "p95": 7.067148430905945e-07,
              "p99": 1.8400000207918765e-06,
              "maximum": 3.632158041000366e-05
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007500384235754609,
              "candidate": 0.0007863600039854646,
              "position": [
                6.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6994985591847519,
            "cvrmse_percent": 110.70847318707825,
            "rms_normalized_rmse_percent": 6.211832492607312,
            "reference_energy": 0.03644430661744558,
            "candidate_energy": 0.03618937921775167,
            "relative_energy_error_percent": 0.6994985591847519,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.5415845598407753e-07,
              "p95": 7.057122957121464e-07,
              "p99": 1.8773873762256699e-06,
              "maximum": 3.632158041000366e-05
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007500384235754609,
              "candidate": 0.0007863600039854646,
              "position": [
                6.5,
                5.5,
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
      90,
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
        "identifier": "glazed_corridor_corridor_grid",
        "full_identifier": "glazed_corridor_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 18,
        "stages": {
          "direct": {
            "nmbe_percent": -0.46142144161544796,
            "cvrmse_percent": 3.283675275246353,
            "rms_normalized_rmse_percent": 1.1633019529258022,
            "reference_energy": 11.02544060250679,
            "candidate_energy": 10.974566855534249,
            "relative_energy_error_percent": 0.46142144161544796,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 3.1918170861899853e-07,
              "p95": 6.418791599571705e-06,
              "p99": 6.387694884324446e-05,
              "maximum": 0.00013667577877640724
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 181,
              "rgb_channel": 0,
              "reference": 0.00013667577877640724,
              "candidate": 0.0,
              "position": [
                2.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 68.72167162817514,
            "cvrmse_percent": 789.2014707812954,
            "rms_normalized_rmse_percent": 35.22520184152818,
            "reference_energy": 3.3286008335452806,
            "candidate_energy": 5.616070968186969,
            "relative_energy_error_percent": 68.72167162817516,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0631567306518264e-06,
              "p90": 0.00013944465899839997,
              "p95": 0.00019219187379349023,
              "p99": 0.00031454721465706825,
              "maximum": 0.02489650994539261
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04523153603076935,
              "candidate": 0.07012804597616196,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 15.581649235396798,
            "cvrmse_percent": 182.99188653562672,
            "rms_normalized_rmse_percent": 35.2216678159994,
            "reference_energy": 14.354041436052071,
            "candidate_energy": 16.590637823721217,
            "relative_energy_error_percent": 15.581649235396785,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00013904999650549144,
              "p95": 0.00019138927018502727,
              "p99": 0.00031468889210373163,
              "maximum": 0.02489650994539261
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04523153603076935,
              "candidate": 0.07012804597616196,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "full_identifier": "glazed_corridor_office_grid",
        "start_sensor_index": 18,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.0838132214777485,
            "cvrmse_percent": 7.243940256281459,
            "rms_normalized_rmse_percent": 0.8940165578980909,
            "reference_energy": 0.6264557174576453,
            "candidate_energy": 0.6259306647397125,
            "relative_energy_error_percent": 0.0838132214777485,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.1505471775308251e-06,
              "maximum": 4.912434087600559e-05
            },
            "worst": {
              "global_sensor_index": 49,
              "local_sensor_index": 31,
              "sky_patch_index": 86,
              "rgb_channel": 0,
              "reference": 4.912434087600559e-05,
              "candidate": 0.0,
              "position": [
                5.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 110.64030625454464,
            "cvrmse_percent": 1322.7221380526262,
            "rms_normalized_rmse_percent": 49.53985633498182,
            "reference_energy": 0.43846068374153013,
            "candidate_energy": 0.9235749270389295,
            "relative_energy_error_percent": 110.64030625454464,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2898372870040498e-05,
              "p95": 2.4670000129844993e-05,
              "p99": 6.419119017664343e-05,
              "maximum": 0.004656250588595867
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01107028964906931,
              "candidate": 0.015726540237665176,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 45.50490442571671,
            "cvrmse_percent": 544.5846186135401,
            "rms_normalized_rmse_percent": 49.53775836714604,
            "reference_energy": 1.0649164011991754,
            "candidate_energy": 1.549505591778642,
            "relative_energy_error_percent": 45.5049044257167,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2807274970327892e-05,
              "p95": 2.4630289772176184e-05,
              "p99": 6.472101085819304e-05,
              "maximum": 0.004656250588595867
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01107028964906931,
              "candidate": 0.015726540237665176,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "full_identifier": "glazed_corridor_meeting_grid",
        "start_sensor_index": 54,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.03640350793459441,
            "cvrmse_percent": 77.2188377553826,
            "rms_normalized_rmse_percent": 1.8444680473091102,
            "reference_energy": 0.004285219445932853,
            "candidate_energy": 0.004283659475731838,
            "relative_energy_error_percent": 0.036403507934594403,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 4.8080582928378135e-06
            },
            "worst": {
              "global_sensor_index": 66,
              "local_sensor_index": 12,
              "sky_patch_index": 98,
              "rgb_channel": 0,
              "reference": 3.326051592011936e-05,
              "candidate": 3.8068574212957174e-05,
              "position": [
                8.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 185.8812467496094,
            "cvrmse_percent": 2705.556715563409,
            "rms_normalized_rmse_percent": 78.38282904453676,
            "reference_energy": 0.011160480131096051,
            "candidate_energy": 0.031905719742019834,
            "relative_energy_error_percent": 185.8812467496094,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.0000000467443897e-07,
              "p95": 1.050000037139398e-06,
              "p99": 3.6402802834345493e-06,
              "maximum": 0.0003455498954281211
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0003902501193806529,
              "candidate": 0.000735800014808774,
              "position": [
                6.5,
                6.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 134.30068050509738,
            "cvrmse_percent": 1955.2797880495748,
            "rms_normalized_rmse_percent": 78.39672268290919,
            "reference_energy": 0.015445699577028904,
            "candidate_energy": 0.03618937921775167,
            "relative_energy_error_percent": 134.3006805050974,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.0000000467443897e-07,
              "p95": 1.050000037139398e-06,
              "p99": 3.6402802834345493e-06,
              "maximum": 0.0003455498954281211
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0003902501193806529,
              "candidate": 0.000735800014808774,
              "position": [
                6.5,
                6.5,
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
      "bias_percent": -0.23539153661694753,
      "rms_normalized_error_percent": 0.38028081483228265,
      "absolute_error": {
        "p95": 0.1697877556490869,
        "p99": 0.43275511797458754,
        "maximum": 0.48145538356379447
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.111837862801506,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.38028081483228265
    },
    "overcast": {
      "bias_percent": -0.20858010324593534,
      "rms_normalized_error_percent": 0.2769224942437927,
      "absolute_error": {
        "p95": 0.08825092315673819,
        "p99": 0.22447117805480954,
        "maximum": 0.2601356506347656
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.945282459259033,
      "reference_fraction_of_uniform": 0.6524789929389954,
      "rms_normalized_to_uniform_percent": 0.193311205075992
    },
    "horizon": {
      "bias_percent": 0.279670415401942,
      "rms_normalized_error_percent": 1.6330083342876125,
      "absolute_error": {
        "p95": 0.06548625194913646,
        "p99": 0.11386901470279415,
        "maximum": 0.1179113395289848
      },
      "worst_index": [
        0
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.9896404127654558,
      "reference_fraction_of_uniform": 0.10861040633806703,
      "rms_normalized_to_uniform_percent": 0.12422058946376865
    },
    "north": {
      "bias_percent": -86.28150578372151,
      "rms_normalized_error_percent": 97.95382531377544,
      "absolute_error": {
        "p95": 4.8724567022873e-05,
        "p99": 9.955579384495648e-05,
        "maximum": 0.00013045761033936287
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 9.041217708727345e-06,
      "reference_fraction_of_uniform": 9.92249624687247e-07,
      "rms_normalized_to_uniform_percent": 0.00010247924618204787
    },
    "east": {
      "bias_percent": -0.1922197527029618,
      "rms_normalized_error_percent": 0.24351766382222942,
      "absolute_error": {
        "p95": 0.021910905838012695,
        "p99": 0.04689723014831542,
        "maximum": 0.06609725952148438
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.7276909351348877,
      "reference_fraction_of_uniform": 0.18960949778556824,
      "rms_normalized_to_uniform_percent": 0.04994158333403805
    },
    "south": {
      "bias_percent": -0.2962484688238615,
      "rms_normalized_error_percent": 0.5467115760501029,
      "absolute_error": {
        "p95": 0.14926605224609368,
        "p99": 0.4047256278991699,
        "maximum": 0.42575645446777344
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.217997074127197,
      "reference_fraction_of_uniform": 0.6824086904525757,
      "rms_normalized_to_uniform_percent": 0.35173911508685873
    },
    "west": {
      "bias_percent": -0.2147091616635416,
      "rms_normalized_error_percent": 0.3464726230230526,
      "absolute_error": {
        "p95": 0.03714205026626583,
        "p99": 0.07701098918914795,
        "maximum": 0.08147764205932617
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.746583342552185,
      "reference_fraction_of_uniform": 0.19168289005756378,
      "rms_normalized_to_uniform_percent": 0.07159792384559406
    }
  },
  "annual": {
    "schema_version": 1,
    "oracle": "converged-coefficients",
    "passed": false,
    "occupied_hours": 3650,
    "structural": {
      "sun_up_hours_match": true,
      "grid_ids_match": true,
      "grid_counts_match": true
    },
    "grids": [
      {
        "identifier": "glazed_corridor_corridor_grid",
        "sensor_count": 18,
        "illuminance": {
          "nmbe_percent": -0.2823453267902455,
          "cvrmse_percent": 1.3685748327905731,
          "absolute_error_percentiles_lux": {
            "p50": 6.200103759765625,
            "p90": 57.176367187500034,
            "p95": 92.16079101562501,
            "p99": 211.01005371093765
          },
          "maximum_absolute_error_lux": 1058.392578125,
          "worst": {
            "sensor_index": 9,
            "position": [
              3.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1357.5,
            "foton_lux": 17552.35546875,
            "radiance_lux": 18610.748046875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.06565449010654431,
            "maximum_error_percentage_points": 0.2515068493150636,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.02391284633445581,
            "maximum_error_percentage_points": 0.10176327879565861,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.012823439878234706,
            "maximum_error_percentage_points": 0.051643835616438594,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.14881278538812814,
            "maximum_error_percentage_points": 0.2747945205479425,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.15091324200913211,
            "maximum_error_percentage_points": 0.32383561643835534,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 5.555555555555555,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.16503404420244056,
          "cvrmse_percent": 5.210063986727887,
          "absolute_error_percentiles_lux": {
            "p50": 0.7404441833496094,
            "p90": 7.700191497802734,
            "p95": 12.007150268554685,
            "p99": 26.70790817260742
          },
          "maximum_absolute_error_lux": 178.2733154296875,
          "worst": {
            "sensor_index": 9,
            "position": [
              1.5,
              5.5,
              0.75
            ],
            "hour_of_year": 1114.5,
            "foton_lux": 1962.830810546875,
            "radiance_lux": 1784.5574951171875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.12460045662100448,
            "maximum_error_percentage_points": 0.5783561643835622,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.30815831712360753,
            "maximum_error_percentage_points": 0.8892254197951104,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.8209170471841694,
            "maximum_error_percentage_points": 3.094246575342467,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.8168645357686455,
            "maximum_error_percentage_points": 3.0942465753424635,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0057838660578386596,
            "maximum_error_percentage_points": 0.056301369863013595,
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
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.4190068308841837,
          "cvrmse_percent": 32.14458321052884,
          "absolute_error_percentiles_lux": {
            "p50": 0.06595847010612488,
            "p90": 0.7852488517761234,
            "p95": 1.3280273139476775,
            "p99": 3.010603749752033
          },
          "maximum_absolute_error_lux": 13.996767044067383,
          "worst": {
            "sensor_index": 2,
            "position": [
              6.5,
              6.5,
              0.75
            ],
            "hour_of_year": 4931.5,
            "foton_lux": 34.49277877807617,
            "radiance_lux": 20.49601173400879
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.00014459665144596654,
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.02682429635787401,
            "maximum_error_percentage_points": 0.08135191741812231,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.003196347031963932,
            "maximum_error_percentage_points": 0.055342465753426495,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0031963470319634675,
            "maximum_error_percentage_points": 0.05534246575342461,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
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
    "numerical_correctness": "failed",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004984599074272289,
      "metrics": {
        "da": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004711579623275952,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004888698630132637,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.004984599074272289,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0035616438356164126,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004246575342467196,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.003561643835624295,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0,
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
      "study_preparation_seconds": 0.010730707901529968,
      "weather_seconds": 0.12860337493475527,
      "metric_reduction_seconds": 0.3020356670022011,
      "write_seconds": 0.06030829099472612,
      "total_seconds": 0.49114541697781533,
      "cold_end_to_end_seconds": 0.5018761248793453,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02774220798164606,
      "engine_upload_seconds": 0.000828625,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.24829695851076394,
      "engine_annual_reduction_seconds": 0.0034591249423101544,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.24829695851076394
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.010730707901529968,
      "weather_seconds": 0.11187499994412065,
      "metric_reduction_seconds": 0.04767949995584786,
      "write_seconds": 0.057960999896749854,
      "total_seconds": 0.2177030409220606,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2177030409220606,
      "raw_export_seconds": 0.026332916924729943,
      "engine_upload_seconds": 0.000109042,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0035706250928342342,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.014596749912016094,
      "full": 0.24268145894166082
    }
  },
  "elapsed_seconds": 189.8951361249201,
  "result_class": "accuracy_failure"
}
```
