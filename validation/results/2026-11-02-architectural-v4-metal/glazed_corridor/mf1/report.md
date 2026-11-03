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
  "model_sha256": "1659d34e511112066d7c346748c85009a2f30d25bd4c9b7b205a76ff2579b640",
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": false,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "glazed_corridor_corridor_grid",
        "bias_percent": -0.025761703068628725,
        "rms_normalized_error_percent": 0.2869347950124172,
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
        "bias_percent": -0.08382821778191002,
        "rms_normalized_error_percent": 0.5392739379610798,
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
        "bias_percent": 0.05016238570819373,
        "rms_normalized_error_percent": 0.6490296630146007,
        "absolute_error": {
          "p95": 0.0001141370739787817,
          "p99": 0.00019466504454612732,
          "maximum": 0.0004961341619491577
        },
        "worst_index": [
          3,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": 0.008304381671624441,
        "rms_normalized_error_percent": 2.038389904506289,
        "absolute_error": {
          "p95": 1.3503799345926368e-05,
          "p99": 6.416917312890291e-05,
          "maximum": 0.00023450469598174095
        },
        "worst_index": [
          20,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_meeting_grid",
        "bias_percent": -0.7098794735841409,
        "rms_normalized_error_percent": 7.9313323042141475,
        "absolute_error": {
          "p95": 1.5835305873679298e-06,
          "p99": 5.170853000890929e-06,
          "maximum": 4.47125785285607e-05
        },
        "worst_index": [
          10,
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
        "bias_percent": -0.051066064190401654,
        "rms_normalized_error_percent": 0.5973259970796954,
        "absolute_error": {
          "p95": 9.589362889528275e-05,
          "p99": 0.00018005911260843277,
          "maximum": 0.0005881115794181824
        },
        "worst_index": [
          13,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "glazed_corridor_office_grid",
        "bias_percent": 0.12894692105150804,
        "rms_normalized_error_percent": 2.032951541748643,
        "absolute_error": {
          "p95": 1.1209950025659055e-05,
          "p99": 5.4296397138386965e-05,
          "maximum": 0.0003208443522453308
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
        "bias_percent": 0.02745743961494384,
        "rms_normalized_error_percent": 5.89360511730805,
        "absolute_error": {
          "p95": 1.2304911777505353e-06,
          "p99": 4.4694165808323305e-06,
          "maximum": 4.233178333379328e-05
        },
        "worst_index": [
          14,
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
                "nmbe_percent": -0.008303876574908853,
                "cvrmse_percent": 7.8678476587407955,
                "rms_normalized_rmse_percent": 2.8762580708258416,
                "reference_energy": 11.028473735624175,
                "candidate_energy": 11.027557944777072,
                "relative_energy_error_percent": 0.008303876574908853,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0001608568185474723,
                  "p95": 0.00027452316135168076,
                  "p99": 0.0004989197477698326,
                  "maximum": 0.0007574015762656927
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 17,
                  "rgb_channel": 0,
                  "reference": 0.003183512482792139,
                  "candidate": 0.0024261109065264463
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.30238453938227733,
                "cvrmse_percent": 41.57154249283937,
                "rms_normalized_rmse_percent": 3.02819782350576,
                "reference_energy": 3.336867016120472,
                "candidate_energy": 3.326776846163977,
                "relative_energy_error_percent": 0.3023845393822774,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0002447374165058127,
                  "p95": 0.00043610879220068455,
                  "p99": 0.0008188704960048199,
                  "maximum": 0.0013894247822463512
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 101,
                  "rgb_channel": 0,
                  "reference": -0.0005050096660852432,
                  "candidate": 0.000884415116161108
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
                "nmbe_percent": 0.2930869656606901,
                "cvrmse_percent": 57.221970237013245,
                "rms_normalized_rmse_percent": 8.210884156768818,
                "reference_energy": 0.6274016404913709,
                "candidate_energy": 0.6292404729219925,
                "relative_energy_error_percent": 0.29308696566069015,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00011334034206811339,
                  "maximum": 0.0004103615938220173
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 18,
                  "rgb_channel": 0,
                  "reference": 0.001365858013741672,
                  "candidate": 0.0009554964199196547
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.1295789884857516,
                "cvrmse_percent": 119.97893798528449,
                "rms_normalized_rmse_percent": 7.61270067295076,
                "reference_energy": 0.4454506730519867,
                "candidate_energy": 0.44602788352833045,
                "relative_energy_error_percent": 0.1295789884857516,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2411010175128467e-07,
                  "p95": 1.5966132627909027e-05,
                  "p99": 0.0001841915654949844,
                  "maximum": 0.0004651173949241638
                },
                "worst": {
                  "global_sensor_index": 46,
                  "local_sensor_index": 28,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": -3.042339812964201e-05,
                  "candidate": 0.0004346939967945218
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
                "nmbe_percent": -9.383546712291569,
                "cvrmse_percent": 432.11167985134284,
                "rms_normalized_rmse_percent": 13.82599927462416,
                "reference_energy": 0.004367816563899396,
                "candidate_energy": 0.003957960456318688,
                "relative_energy_error_percent": 9.383546712291569,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 5.475280340760946e-05
                },
                "worst": {
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "sky_patch_index": 19,
                  "rgb_channel": 0,
                  "reference": 0.00028429100348148495,
                  "candidate": 0.0002295382000738755
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -5.692422801221545,
                "cvrmse_percent": 353.42112123589504,
                "rms_normalized_rmse_percent": 16.875607599110296,
                "reference_energy": 0.01155485417308455,
                "candidate_energy": 0.010897103019487986,
                "relative_energy_error_percent": 5.692422801221545,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.37059599487111e-06,
                  "maximum": 0.0001136779465014115
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0004958264471497387,
                  "candidate": 0.00038214850064832717
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 182.82587500289083,
            "full": 492.16062494087964
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 158.2993339980021,
            "full": 482.236583949998
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 154.4596249004826,
            "full": 479.5918329618871
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.43545794207603,
            "full": 473.13970897812396
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
                "nmbe_percent": -0.009453541284008726,
                "cvrmse_percent": 3.9808409178793447,
                "rms_normalized_rmse_percent": 1.455901313561009,
                "reference_energy": 11.025532034630487,
                "candidate_energy": 11.024489731407812,
                "relative_energy_error_percent": 0.009453541284008726,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.999662346061083e-05,
                  "p95": 0.0001361954491585493,
                  "p99": 0.0002569642383605242,
                  "maximum": 0.0004664747975766659
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 73,
                  "rgb_channel": 0,
                  "reference": 0.010303755290806293,
                  "candidate": 0.01077023008838296
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.020244170833683062,
                "cvrmse_percent": 12.490174039052777,
                "rms_normalized_rmse_percent": 1.231135402531209,
                "reference_energy": 5.646489375003394,
                "candidate_energy": 5.647632459958576,
                "relative_energy_error_percent": 0.020244170833683066,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.0645477383804973e-07,
                  "p90": 0.00012109566014260051,
                  "p95": 0.0001992939505726099,
                  "p99": 0.0003728047013282776,
                  "maximum": 0.0011104904115200043
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.08290578424930573,
                  "candidate": 0.08401627466082573
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
                "nmbe_percent": 0.19845004462532104,
                "cvrmse_percent": 30.85005173040594,
                "rms_normalized_rmse_percent": 4.434924057232378,
                "reference_energy": 0.6259808807690206,
                "candidate_energy": 0.6272231401062527,
                "relative_energy_error_percent": 0.198450044625321,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.593740545213223e-05,
                  "maximum": 0.0002486761659383774
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.004347160458564758,
                  "candidate": 0.004595836624503136
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.40260286850463894,
                "cvrmse_percent": 36.25693206556375,
                "rms_normalized_rmse_percent": 3.5234641550531287,
                "reference_energy": 0.9215911481789796,
                "candidate_energy": 0.9178807957805262,
                "relative_energy_error_percent": 0.40260286850463894,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.452438050530418e-08,
                  "p90": 9.13304029381834e-06,
                  "p95": 1.8467261247678822e-05,
                  "p99": 0.00011668243678286672,
                  "maximum": 0.00031190644949674606
                },
                "worst": {
                  "global_sensor_index": 47,
                  "local_sensor_index": 29,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.006426297593861818,
                  "candidate": 0.006738204043358564
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.5162258539017253,
                "cvrmse_percent": 336.81873433711456,
                "rms_normalized_rmse_percent": 10.752318450850183,
                "reference_energy": 0.004175821934040869,
                "candidate_energy": 0.004197378606477287,
                "relative_energy_error_percent": 0.5162258539017253,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.743540193885565e-05
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 2,
                  "sky_patch_index": 19,
                  "rgb_channel": 0,
                  "reference": 0.0003739213425433263,
                  "candidate": 0.00042135674448218197
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.9779944300468966,
                "cvrmse_percent": 117.70368577863577,
                "rms_normalized_rmse_percent": 10.64045072348715,
                "reference_energy": 0.03270347682436281,
                "candidate_energy": 0.03238363864258886,
                "relative_energy_error_percent": 0.9779944300468966,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.1248884952408389e-06,
                  "p95": 2.131571732633116e-06,
                  "p99": 7.283508011823869e-06,
                  "maximum": 7.789694063831121e-05
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 2,
                  "sky_patch_index": 19,
                  "rgb_channel": 0,
                  "reference": 5.740740743931383e-05,
                  "candidate": -2.048953319899738e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 237.88887495175004,
            "full": 6781.637292006053
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 237.28583299089223,
            "full": 6704.001166974194
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 227.45875001419336,
            "full": 6676.373000023887
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 229.77816709317267,
            "full": 6697.038874961436
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
                "nmbe_percent": 0.060526650429466124,
                "cvrmse_percent": 3.9812952670131363,
                "rms_normalized_rmse_percent": 1.456235395171869,
                "reference_energy": 11.026299903170184,
                "candidate_energy": 11.03297375316788,
                "relative_energy_error_percent": 0.06052665042946613,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 7.157642394304275e-05,
                  "p95": 0.00013332394883036613,
                  "p99": 0.00025192974135279655,
                  "maximum": 0.000476970337331295
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 72,
                  "rgb_channel": 0,
                  "reference": 0.013533629942685366,
                  "candidate": 0.01401060028001666
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.023846871132038545,
                "cvrmse_percent": 12.527401963448016,
                "rms_normalized_rmse_percent": 1.236095432154374,
                "reference_energy": 5.650124410889781,
                "candidate_energy": 5.6514717887768455,
                "relative_energy_error_percent": 0.023846871132038542,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.788744263350964e-07,
                  "p90": 0.00010598032968118787,
                  "p95": 0.0002020946703851223,
                  "p99": 0.0003863195888698101,
                  "maximum": 0.0012199506163597107
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07208307087421417,
                  "candidate": 0.07330302149057388
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
                "nmbe_percent": 0.3186109454620767,
                "cvrmse_percent": 28.814785800543213,
                "rms_normalized_rmse_percent": 4.137154443372571,
                "reference_energy": 0.6241853865158191,
                "candidate_energy": 0.6261741094772333,
                "relative_energy_error_percent": 0.31861094546207663,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 6.914499681442976e-05,
                  "maximum": 0.00018064951291307807
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 15,
                  "rgb_channel": 0,
                  "reference": 0.0011713815038092434,
                  "candidate": 0.0013520310167223215
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.4354544555568121,
                "cvrmse_percent": 36.11583404260539,
                "rms_normalized_rmse_percent": 3.5232000234416496,
                "reference_energy": 0.9232969174246293,
                "candidate_energy": 0.919276379859685,
                "relative_energy_error_percent": 0.4354544555568121,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.746854985806294e-08,
                  "p90": 9.45047395362053e-06,
                  "p95": 1.954658700924474e-05,
                  "p99": 0.00011879130033776164,
                  "maximum": 0.0003235058393329382
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0059368673246353865,
                  "candidate": 0.005613361485302448
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "start_sensor_index": 54,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -4.278118213948989,
                "cvrmse_percent": 258.0177205091855,
                "rms_normalized_rmse_percent": 8.221400854514455,
                "reference_energy": 0.004360857608844526,
                "candidate_energy": 0.004174294965196168,
                "relative_energy_error_percent": 4.27811821394899,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.0393846575170755e-05
                },
                "worst": {
                  "global_sensor_index": 55,
                  "local_sensor_index": 1,
                  "sky_patch_index": 19,
                  "rgb_channel": 0,
                  "reference": 0.0003030794468941167,
                  "candidate": 0.00026268560031894594
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 3.0254812375756397,
                "cvrmse_percent": 142.42794705657894,
                "rms_normalized_rmse_percent": 12.974744272099965,
                "reference_energy": 0.03172197070411187,
                "candidate_energy": 0.032681712975954014,
                "relative_energy_error_percent": 3.0254812375756397,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.0656179370016616e-06,
                  "p95": 2.1272000999772407e-06,
                  "p99": 7.5056959758512676e-06,
                  "maximum": 9.060345473699272e-05
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.000732688611606136,
                  "candidate": 0.0008232920663431287
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 234.71020895522088,
            "full": 6956.098792026751
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 250.9923749603331,
            "full": 7024.816166027449
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 232.64554096385837,
            "full": 7062.909833039157
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 225.99787497892976,
            "full": 7135.37949998863
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
                "nmbe_percent": -0.03801474241343358,
                "cvrmse_percent": 2.1739761649624967,
                "rms_normalized_rmse_percent": 0.7952122745929,
                "reference_energy": 11.027623570907053,
                "candidate_energy": 11.02343144821225,
                "relative_energy_error_percent": 0.038014742413433576,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.9862049743533124e-05,
                  "p95": 7.823144551366568e-05,
                  "p99": 0.0001390804536640644,
                  "maximum": 0.00024267565459012985
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 133,
                  "rgb_channel": 0,
                  "reference": 0.018119284883141518,
                  "candidate": 0.018361960537731647
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.08905600209702715,
                "cvrmse_percent": 7.749724707462143,
                "rms_normalized_rmse_percent": 0.7641417906100592,
                "reference_energy": 5.64387626913107,
                "candidate_energy": 5.648902479699661,
                "relative_energy_error_percent": 0.08905600209702715,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.7298085569782415e-07,
                  "p90": 7.245865417644379e-05,
                  "p95": 0.00012501387391239405,
                  "p99": 0.00022469926625490189,
                  "maximum": 0.0006360039114952087
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06514180824160576,
                  "candidate": 0.06577781215310097
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
                "nmbe_percent": 0.17555854069760285,
                "cvrmse_percent": 16.235239814208008,
                "rms_normalized_rmse_percent": 2.3307614061337296,
                "reference_energy": 0.6262126055326007,
                "candidate_energy": 0.6273119752445382,
                "relative_energy_error_percent": 0.17555854069760288,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.4490483812987804e-05,
                  "maximum": 0.00011235644342377782
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 18,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0013936904724687338,
                  "candidate": 0.001281334029044956
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0820596702350238,
                "cvrmse_percent": 25.015646713103084,
                "rms_normalized_rmse_percent": 2.440424338360234,
                "reference_energy": 0.9213202105401059,
                "candidate_energy": 0.9220762428666838,
                "relative_energy_error_percent": 0.08205967023502381,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.000000058430487e-08,
                  "p90": 6.430454959627241e-06,
                  "p95": 1.275482318305872e-05,
                  "p99": 6.715388735756278e-05,
                  "maximum": 0.00048659928143024445
                },
                "worst": {
                  "global_sensor_index": 41,
                  "local_sensor_index": 23,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.015559470281004906,
                  "candidate": 0.01604606956243515
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
                "nmbe_percent": -0.7011095729679321,
                "cvrmse_percent": 65.1151530500973,
                "rms_normalized_rmse_percent": 2.0616843408965884,
                "reference_energy": 0.004396861550048925,
                "candidate_energy": 0.004366034732811386,
                "relative_energy_error_percent": 0.7011095729679321,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 1.0202751582255587e-05
                },
                "worst": {
                  "global_sensor_index": 66,
                  "local_sensor_index": 12,
                  "sky_patch_index": 19,
                  "rgb_channel": 0,
                  "reference": 0.0001368434022879228,
                  "candidate": 0.0001266406507056672
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.043507997061932126,
                "cvrmse_percent": 76.37772515731994,
                "rms_normalized_rmse_percent": 6.78944705829002,
                "reference_energy": 0.03209100260114184,
                "candidate_energy": 0.03210496475361069,
                "relative_energy_error_percent": 0.043507997061932126,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.407283011990785e-07,
                  "p95": 1.5421076552613026e-06,
                  "p99": 4.499699571169913e-06,
                  "maximum": 4.9462803872302175e-05
                },
                "worst": {
                  "global_sensor_index": 56,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0007639902469236404,
                  "candidate": 0.0007145274430513382
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 397.0573330298066,
            "full": 12314.680749899708
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 383.5564999608323,
            "full": 12328.284541959874
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 374.68912499025464,
            "full": 12281.457624980249
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 394.1874169977382,
            "full": 12405.54745902773
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 4054.4867500429973,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 15504.255915991962,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/direct_4096/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/direct_4096/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 4096,
      "elapsed_ms": 61969.22274993267,
      "worker_pool_size": 12,
      "invocation_count": 6
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/direct_16384/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/glazed_corridor/mf1/direct_16384/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 16384,
      "elapsed_ms": 224079.5760418987,
      "worker_pool_size": 12,
      "invocation_count": 6
    }
  ],
  "coefficients": {
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
            "nmbe_percent": -0.4318298612986613,
            "cvrmse_percent": 2.779017156854135,
            "rms_normalized_rmse_percent": 1.018826911567272,
            "reference_energy": 11.024760670794194,
            "candidate_energy": 10.977152462080994,
            "relative_energy_error_percent": 0.4318298612986613,
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
            "nmbe_percent": -0.24874544007520083,
            "cvrmse_percent": 18.745047176038216,
            "rms_normalized_rmse_percent": 1.8486723491746366,
            "reference_energy": 5.6471561981841365,
            "candidate_energy": 5.633109154647229,
            "relative_energy_error_percent": 0.24874544007520083,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.610702257603407e-06,
              "p90": 0.00013986970152473073,
              "p95": 0.00020498782396316528,
              "p99": 0.00041957246139645576,
              "maximum": 0.00334177166223526
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07770479470491409,
              "candidate": 0.07436302304267883,
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
            "nmbe_percent": -0.36981501728112526,
            "cvrmse_percent": 6.125698809392505,
            "rms_normalized_rmse_percent": 1.783547922375207,
            "reference_energy": 16.67191686897833,
            "candidate_energy": 16.610261616728224,
            "relative_energy_error_percent": 0.3698150172811146,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.2240355974645354e-06,
              "p90": 0.00012300459202378982,
              "p95": 0.0001881960779428482,
              "p99": 0.00038401782512664795,
              "maximum": 0.00334177166223526
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07770479470491409,
              "candidate": 0.07436302304267883,
              "position": [
                1.5,
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
            "nmbe_percent": 0.036244331671617,
            "cvrmse_percent": 5.7768589037582965,
            "rms_normalized_rmse_percent": 0.831203649128976,
            "reference_energy": 0.6263635077229548,
            "candidate_energy": 0.6265905289901639,
            "relative_energy_error_percent": 0.036244331671617,
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
            "nmbe_percent": -0.4745392923747686,
            "cvrmse_percent": 55.066346347292445,
            "rms_normalized_rmse_percent": 5.367952622285893,
            "reference_energy": 0.9220970017774981,
            "candidate_energy": 0.9177212891902542,
            "relative_energy_error_percent": 0.47453929237476855,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2963094064843972e-07,
              "p90": 2.2394422558136284e-05,
              "p95": 3.907804534719609e-05,
              "p99": 9.99073963612318e-05,
              "maximum": 0.0007016616873443127
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004770441446453333,
              "candidate": 0.00406877975910902,
              "position": [
                4.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.26792361152130506,
            "cvrmse_percent": 32.76290445669651,
            "rms_normalized_rmse_percent": 5.363253582254504,
            "reference_energy": 1.5484605095004529,
            "candidate_energy": 1.544311818180418,
            "relative_energy_error_percent": 0.26792361152130506,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2963094064843972e-07,
              "p90": 2.2325622012431268e-05,
              "p95": 3.8912183117645304e-05,
              "p99": 9.980404865927994e-05,
              "maximum": 0.0007016616873443127
            },
            "worst": {
              "global_sensor_index": 45,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.004770441446453333,
              "candidate": 0.00406877975910902,
              "position": [
                4.5,
                5.5,
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
            "nmbe_percent": 0.758202394273629,
            "cvrmse_percent": 229.7514699744507,
            "rms_normalized_rmse_percent": 20.6513878077071,
            "reference_energy": 0.03219745788161532,
            "candidate_energy": 0.03244157977816897,
            "relative_energy_error_percent": 0.7582023942736291,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.0323641365393996e-06,
              "p95": 4.466194342001013e-06,
              "p99": 1.731849283714837e-05,
              "maximum": 0.00016462994972243905
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007712800288572907,
              "candidate": 0.0009359099785797298,
              "position": [
                6.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.6816655776672399,
            "cvrmse_percent": 202.31611957427307,
            "rms_normalized_rmse_percent": 20.603827744364175,
            "reference_energy": 0.03647943169404755,
            "candidate_energy": 0.036728099422834504,
            "relative_energy_error_percent": 0.6816655776672399,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.0323641365393996e-06,
              "p95": 4.466194342001013e-06,
              "p99": 1.7684404156170785e-05,
              "maximum": 0.00016462994972243905
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0007712800288572907,
              "candidate": 0.0009359099785797298,
              "position": [
                6.5,
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
            "nmbe_percent": -0.4318298612986613,
            "cvrmse_percent": 2.779017156854135,
            "rms_normalized_rmse_percent": 1.018826911567272,
            "reference_energy": 11.024760670794194,
            "candidate_energy": 10.977152462080994,
            "relative_energy_error_percent": 0.4318298612986613,
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
            "nmbe_percent": 68.90491313468338,
            "cvrmse_percent": 404.58118582935873,
            "rms_normalized_rmse_percent": 29.48455577031209,
            "reference_energy": 3.3350771449468937,
            "candidate_energy": 5.633109154647229,
            "relative_energy_error_percent": 68.90491313468338,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.845069260132732e-06,
              "p90": 0.000523824692936614,
              "p95": 0.0006829367484897375,
              "p99": 0.001116409432142973,
              "maximum": 0.025550462305545807
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0449753999710083,
              "candidate": 0.07052586227655411,
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
            "nmbe_percent": 15.67165193551314,
            "cvrmse_percent": 93.94039126255296,
            "rms_normalized_rmse_percent": 29.477111299820017,
            "reference_energy": 14.359837815741088,
            "candidate_energy": 16.610261616728224,
            "relative_energy_error_percent": 15.671651935513138,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0005216250511239192,
              "p95": 0.0006809513215557672,
              "p99": 0.0011169523932039738,
              "maximum": 0.025550462305545807
            },
            "worst": {
              "global_sensor_index": 0,
              "local_sensor_index": 0,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0449753999710083,
              "candidate": 0.07052586227655411,
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
            "nmbe_percent": 0.036244331671617,
            "cvrmse_percent": 5.7768589037582965,
            "rms_normalized_rmse_percent": 0.831203649128976,
            "reference_energy": 0.6263635077229548,
            "candidate_energy": 0.6265905289901639,
            "relative_energy_error_percent": 0.036244331671617,
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
            "nmbe_percent": 104.98722142122664,
            "cvrmse_percent": 631.1822555750484,
            "rms_normalized_rmse_percent": 40.05924158091783,
            "reference_energy": 0.44769682852787973,
            "candidate_energy": 0.9177212891902542,
            "relative_energy_error_percent": 104.98722142122665,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.8049998187925667e-05,
              "p95": 0.00010682609745344952,
              "p99": 0.0003123203059658408,
              "maximum": 0.004020237363874912
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011132022365927696,
              "candidate": 0.015152259729802608,
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
            "nmbe_percent": 43.782594520813,
            "cvrmse_percent": 263.11699522378655,
            "rms_normalized_rmse_percent": 40.062818882204375,
            "reference_energy": 1.0740603362508345,
            "candidate_energy": 1.544311818180418,
            "relative_energy_error_percent": 43.782594520813,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.763999797636643e-05,
              "p95": 0.00010563149917288679,
              "p99": 0.0003211192088201642,
              "maximum": 0.004020237363874912
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 23,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011132022365927696,
              "candidate": 0.015152259729802608,
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
            "nmbe_percent": 192.08509408293654,
            "cvrmse_percent": 1631.168846290917,
            "rms_normalized_rmse_percent": 77.37991111300394,
            "reference_energy": 0.011106893311357169,
            "candidate_energy": 0.03244157977816897,
            "relative_energy_error_percent": 192.08509408293654,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.250244718510658e-07,
              "p95": 4.430740611383024e-06,
              "p99": 2.7950000003329478e-05,
              "maximum": 0.0004969224974047393
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00043898748117499053,
              "candidate": 0.0009359099785797298,
              "position": [
                6.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 138.6666875955875,
            "cvrmse_percent": 1177.227317173701,
            "rms_normalized_rmse_percent": 77.37553928792529,
            "reference_energy": 0.015388867123789396,
            "candidate_energy": 0.036728099422834504,
            "relative_energy_error_percent": 138.66668759558746,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.250244718510658e-07,
              "p95": 4.430740611383024e-06,
              "p99": 2.8892272894154303e-05,
              "maximum": 0.0004969224974047393
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00043898748117499053,
              "candidate": 0.0009359099785797298,
              "position": [
                6.5,
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
      "bias_percent": -0.1254147156547215,
      "rms_normalized_error_percent": 0.43722024780643326,
      "absolute_error": {
        "p95": 0.18751159994998368,
        "p99": 0.4868467912468686,
        "maximum": 0.561574751014188
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 9.109689786434167,
      "rms_normalized_to_uniform_percent": 0.43722024780643326
    },
    "overcast": {
      "bias_percent": -0.0760950952220341,
      "rms_normalized_error_percent": 0.3187855313058632,
      "absolute_error": {
        "p95": 0.10410861968994134,
        "p99": 0.22849538803100583,
        "maximum": 0.29215145111083984
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.922847270965576,
      "rms_normalized_to_uniform_percent": 0.22109176580606577
    },
    "horizon": {
      "bias_percent": 0.21581391834948577,
      "rms_normalized_error_percent": 2.425857346577049,
      "absolute_error": {
        "p95": 0.07808331151711044,
        "p99": 0.11491241915144819,
        "maximum": 0.13373245923576293
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.7789560212461423,
      "rms_normalized_to_uniform_percent": 0.15069052647071707
    },
    "north": {
      "bias_percent": -95.48363494435114,
      "rms_normalized_error_percent": 99.96589286162285,
      "absolute_error": {
        "p95": 7.595796960231378e-05,
        "p99": 0.00020795628879568525,
        "maximum": 0.0004192057822365314
      },
      "worst_index": [
        82
      ],
      "passed": true,
      "physically_near_zero": true,
      "reference_mean": 1.76221856236225e-05,
      "rms_normalized_to_uniform_percent": 0.00023626462451044585
    },
    "east": {
      "bias_percent": -0.12985479089216262,
      "rms_normalized_error_percent": 0.6194988983523286,
      "absolute_error": {
        "p95": 0.0766476035118103,
        "p99": 0.13172523498535155,
        "maximum": 0.1395101547241211
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.8548418283462524,
      "rms_normalized_to_uniform_percent": 0.13501667840341397
    },
    "south": {
      "bias_percent": -0.17756843847068898,
      "rms_normalized_error_percent": 0.5856535859593054,
      "absolute_error": {
        "p95": 0.1396631240844726,
        "p99": 0.42899471282958984,
        "maximum": 0.45767974853515625
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 6.178340435028076,
      "rms_normalized_to_uniform_percent": 0.3756952395127679
    },
    "west": {
      "bias_percent": -0.16758895406591842,
      "rms_normalized_error_percent": 0.5209589324871188,
      "absolute_error": {
        "p95": 0.06312813758850094,
        "p99": 0.09500364780426024,
        "maximum": 0.1147456169128418
      },
      "worst_index": [
        9
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 1.7940126657485962,
      "rms_normalized_to_uniform_percent": 0.10904028033902034
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
          "nmbe_percent": -0.16804040457975966,
          "cvrmse_percent": 1.6060571526788552,
          "absolute_error_percentiles_lux": {
            "p50": 10.2750244140625,
            "p90": 84.79716796875002,
            "p95": 127.98266601562504,
            "p99": 250.43789550781253
          },
          "maximum_absolute_error_lux": 807.8447265625,
          "worst": {
            "sensor_index": 9,
            "position": [
              3.5,
              2.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 15817.4404296875,
            "radiance_lux": 16625.28515625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.07547184170472024,
            "maximum_error_percentage_points": 0.3336986301369791,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.035454575681594096,
            "maximum_error_percentage_points": 0.14079702473115674,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.025357686453577166,
            "maximum_error_percentage_points": 0.11123287671232873,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.19547945205479542,
            "maximum_error_percentage_points": 0.5200000000000031,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.19840182648401822,
            "maximum_error_percentage_points": 0.5198630136986253,
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
          "nmbe_percent": -0.05117248413940071,
          "cvrmse_percent": 9.234826595712654,
          "absolute_error_percentiles_lux": {
            "p50": 1.720083236694336,
            "p90": 15.098374176025391,
            "p95": 23.333047866821264,
            "p99": 47.16122314453116
          },
          "maximum_absolute_error_lux": 200.0809326171875,
          "worst": {
            "sensor_index": 24,
            "position": [
              4.5,
              8.5,
              0.75
            ],
            "hour_of_year": 349.5,
            "foton_lux": 1383.61328125,
            "radiance_lux": 1183.5323486328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.27616818873668186,
            "maximum_error_percentage_points": 1.070547945205476,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.6624177538936225,
            "maximum_error_percentage_points": 2.0281723972107564,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 1.7126750380517508,
            "maximum_error_percentage_points": 5.2908219178082305,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 1.7159817351598168,
            "maximum_error_percentage_points": 5.29082191780822,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.006666666666666684,
            "maximum_error_percentage_points": 0.11150684931506882,
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
          "nmbe_percent": -0.027556942443149986,
          "cvrmse_percent": 68.43127157742259,
          "absolute_error_percentiles_lux": {
            "p50": 0.15945404767990112,
            "p90": 1.5671807169914258,
            "p95": 2.767641568183897,
            "p99": 6.829697360992422
          },
          "maximum_absolute_error_lux": 32.100409507751465,
          "worst": {
            "sensor_index": 9,
            "position": [
              7.5,
              5.5,
              0.75
            ],
            "hour_of_year": 1859.5,
            "foton_lux": 40.54688262939453,
            "radiance_lux": 8.446473121643066
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
            "mean_absolute_error_percentage_points": 0.11629378299555067,
            "maximum_error_percentage_points": 0.4675489874127998,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.005536529680365653,
            "maximum_error_percentage_points": 0.11260273972602874,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0055365296803652955,
            "maximum_error_percentage_points": 0.11260273972602741,
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
      "maximum_error_percentage_points": 0.004977258133561646,
      "metrics": {
        "da": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
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
            "maximum_error_percentage_points": 0.004968964041097479,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_office_grid",
            "maximum_error_percentage_points": 0.004935787671232816,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.004977258133561646,
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
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.003972602739725994,
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
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "glazed_corridor_meeting_grid",
            "maximum_error_percentage_points": 0.00397260273972222,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "glazed_corridor_corridor_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
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
      "study_preparation_seconds": 0.0631577919702977,
      "weather_seconds": 0.15789362497162074,
      "metric_reduction_seconds": 0.04999700002372265,
      "write_seconds": 0.055257583037018776,
      "total_seconds": 0.2639405410736799,
      "cold_end_to_end_seconds": 0.3270983330439776,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02408125007059425,
      "engine_upload_seconds": 0.000299209,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0326242916053161,
      "engine_annual_reduction_seconds": 0.0007266249740496278,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0326242916053161
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0631577919702977,
      "weather_seconds": 0.10219537501689047,
      "metric_reduction_seconds": 0.013283416978083551,
      "write_seconds": 0.038594083045609295,
      "total_seconds": 0.15458962495904416,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.15458962495904416,
      "raw_export_seconds": 0.022882083081640303,
      "engine_upload_seconds": 6.8375e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0007518333150073886,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.02148304204456508,
      "full": 0.02197516697924584
    }
  },
  "elapsed_seconds": 418.2300095829414,
  "result_class": "unstable_reference"
}
```
