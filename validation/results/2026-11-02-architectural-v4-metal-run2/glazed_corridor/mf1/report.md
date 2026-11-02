# Foton report

Status: **incomplete**

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
  "sky_density": 1,
  "status": "incomplete",
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 706269953697064074,
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
  "oracle_stable": false,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": -0.025762782528642295,
        "rms_normalized_error_percent": 0.28693480992515397,
        "absolute_error": {
          "p95": 7.075606845319271e-06,
          "p99": 5.537690594792366e-05,
          "maximum": 0.0001775913406163454
        },
        "worst_index": [
          1,
          94,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": -0.08375558859698146,
        "rms_normalized_error_percent": 0.539328113479543,
        "absolute_error": {
          "p95": 0.0,
          "p99": 6.303394911810756e-06,
          "maximum": 4.316645208746195e-05
        },
        "worst_index": [
          28,
          47,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "bias_percent": -0.403069868915149,
        "rms_normalized_error_percent": 1.627412963662213,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 8.049566531553864e-06
        },
        "worst_index": [
          1,
          19,
          0
        ],
        "passed": true
      }
    ],
    "samples_per_patch": [
      4096,
      16384
    ]
  },
  "depth_stability": {
    "passed": false,
    "grids": [
      {
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": -0.030574348843653208,
        "rms_normalized_error_percent": 0.6594151262476842,
        "absolute_error": {
          "p95": 0.00010414514690637589,
          "p99": 0.00021506007760763168,
          "maximum": 0.0005495548248291016
        },
        "worst_index": [
          10,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": 0.053968402462963694,
        "rms_normalized_error_percent": 2.1772563587170137,
        "absolute_error": {
          "p95": 1.222346691065465e-05,
          "p99": 6.586179370060563e-05,
          "maximum": 0.0002513192594051361
        },
        "worst_index": [
          23,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "bias_percent": 2.2411651615522508,
        "rms_normalized_error_percent": 7.702389026508487,
        "absolute_error": {
          "p95": 1.3922913922215227e-06,
          "p99": 4.484161763684824e-06,
          "maximum": 5.708116805180907e-05
        },
        "worst_index": [
          2,
          0,
          0
        ],
        "passed": false
      }
    ]
  },
  "sample_stability": {
    "passed": false,
    "grids": [
      {
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": 0.017966623910158,
        "rms_normalized_error_percent": 0.6035810780111104,
        "absolute_error": {
          "p95": 8.337595500051975e-05,
          "p99": 0.00017588213086128235,
          "maximum": 0.0008866935968399048
        },
        "worst_index": [
          12,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": -0.06078114322449833,
        "rms_normalized_error_percent": 1.6794814480386533,
        "absolute_error": {
          "p95": 1.110811344915419e-05,
          "p99": 5.024950951337814e-05,
          "maximum": 0.00019061751663684845
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
        "bias_percent": -0.7131403460576311,
        "rms_normalized_error_percent": 6.28757477444953,
        "absolute_error": {
          "p95": 1.3248430605017316e-06,
          "p99": 3.4756449167616665e-06,
          "maximum": 4.044649540446699e-05
        },
        "worst_index": [
          9,
          0,
          0
        ],
        "passed": false
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0633198848304519,
                "cvrmse_percent": 5.182437062193408,
                "rms_normalized_rmse_percent": 1.8957908787421438,
                "reference_energy": 11.022188620842826,
                "candidate_energy": 11.029167857983339,
                "relative_energy_error_percent": 0.06331988483045188,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 9.310466703027484e-05,
                  "p95": 0.00018341699615120888,
                  "p99": 0.0003250009613111615,
                  "maximum": 0.0005862950347363949
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 76,
                  "rgb_channel": 0,
                  "reference": 0.012432795017957687,
                  "candidate": 0.011846499983221292
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.5349940859922718,
                "cvrmse_percent": 34.89401628570735,
                "rms_normalized_rmse_percent": 2.53072571223878,
                "reference_energy": 3.311042145948413,
                "candidate_energy": 3.3287560256139486,
                "relative_energy_error_percent": 0.5349940859922718,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.00018445625901222228,
                  "p95": 0.0003413960221223533,
                  "p99": 0.0006718875374644995,
                  "maximum": 0.0017629843205213547
                },
                "worst": {
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05437351018190384,
                  "candidate": 0.056136494502425194
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
                "nmbe_percent": 0.2330258504130087,
                "cvrmse_percent": 55.308801731847055,
                "rms_normalized_rmse_percent": 7.931732312956043,
                "reference_energy": 0.6258308781384585,
                "candidate_energy": 0.6272892258643878,
                "relative_energy_error_percent": 0.23302585041300872,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011296157026663423,
                  "maximum": 0.0004491958243306726
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 17,
                  "sky_patch_index": 17,
                  "rgb_channel": 0,
                  "reference": 0.0014583735028281808,
                  "candidate": 0.0010091776784975082
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.5993162789630113,
                "cvrmse_percent": 132.83235240105807,
                "rms_normalized_rmse_percent": 8.401008528801047,
                "reference_energy": 0.44504410405857087,
                "candidate_energy": 0.44771132582275897,
                "relative_energy_error_percent": 0.5993162789630113,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.0887197277043015e-07,
                  "p95": 1.536001235535877e-05,
                  "p99": 0.000197269224372576,
                  "maximum": 0.0006058218132238835
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 17,
                  "sky_patch_index": 17,
                  "rgb_channel": 0,
                  "reference": -0.0002767054829746485,
                  "candidate": 0.00032911633024923503
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
                "nmbe_percent": 11.342066048487027,
                "cvrmse_percent": 420.1600409039808,
                "rms_normalized_rmse_percent": 13.176425161829814,
                "reference_energy": 0.004247474840667564,
                "candidate_energy": 0.004729226242488949,
                "relative_energy_error_percent": 11.342066048487025,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.1752351282630116e-05
                },
                "worst": {
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "sky_patch_index": 18,
                  "rgb_channel": 0,
                  "reference": 0.00014432604803005233,
                  "candidate": 0.00019607839931268245
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 9.24222820592759,
                "cvrmse_percent": 521.8896947710924,
                "rms_normalized_rmse_percent": 24.309069463912788,
                "reference_energy": 0.010545138409071342,
                "candidate_energy": 0.011519744165468637,
                "relative_energy_error_percent": 9.242228205927589,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.810735041857697e-06,
                  "maximum": 0.00011437544890213758
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.00033909005287569016,
                  "candidate": 0.00045346550177782774
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 174.98445801902562,
            "full": 480.13574990909547
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.63491692673415,
            "full": 492.7043749485165
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 168.74833300244063,
            "full": 487.970249960199
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 160.20724992267787,
            "full": 481.02195805404335
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": 0.03524920563160003,
                "cvrmse_percent": 3.995771493865593,
                "rms_normalized_rmse_percent": 1.4610569974158194,
                "reference_energy": 11.023265115461072,
                "candidate_energy": 11.027150728848937,
                "relative_energy_error_percent": 0.03524920563160003,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.441554382443423e-05,
                  "p95": 0.00014037953224033117,
                  "p99": 0.0002522696740925312,
                  "maximum": 0.0004264945164322853
                },
                "worst": {
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "sky_patch_index": 99,
                  "rgb_channel": 0,
                  "reference": 0.009023197926580906,
                  "candidate": 0.009449692443013191
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.19819724189081153,
                "cvrmse_percent": 13.777100308695486,
                "rms_normalized_rmse_percent": 1.3595298942813974,
                "reference_energy": 5.642181023597413,
                "candidate_energy": 5.65336367076867,
                "relative_energy_error_percent": 0.19819724189081156,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.7513538586608774e-07,
                  "p90": 0.00012294090120121834,
                  "p95": 0.00022554490715265274,
                  "p99": 0.00043544545769691467,
                  "maximum": 0.001252681016921997
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.08005185425281525,
                  "candidate": 0.08130453526973724
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
                "nmbe_percent": 0.2912752846535528,
                "cvrmse_percent": 30.613104972107827,
                "rms_normalized_rmse_percent": 4.405820282855559,
                "reference_energy": 0.6239767593524448,
                "candidate_energy": 0.6257942494344206,
                "relative_energy_error_percent": 0.2912752846535528,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.792903877794743e-05,
                  "maximum": 0.00020426185801625252
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 17,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.004335786681622267,
                  "candidate": 0.004540048539638519
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.35937365267495985,
                "cvrmse_percent": 37.0635979433079,
                "rms_normalized_rmse_percent": 3.61351292928183,
                "reference_energy": 0.9251605928879059,
                "candidate_energy": 0.9218358094721353,
                "relative_energy_error_percent": 0.3593736526749599,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.739769631280979e-08,
                  "p90": 9.917914212564938e-06,
                  "p95": 2.0191391740809096e-05,
                  "p99": 0.00011334143346175551,
                  "maximum": 0.0003757718950510025
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.00611487147398293,
                  "candidate": 0.005739099578931928
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
                "nmbe_percent": -1.431692465622739,
                "cvrmse_percent": 186.37614595520495,
                "rms_normalized_rmse_percent": 5.8388676314372505,
                "reference_energy": 0.004216485111101065,
                "candidate_energy": 0.004156118011451326,
                "relative_energy_error_percent": 1.431692465622739,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 3.353274951223284e-05
                },
                "worst": {
                  "global_sensor_index": 60,
                  "local_sensor_index": 6,
                  "sky_patch_index": 19,
                  "rgb_channel": 0,
                  "reference": 0.0002641871033119969,
                  "candidate": 0.00023065435379976407
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0007548373583412245,
                "cvrmse_percent": 128.4088827139938,
                "rms_normalized_rmse_percent": 11.732429445788936,
                "reference_energy": 0.03148038348857796,
                "candidate_energy": 0.03148062111427308,
                "relative_energy_error_percent": 0.0007548373583412245,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.1500305845402181e-06,
                  "p95": 2.2055994900682613e-06,
                  "p99": 6.439201644781178e-06,
                  "maximum": 9.486015187576413e-05
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0006810837949160486,
                  "candidate": 0.0007759439467918128
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 236.24558292794973,
            "full": 6705.238749971613
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 238.6414590291679,
            "full": 6700.093084014952
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 252.39512498956174,
            "full": 6728.549459017813
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 233.15362492576241,
            "full": 6824.1231250576675
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": -0.019298548041975217,
                "cvrmse_percent": 3.8019740922450325,
                "rms_normalized_rmse_percent": 1.3905531840644125,
                "reference_energy": 11.022927801511287,
                "candidate_energy": 11.02080053649388,
                "relative_energy_error_percent": 0.01929854804197522,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.697324570268385e-05,
                  "p95": 0.00012743542902171612,
                  "p99": 0.00025227945297956467,
                  "maximum": 0.0004471212159842253
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.007416465552523732,
                  "candidate": 0.007863586768507957
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.09204453167056972,
                "cvrmse_percent": 11.983711534975155,
                "rms_normalized_rmse_percent": 1.1816535575543732,
                "reference_energy": 5.643421248045641,
                "candidate_energy": 5.648615708703602,
                "relative_energy_error_percent": 0.09204453167056972,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.3792499582195887e-07,
                  "p90": 0.00011923283454962073,
                  "p95": 0.00020131422206759453,
                  "p99": 0.0003759767860174179,
                  "maximum": 0.0006198100745677948
                },
                "worst": {
                  "global_sensor_index": 0,
                  "local_sensor_index": 0,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06999391317367554,
                  "candidate": 0.07061372324824333
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
                "nmbe_percent": -0.0681609646979378,
                "cvrmse_percent": 28.74693800494139,
                "rms_normalized_rmse_percent": 4.131198735318291,
                "reference_energy": 0.6267869079119919,
                "candidate_energy": 0.6263596839089587,
                "relative_energy_error_percent": 0.0681609646979378,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.498116999864578e-05,
                  "maximum": 0.00016311369836330414
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 30,
                  "sky_patch_index": 18,
                  "rgb_channel": 0,
                  "reference": 0.0009558794845361263,
                  "candidate": 0.0007927657861728221
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.10577152472362827,
                "cvrmse_percent": 37.64917506456149,
                "rms_normalized_rmse_percent": 3.6813713148085574,
                "reference_energy": 0.9231342534737763,
                "candidate_energy": 0.922157840298631,
                "relative_energy_error_percent": 0.10577152472362826,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.591955425960805e-08,
                  "p90": 9.205253263644408e-06,
                  "p95": 1.8588436614663775e-05,
                  "p99": 0.00010670092888176441,
                  "maximum": 0.0007118652574717999
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.015296634752303362,
                  "candidate": 0.016008500009775162
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
                "nmbe_percent": -6.897608241163657,
                "cvrmse_percent": 281.55652727711157,
                "rms_normalized_rmse_percent": 8.849828289698104,
                "reference_energy": 0.0044006978314428125,
                "candidate_energy": 0.004097154935152503,
                "relative_energy_error_percent": 6.897608241163656,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.065201210323721e-05
                },
                "worst": {
                  "global_sensor_index": 60,
                  "local_sensor_index": 6,
                  "sky_patch_index": 19,
                  "rgb_channel": 0,
                  "reference": 0.000277891056612134,
                  "candidate": 0.00023723904450889677
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.3949608812123637,
                "cvrmse_percent": 120.32435103639067,
                "rms_normalized_rmse_percent": 10.56322597264527,
                "reference_energy": 0.03228097803154739,
                "candidate_energy": 0.03215348079625002,
                "relative_energy_error_percent": 0.3949608812123637,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.1000248534287493e-06,
                  "p95": 2.1218492918251273e-06,
                  "p99": 6.326679567791871e-06,
                  "maximum": 8.912119665183127e-05
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0008204224868677557,
                  "candidate": 0.0007313012902159244
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 238.25366608798504,
            "full": 7091.905917041004
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 228.2176249427721,
            "full": 7164.835334056988
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 233.20395802147686,
            "full": 7032.259999890812
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 232.58291592355818,
            "full": 7133.220958057791
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "start_sensor_index": 0,
            "sensor_count": 18,
            "stages": {
              "direct": {
                "nmbe_percent": -0.008760296083075107,
                "cvrmse_percent": 2.1119762995354385,
                "rms_normalized_rmse_percent": 0.772479861497314,
                "reference_energy": 11.026308906320537,
                "candidate_energy": 11.025342969013309,
                "relative_energy_error_percent": 0.008760296083075107,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.0109071414917645e-05,
                  "p95": 6.98501244187355e-05,
                  "p99": 0.0001368713565170765,
                  "maximum": 0.00024027004837989807
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 74,
                  "rgb_channel": 0,
                  "reference": 0.013518515042960644,
                  "candidate": 0.013758785091340542
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.1281289716578202,
                "cvrmse_percent": 7.374425886137521,
                "rms_normalized_rmse_percent": 0.7272642559185857,
                "reference_energy": 5.648670069939808,
                "candidate_energy": 5.641432487066851,
                "relative_energy_error_percent": 0.1281289716578202,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.260739672190539e-07,
                  "p90": 6.894486723467702e-05,
                  "p95": 0.00011768005788326263,
                  "p99": 0.00023033982142806053,
                  "maximum": 0.0007026754319667816
                },
                "worst": {
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.08330430462956429,
                  "candidate": 0.0826016291975975
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
                "nmbe_percent": 0.13360709422773354,
                "cvrmse_percent": 15.725514892091484,
                "rms_normalized_rmse_percent": 2.2662774696674983,
                "reference_energy": 0.6261125634678137,
                "candidate_energy": 0.6269490942704579,
                "relative_energy_error_percent": 0.13360709422773354,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.317450318718329e-05,
                  "maximum": 0.00011643592733889818
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 16,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.002543459995649755,
                  "candidate": 0.002659895922988653
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.30348594492571124,
                "cvrmse_percent": 21.43751148746937,
                "rms_normalized_rmse_percent": 2.0858973306740345,
                "reference_energy": 0.920350304981806,
                "candidate_energy": 0.9231434388015067,
                "relative_energy_error_percent": 0.30348594492571124,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.236662741798682e-08,
                  "p90": 6.476548151113093e-06,
                  "p95": 1.3028441662754625e-05,
                  "p99": 5.8464473113417625e-05,
                  "maximum": 0.00031869905069470406
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 16,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0077704149298369884,
                  "candidate": 0.008089113980531693
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
                "nmbe_percent": 3.737279844115708,
                "cvrmse_percent": 147.35753801893804,
                "rms_normalized_rmse_percent": 4.606133443520849,
                "reference_energy": 0.004293985039112158,
                "candidate_energy": 0.004454463276488241,
                "relative_energy_error_percent": 3.737279844115708,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 2.0504347048699856e-05
                },
                "worst": {
                  "global_sensor_index": 66,
                  "local_sensor_index": 12,
                  "sky_patch_index": 19,
                  "rgb_channel": 0,
                  "reference": 0.00010271184874000028,
                  "candidate": 0.00012321619578870013
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.3934312420780832,
                "cvrmse_percent": 88.99174342646593,
                "rms_normalized_rmse_percent": 8.082379198584247,
                "reference_energy": 0.03161163347741791,
                "candidate_energy": 0.032052119854423466,
                "relative_energy_error_percent": 1.3934312420780832,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.3439336151514e-07,
                  "p95": 1.5545263041261135e-06,
                  "p99": 5.0091375101146696e-06,
                  "maximum": 4.9378431867808104e-05
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.000717353803338483,
                  "candidate": 0.0007667322352062911
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 391.58329204656184,
            "full": 12394.22737492714
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 396.40316599979997,
            "full": 12420.315958093852
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 390.7924999948591,
            "full": 12480.140667059459
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 393.0371659807861,
            "full": 12282.273374963552
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 3946.828042040579,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 15320.816374965943,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 4096,
      "elapsed_ms": 61714.30991706438,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/direct_16384/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/glazed_corridor/mf1/direct_16384/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 16384,
      "elapsed_ms": 219455.20374993794,
      "worker_pool_size": 12,
      "invocation_count": 6
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      90,
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
        "identifier": "glazed_corridor_corridor_grid",
        "full_identifier": "glazed_corridor_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 18,
        "stages": {
          "direct": {
            "nmbe_percent": -0.4318278213994641,
            "cvrmse_percent": 2.7790117929935074,
            "rms_normalized_rmse_percent": 1.0188249251242603,
            "reference_energy": 11.024760444924823,
            "candidate_energy": 10.977152462080994,
            "relative_energy_error_percent": 0.4318278213994641,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0874451254494462e-05,
              "p95": 5.478193997987546e-05,
              "p99": 0.00016140971274580806,
              "maximum": 0.0004501957446336746
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.0004501957446336746,
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
            "nmbe_percent": -0.4245133334548889,
            "cvrmse_percent": 13.969890923712422,
            "rms_normalized_rmse_percent": 1.3776423799250805,
            "reference_energy": 5.646116831963511,
            "candidate_energy": 5.622148313189385,
            "relative_energy_error_percent": 0.42451333345488895,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.321840040371171e-06,
              "p90": 8.59856605529785e-05,
              "p95": 0.0001420760527253151,
              "p99": 0.00044947373680770397,
              "maximum": 0.0013758018612861633
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07093927264213562,
              "candidate": 0.06956347078084946,
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
            "nmbe_percent": -0.429350540041373,
            "cvrmse_percent": 4.444669097150058,
            "rms_normalized_rmse_percent": 1.2941705316089804,
            "reference_energy": 16.670877276888334,
            "candidate_energy": 16.59930077527038,
            "relative_energy_error_percent": 0.42935054004137296,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.4340928942147002e-06,
              "p90": 7.307175546884524e-05,
              "p95": 0.00011801929213106632,
              "p99": 0.0003124568611383438,
              "maximum": 0.0013758018612861633
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07093927264213562,
              "candidate": 0.06956347078084946,
              "position": [
                2.5,
                2.5,
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
            "nmbe_percent": 0.03628867339602054,
            "cvrmse_percent": 5.776908355348413,
            "rms_normalized_rmse_percent": 0.8312106476517812,
            "reference_energy": 0.6263632300833262,
            "candidate_energy": 0.6265905289901639,
            "relative_energy_error_percent": 0.03628867339602054,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.801689207553864e-06,
              "maximum": 6.863447197247297e-05
            },
            "worst": {
              "global_sensor_index": 50,
              "local_sensor_index": 32,
              "sky_patch_index": 13,
              "rgb_channel": 0,
              "reference": 6.863447197247297e-05,
              "candidate": 0.0,
              "position": [
                5.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.15353962405239688,
            "cvrmse_percent": 28.44193765355543,
            "rms_normalized_rmse_percent": 2.76540383801654,
            "reference_energy": 0.921914476020973,
            "candidate_energy": 0.9204989720004058,
            "relative_energy_error_percent": 0.15353962405239688,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1556325318906602e-07,
              "p90": 1.2107637303415686e-05,
              "p95": 2.1064420434413464e-05,
              "p99": 5.389191210269928e-05,
              "maximum": 0.0003415588289499283
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0048869913443923,
              "candidate": 0.005228550173342228,
              "position": [
                4.5,
                8.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.07674366872589204,
            "cvrmse_percent": 16.841517059745627,
            "rms_normalized_rmse_percent": 2.7500387709308387,
            "reference_energy": 1.5482777061042992,
            "candidate_energy": 1.5470895009905696,
            "relative_energy_error_percent": 0.07674366872589203,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1556325318906602e-07,
              "p90": 1.2223143130540848e-05,
              "p95": 2.0891387976007526e-05,
              "p99": 5.389191210269928e-05,
              "maximum": 0.0003415588289499283
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 24,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0048869913443923,
              "candidate": 0.005228550173342228,
              "position": [
                4.5,
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
            "nmbe_percent": 0.10616207460462337,
            "cvrmse_percent": 39.93758431331301,
            "rms_normalized_rmse_percent": 1.2614561781296112,
            "reference_energy": 0.004281973812432227,
            "candidate_energy": 0.004286519644665532,
            "relative_energy_error_percent": 0.10616207460462336,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 5.741254426538944e-06
            },
            "worst": {
              "global_sensor_index": 55,
              "local_sensor_index": 1,
              "sky_patch_index": 19,
              "rgb_channel": 0,
              "reference": 0.0002758817281574011,
              "candidate": 0.00028162298258394003,
              "position": [
                6.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.8295376768949391,
            "cvrmse_percent": 105.17931150189678,
            "rms_normalized_rmse_percent": 9.525985227675159,
            "reference_energy": 0.03192412714523485,
            "candidate_energy": 0.032188949807924416,
            "relative_energy_error_percent": 0.8295376768949391,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.4468345810314531e-06,
              "p95": 2.7172964585986374e-06,
              "p99": 7.2649568210181314e-06,
              "maximum": 5.940574919804931e-05
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007411242695525289,
              "candidate": 0.0008005300187505782,
              "position": [
                6.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.7439864768587585,
            "cvrmse_percent": 92.7821362030784,
            "rms_normalized_rmse_percent": 9.530302237381667,
            "reference_energy": 0.036206100957667076,
            "candidate_energy": 0.03647546945258995,
            "relative_energy_error_percent": 0.7439864768587585,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.4478607397450105e-06,
              "p95": 2.7239380870014426e-06,
              "p99": 7.296222690911236e-06,
              "maximum": 5.940574919804931e-05
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007411242695525289,
              "candidate": 0.0008005300187505782,
              "position": [
                6.5,
                6.5,
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
        "identifier": "glazed_corridor_corridor_grid",
        "full_identifier": "glazed_corridor_corridor_grid",
        "start_sensor_index": 0,
        "sensor_count": 18,
        "stages": {
          "direct": {
            "nmbe_percent": -0.4318278213994641,
            "cvrmse_percent": 2.7790117929935074,
            "rms_normalized_rmse_percent": 1.0188249251242603,
            "reference_energy": 11.024760444924823,
            "candidate_energy": 10.977152462080994,
            "relative_energy_error_percent": 0.4318278213994641,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.0874451254494462e-05,
              "p95": 5.478193997987546e-05,
              "p99": 0.00016140971274580806,
              "maximum": 0.0004501957446336746
            },
            "worst": {
              "global_sensor_index": 6,
              "local_sensor_index": 6,
              "sky_patch_index": 31,
              "rgb_channel": 0,
              "reference": 0.0004501957446336746,
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
            "nmbe_percent": 69.30016003481587,
            "cvrmse_percent": 406.04480596190507,
            "rms_normalized_rmse_percent": 29.477840469421103,
            "reference_energy": 3.32081689233679,
            "candidate_energy": 5.622148313189385,
            "relative_energy_error_percent": 69.30016003481587,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.740391140003794e-05,
              "p90": 0.0005224648746661841,
              "p95": 0.0006673363968729973,
              "p99": 0.0010295244865119457,
              "maximum": 0.025773264467716217
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04504401236772537,
              "candidate": 0.07081727683544159,
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
            "nmbe_percent": 15.710231697366968,
            "cvrmse_percent": 93.96943034308993,
            "rms_normalized_rmse_percent": 29.47008580711768,
            "reference_energy": 14.345577337261613,
            "candidate_energy": 16.59930077527038,
            "relative_energy_error_percent": 15.710231697366966,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0035653303930303e-06,
              "p90": 0.0005223105777986347,
              "p95": 0.0006710086017847061,
              "p99": 0.0010281847789883614,
              "maximum": 0.025773264467716217
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04504401236772537,
              "candidate": 0.07081727683544159,
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
            "nmbe_percent": 0.03628867339602054,
            "cvrmse_percent": 5.776908355348413,
            "rms_normalized_rmse_percent": 0.8312106476517812,
            "reference_energy": 0.6263632300833262,
            "candidate_energy": 0.6265905289901639,
            "relative_energy_error_percent": 0.03628867339602054,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 7.801689207553864e-06,
              "maximum": 6.863447197247297e-05
            },
            "worst": {
              "global_sensor_index": 50,
              "local_sensor_index": 32,
              "sky_patch_index": 13,
              "rgb_channel": 0,
              "reference": 6.863447197247297e-05,
              "candidate": 0.0,
              "position": [
                5.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 106.12437378596002,
            "cvrmse_percent": 639.8965513367074,
            "rms_normalized_rmse_percent": 40.5510891888427,
            "reference_energy": 0.4465745389995721,
            "candidate_energy": 0.9204989720004058,
            "relative_energy_error_percent": 106.12437378596,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.704000068362802e-05,
              "p95": 0.0001009869637982774,
              "p99": 0.00027011753991246223,
              "maximum": 0.004323975183069706
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011118074879050255,
              "candidate": 0.01544205006211996,
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
            "nmbe_percent": 44.191913601192,
            "cvrmse_percent": 266.3572243617765,
            "rms_normalized_rmse_percent": 40.554384041858924,
            "reference_energy": 1.0729377690828983,
            "candidate_energy": 1.5470895009905696,
            "relative_energy_error_percent": 44.191913601192,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.686000076821074e-05,
              "p95": 0.00010095003685819392,
              "p99": 0.0002678439486771822,
              "maximum": 0.004323975183069706
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011118074879050255,
              "candidate": 0.01544205006211996,
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
            "nmbe_percent": 0.10616207460462337,
            "cvrmse_percent": 39.93758431331301,
            "rms_normalized_rmse_percent": 1.2614561781296112,
            "reference_energy": 0.004281973812432227,
            "candidate_energy": 0.004286519644665532,
            "relative_energy_error_percent": 0.10616207460462336,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 5.741254426538944e-06
            },
            "worst": {
              "global_sensor_index": 55,
              "local_sensor_index": 1,
              "sky_patch_index": 19,
              "rgb_channel": 0,
              "reference": 0.0002758817281574011,
              "candidate": 0.00028162298258394003,
              "position": [
                6.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 186.40867241473683,
            "cvrmse_percent": 1440.9399972073077,
            "rms_normalized_rmse_percent": 68.29860753395442,
            "reference_energy": 0.011238818132333961,
            "candidate_energy": 0.032188949807924416,
            "relative_energy_error_percent": 186.40867241473683,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9999999949504854e-06,
              "p95": 4.439499889485876e-06,
              "p99": 2.1303298581187846e-05,
              "maximum": 0.0004042522341478616
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00039627778460271657,
              "candidate": 0.0008005300187505782,
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
            "nmbe_percent": 135.01036275980718,
            "cvrmse_percent": 1043.3517533123375,
            "rms_normalized_rmse_percent": 68.29516157729934,
            "reference_energy": 0.015520791944766188,
            "candidate_energy": 0.03647546945258995,
            "relative_energy_error_percent": 135.01036275980718,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9999999949504854e-06,
              "p95": 4.439499889485876e-06,
              "p99": 2.1429999833344482e-05,
              "maximum": 0.0004042522341478616
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00039627778460271657,
              "candidate": 0.0008005300187505782,
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
      "bias_percent": -0.19217152627193007,
      "rms_normalized_error_percent": 0.4004536378255035,
      "absolute_error": {
        "p95": 0.17154758565322364,
        "p99": 0.4570315963013851,
        "maximum": 0.48711013074272813
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.108524680835355,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.4004536378255035
    },
    "overcast": {
      "bias_percent": -0.14890471476651984,
      "rms_normalized_error_percent": 0.2843931120013644,
      "absolute_error": {
        "p95": 0.07854666709899902,
        "p99": 0.22636443138122558,
        "maximum": 0.25099658966064453
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.922800064086914,
      "reference_fraction_of_uniform": 0.6502480506896973,
      "rms_normalized_to_uniform_percent": 0.1972524363452233
    },
    "horizon": {
      "bias_percent": 0.08944546922937216,
      "rms_normalized_error_percent": 1.820598447625249,
      "absolute_error": {
        "p95": 0.0649709014831791,
        "p99": 0.0921374043864085,
        "maximum": 0.09842940800007494
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7783034284065448,
      "reference_fraction_of_uniform": 0.08544780364312143,
      "rms_normalized_to_uniform_percent": 0.11303470816507759
    },
    "north": {
      "bias_percent": -69.31308224059585,
      "rms_normalized_error_percent": 110.4833874684758,
      "absolute_error": {
        "p95": 7.00942371622659e-05,
        "p99": 0.00017872725904453544,
        "maximum": 0.00019314132805448025
      },
      "worst_index": [
        82
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.47193286466063e-05,
      "reference_fraction_of_uniform": 1.6159948472704855e-06,
      "rms_normalized_to_uniform_percent": 0.00016200463736481104
    },
    "east": {
      "bias_percent": -0.21210763205349134,
      "rms_normalized_error_percent": 0.4209831253820017,
      "absolute_error": {
        "p95": 0.057784330844879134,
        "p99": 0.08233436584472656,
        "maximum": 0.08347511291503906
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.8539268970489502,
      "reference_fraction_of_uniform": 0.20353756844997406,
      "rms_normalized_to_uniform_percent": 0.09172513245915902
    },
    "south": {
      "bias_percent": -0.2695824037504039,
      "rms_normalized_error_percent": 0.5666759556926451,
      "absolute_error": {
        "p95": 0.1586206436157226,
        "p99": 0.41011791229248046,
        "maximum": 0.44965362548828125
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.17747688293457,
      "reference_fraction_of_uniform": 0.6782082915306091,
      "rms_normalized_to_uniform_percent": 0.36350358283464096
    },
    "west": {
      "bias_percent": -0.12415561394879719,
      "rms_normalized_error_percent": 0.3146489270252479,
      "absolute_error": {
        "p95": 0.0321556806564331,
        "p99": 0.05872885704040526,
        "maximum": 0.08219480514526367
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.793677568435669,
      "reference_fraction_of_uniform": 0.19692295789718628,
      "rms_normalized_to_uniform_percent": 0.06585468396776058
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
          "nmbe_percent": -0.22442837685905898,
          "cvrmse_percent": 1.1974262873876522,
          "absolute_error_percentiles_lux": {
            "p50": 6.904052734375,
            "p90": 53.47053222656253,
            "p95": 82.83919677734376,
            "p99": 176.83625976562502
          },
          "maximum_absolute_error_lux": 783.9638671875,
          "worst": {
            "sensor_index": 6,
            "position": [
              2.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 15833.4306640625,
            "radiance_lux": 16617.39453125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07519786910198197,
            "maximum_error_percentage_points": 0.30616438356165077,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.02929766873185634,
            "maximum_error_percentage_points": 0.11525723879746863,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.02350837138508381,
            "maximum_error_percentage_points": 0.11123287671232873,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1537595129375943,
            "maximum_error_percentage_points": 0.3534246575342479,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.17229071537290697,
            "maximum_error_percentage_points": 0.4646575342465731,
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
          "nmbe_percent": -0.02578599257922831,
          "cvrmse_percent": 5.054231726309377,
          "absolute_error_percentiles_lux": {
            "p50": 0.9432563781738281,
            "p90": 8.261659240722656,
            "p95": 12.720992279052727,
            "p99": 25.41154548645017
          },
          "maximum_absolute_error_lux": 107.51806640625,
          "worst": {
            "sensor_index": 18,
            "position": [
              3.5,
              8.5,
              0.75
            ],
            "hour_of_year": 348.5,
            "foton_lux": 1693.3585205078125,
            "radiance_lux": 1585.8404541015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.16067351598173515,
            "maximum_error_percentage_points": 0.956164383561644,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3681778502320251,
            "maximum_error_percentage_points": 1.2897594368512593,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.8831659056316594,
            "maximum_error_percentage_points": 3.5106849315068445,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.8796727549467288,
            "maximum_error_percentage_points": 3.5106849315068516,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.005555555555555548,
            "maximum_error_percentage_points": 0.07931506849315062,
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
          "nmbe_percent": -0.8379053987898155,
          "cvrmse_percent": 35.28075756622164,
          "absolute_error_percentiles_lux": {
            "p50": 0.09028402343392372,
            "p90": 0.9039496898651127,
            "p95": 1.5369795322418178,
            "p99": 3.5066709995269707
          },
          "maximum_absolute_error_lux": 12.246709823608398,
          "worst": {
            "sensor_index": 3,
            "position": [
              6.5,
              5.5,
              0.75
            ],
            "hour_of_year": 1954.5,
            "foton_lux": 29.61469078063965,
            "radiance_lux": 17.36798095703125
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.049315176961951805,
            "maximum_error_percentage_points": 0.1827319733656067,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.0014840182648402983,
            "maximum_error_percentage_points": 0.02863013698629402,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0014840182648401838,
            "maximum_error_percentage_points": 0.028630136986301402,
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
    "numerical_correctness": "incomplete",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.0049785248220782785,
      "metrics": {
        "da": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004955586472604523,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004962007705479721,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0049785248220782785,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.0045205479452086195,
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
      "study_preparation_seconds": 0.07602983305696398,
      "weather_seconds": 0.20815087493974715,
      "metric_reduction_seconds": 0.0922120000468567,
      "write_seconds": 0.06888574990443885,
      "total_seconds": 0.37015129101928324,
      "cold_end_to_end_seconds": 0.4461811240762472,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03231983399018645,
      "engine_upload_seconds": 0.000274667,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.07388591661583632,
      "engine_annual_reduction_seconds": 0.0007573749171569943,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.07388591661583632
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.07602983305696398,
      "weather_seconds": 0.13021937501616776,
      "metric_reduction_seconds": 0.013247541966848075,
      "write_seconds": 0.059548582998104393,
      "total_seconds": 0.2032210840843618,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2032210840843618,
      "raw_export_seconds": 0.022844291059300303,
      "engine_upload_seconds": 5.9792e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0007662499556317925,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.011024625040590763,
      "full": 0.0634859170531854
    }
  },
  "elapsed_seconds": 414.0341787500074,
  "result_class": "unstable_reference"
}
```
