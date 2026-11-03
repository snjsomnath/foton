# Foton report

Status: **passed**

```json
{
  "scene": "courtyard_rooms",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "courtyard_rooms",
    "category": "connections",
    "question": "Do four inward-facing rooms shade one another beneath a pergola?",
    "interactions": [
      "multiroom_context",
      "courtyard",
      "combined_shading"
    ],
    "room_count": 4,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 4,
    "apertures": 4,
    "shades": 4,
    "sensors": 112,
    "floor_area": 112.0,
    "aperture_area": 17.999999999999996
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "2ef815d189cb6f9f1f804d12e4734e55b6b81cd9f61669b712af2479848522a5",
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
      "scene_fingerprint": 16353448696249269853,
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
      "scene_fingerprint": 16353448696249269853,
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
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": 0.15600976097374,
        "rms_normalized_error_percent": 2.6080787081247703,
        "absolute_error": {
          "p95": 5.2641611546278e-05,
          "p99": 0.00025876224972307723,
          "maximum": 0.0006226329132914543
        },
        "worst_index": [
          20,
          64,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": -0.006315200969938644,
        "rms_normalized_error_percent": 2.750563276963437,
        "absolute_error": {
          "p95": 6.438465788960457e-05,
          "p99": 0.0002754469634965063,
          "maximum": 0.0006568883545696735
        },
        "worst_index": [
          4,
          56,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": -0.052938446660532275,
        "rms_normalized_error_percent": 2.9311502537615928,
        "absolute_error": {
          "p95": 6.779102113796398e-05,
          "p99": 0.0003074812702834606,
          "maximum": 0.0009097978472709656
        },
        "worst_index": [
          11,
          119,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": -0.2635397675840732,
        "rms_normalized_error_percent": 2.729739719298592,
        "absolute_error": {
          "p95": 8.244859054684639e-05,
          "p99": 0.0002848142758011818,
          "maximum": 0.000855528749525547
        },
        "worst_index": [
          8,
          64,
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
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": 0.19775355251046012,
        "rms_normalized_error_percent": 1.153873242036245,
        "absolute_error": {
          "p95": 5.5256299674510956e-05,
          "p99": 0.00016152281314134773,
          "maximum": 0.001015692949295044
        },
        "worst_index": [
          28,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": 0.06749982533483248,
        "rms_normalized_error_percent": 1.0718366483436759,
        "absolute_error": {
          "p95": 5.5282784160226583e-05,
          "p99": 0.00017113954527303647,
          "maximum": 0.0004891045391559601
        },
        "worst_index": [
          21,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": 0.05461107917803694,
        "rms_normalized_error_percent": 1.1210447937805432,
        "absolute_error": {
          "p95": 7.503200322389603e-05,
          "p99": 0.00020996714010834694,
          "maximum": 0.00066341832280159
        },
        "worst_index": [
          11,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": 0.10571853617547079,
        "rms_normalized_error_percent": 1.033744961336022,
        "absolute_error": {
          "p95": 7.461663335561752e-05,
          "p99": 0.0001806570217013359,
          "maximum": 0.0005846470594406128
        },
        "worst_index": [
          11,
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
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": -0.13208832371539145,
        "rms_normalized_error_percent": 0.8670465601251272,
        "absolute_error": {
          "p95": 4.625367000699043e-05,
          "p99": 0.00013371488312259347,
          "maximum": 0.00043338164687156677
        },
        "worst_index": [
          13,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": -0.0010733034339510572,
        "rms_normalized_error_percent": 0.8142007893296643,
        "absolute_error": {
          "p95": 4.486337275011465e-05,
          "p99": 0.00012751030735671563,
          "maximum": 0.0003674030303955078
        },
        "worst_index": [
          20,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": 0.01977319224699001,
        "rms_normalized_error_percent": 0.9349264096617129,
        "absolute_error": {
          "p95": 5.853921175003052e-05,
          "p99": 0.00016352208331227303,
          "maximum": 0.0007237344980239868
        },
        "worst_index": [
          11,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": -0.04820307159908049,
        "rms_normalized_error_percent": 0.8405567489297721,
        "absolute_error": {
          "p95": 5.8582983911037445e-05,
          "p99": 0.0001470819115638733,
          "maximum": 0.0006262026727199554
        },
        "worst_index": [
          17,
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.14375678205223627,
                "cvrmse_percent": 17.02149058785288,
                "rms_normalized_rmse_percent": 3.6791515955769913,
                "reference_energy": 5.71823661205579,
                "candidate_energy": 5.726456964999414,
                "relative_energy_error_percent": 0.14375678205223624,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.75250999443233e-07,
                  "p95": 8.812930173007771e-05,
                  "p99": 0.0003847516141831893,
                  "maximum": 0.0009744446724653244
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 70,
                  "rgb_channel": 0,
                  "reference": 0.009965100325644016,
                  "candidate": 0.01093954499810934
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.26481576104388316,
                "cvrmse_percent": 54.22910993704348,
                "rms_normalized_rmse_percent": 3.374977053526285,
                "reference_energy": 2.411908818069712,
                "candidate_energy": 2.405521703377456,
                "relative_energy_error_percent": 0.26481576104388316,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4030409829501878e-06,
                  "p90": 5.9396334108896554e-05,
                  "p95": 0.00013139750808477402,
                  "p99": 0.0005359944654628645,
                  "maximum": 0.001040888950228691
                },
                "worst": {
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04029346443712711,
                  "candidate": 0.03925257548689842
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.379867270146701,
                "cvrmse_percent": 14.250335097223335,
                "rms_normalized_rmse_percent": 3.086792998884555,
                "reference_energy": 5.74551756807422,
                "candidate_energy": 5.723692227332577,
                "relative_energy_error_percent": 0.37986727014670096,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.3559134610404726e-07,
                  "p95": 8.211573003791273e-05,
                  "p99": 0.00031373099773190975,
                  "maximum": 0.0007089173886924982
                },
                "worst": {
                  "global_sensor_index": 49,
                  "local_sensor_index": 17,
                  "sky_patch_index": 50,
                  "rgb_channel": 0,
                  "reference": 0.005139387445524335,
                  "candidate": 0.005848304834216833
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.9674228272002375,
                "cvrmse_percent": 55.86383917942769,
                "rms_normalized_rmse_percent": 3.437684838961469,
                "reference_energy": 2.3822987977916306,
                "candidate_energy": 2.4053457001735836,
                "relative_energy_error_percent": 0.9674228272002374,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.789210035800352e-06,
                  "p90": 6.772109918529168e-05,
                  "p95": 0.0001604688004590571,
                  "p99": 0.0004875813610851769,
                  "maximum": 0.001125674694776535
                },
                "worst": {
                  "global_sensor_index": 52,
                  "local_sensor_index": 20,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03277553990483284,
                  "candidate": 0.031649865210056305
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.07768204031858644,
                "cvrmse_percent": 15.636127110056938,
                "rms_normalized_rmse_percent": 3.811311650082578,
                "reference_energy": 5.345440521411604,
                "candidate_energy": 5.341288074150555,
                "relative_energy_error_percent": 0.07768204031858644,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.378520305996062e-06,
                  "p95": 0.00013418053276836872,
                  "p99": 0.0004241541028022766,
                  "maximum": 0.0008547243196517229
                },
                "worst": {
                  "global_sensor_index": 70,
                  "local_sensor_index": 6,
                  "sky_patch_index": 43,
                  "rgb_channel": 0,
                  "reference": 0.004841115325689316,
                  "candidate": 0.003986391006037593
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.7751951344034782,
                "cvrmse_percent": 57.694657507981994,
                "rms_normalized_rmse_percent": 3.964861917131872,
                "reference_energy": 2.268696054097326,
                "candidate_energy": 2.286282875523092,
                "relative_energy_error_percent": 0.7751951344034783,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.7409857889560953e-05,
                  "p90": 8.667591779953909e-05,
                  "p95": 0.00021633147116517648,
                  "p99": 0.0006858254782855511,
                  "maximum": 0.0017075557261705399
                },
                "worst": {
                  "global_sensor_index": 79,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04526098445057869,
                  "candidate": 0.04696854017674923
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.20315965103784167,
                "cvrmse_percent": 14.51060834974644,
                "rms_normalized_rmse_percent": 3.4832810751308565,
                "reference_energy": 5.361944943689224,
                "candidate_energy": 5.372838252325664,
                "relative_energy_error_percent": 0.2031596510378417,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 8.400804290431552e-06,
                  "p95": 0.00013267050962895155,
                  "p99": 0.0004040489438921213,
                  "maximum": 0.0010153180919587612
                },
                "worst": {
                  "global_sensor_index": 93,
                  "local_sensor_index": 5,
                  "sky_patch_index": 64,
                  "rgb_channel": 0,
                  "reference": 0.009563216473907232,
                  "candidate": 0.010578534565865993
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.2672516651720545,
                "cvrmse_percent": 57.27815117653152,
                "rms_normalized_rmse_percent": 3.8175925662291252,
                "reference_energy": 2.176016374643268,
                "candidate_energy": 2.181831814638919,
                "relative_energy_error_percent": 0.2672516651720545,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.6583282103965757e-05,
                  "p90": 8.376756886718795e-05,
                  "p95": 0.0002090164925903082,
                  "p99": 0.0006007639167364687,
                  "maximum": 0.0015980047173798084
                },
                "worst": {
                  "global_sensor_index": 100,
                  "local_sensor_index": 12,
                  "sky_patch_index": 86,
                  "rgb_channel": 0,
                  "reference": -0.0009578000754117966,
                  "candidate": 0.0006402046419680119
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 173.91483299434185,
            "full": 544.3919169483706
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 176.98862496763468,
            "full": 547.8139169281349
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 173.00583410542458,
            "full": 539.1872090985999
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 186.47654203232378,
            "full": 551.5972920693457
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.028811653979509903,
                "cvrmse_percent": 8.62044784663083,
                "rms_normalized_rmse_percent": 1.864912077280085,
                "reference_energy": 5.729494433524948,
                "candidate_energy": 5.731145195635911,
                "relative_energy_error_percent": 0.028811653979509907,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.055462679592893e-07,
                  "p95": 4.4513813918456435e-05,
                  "p99": 0.00019215263309888675,
                  "maximum": 0.0004411174450069666
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 38,
                  "rgb_channel": 0,
                  "reference": 0.005373172927647829,
                  "candidate": 0.0049320554826408625
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.1823020571213935,
                "cvrmse_percent": 19.594131557498766,
                "rms_normalized_rmse_percent": 1.7859223066610965,
                "reference_energy": 4.3765522320136725,
                "candidate_energy": 4.368573687263719,
                "relative_energy_error_percent": 0.1823020571213935,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.130719556385884e-05,
                  "p90": 5.022892582928762e-05,
                  "p95": 9.332236368209124e-05,
                  "p99": 0.0003000146563863392,
                  "maximum": 0.000697009265422821
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 65,
                  "rgb_channel": 0,
                  "reference": 0.0007335124537348747,
                  "candidate": 3.650318831205368e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.000756582458245875,
                "cvrmse_percent": 8.490743832331846,
                "rms_normalized_rmse_percent": 1.83777162578393,
                "reference_energy": 5.729252468247395,
                "candidate_energy": 5.729295814766559,
                "relative_energy_error_percent": 0.0007565824582458751,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.1446688808500767e-07,
                  "p95": 4.4859014451503754e-05,
                  "p99": 0.00018639638146851216,
                  "maximum": 0.0004193955101072788
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 3,
                  "sky_patch_index": 77,
                  "rgb_channel": 0,
                  "reference": 0.010445894673466682,
                  "candidate": 0.010865290183573961
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.23219985551117933,
                "cvrmse_percent": 19.309047254139234,
                "rms_normalized_rmse_percent": 1.763316990688129,
                "reference_energy": 4.3794741654381255,
                "candidate_energy": 4.389643298122422,
                "relative_energy_error_percent": 0.23219985551117936,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.1119324426545063e-05,
                  "p90": 5.011943994759349e-05,
                  "p95": 8.982251165434718e-05,
                  "p99": 0.0003085527830990034,
                  "maximum": 0.0008406303822994232
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05262545496225357,
                  "candidate": 0.053466085344552994
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.015443672548260828,
                "cvrmse_percent": 9.629362783822673,
                "rms_normalized_rmse_percent": 2.3480107430290715,
                "reference_energy": 5.359095515094943,
                "candidate_energy": 5.358267873932043,
                "relative_energy_error_percent": 0.015443672548260828,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.685510132025229e-06,
                  "p95": 7.11916945874691e-05,
                  "p99": 0.00023099291138350964,
                  "maximum": 0.0006418789271265268
                },
                "worst": {
                  "global_sensor_index": 80,
                  "local_sensor_index": 16,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.004931722534820437,
                  "candidate": 0.004289843607693911
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.013466347659178889,
                "cvrmse_percent": 20.083579716485133,
                "rms_normalized_rmse_percent": 1.9540039728161733,
                "reference_energy": 4.124502861844313,
                "candidate_energy": 4.123947441949724,
                "relative_energy_error_percent": 0.013466347659178887,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4171137763696606e-05,
                  "p90": 6.463136469392339e-05,
                  "p95": 0.00012524821795523167,
                  "p99": 0.00039944727905094624,
                  "maximum": 0.001097157597541809
                },
                "worst": {
                  "global_sensor_index": 66,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03436625376343727,
                  "candidate": 0.03326909616589546
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05658961245998713,
                "cvrmse_percent": 8.33375066311533,
                "rms_normalized_rmse_percent": 1.9983848047255233,
                "reference_energy": 5.347737802765934,
                "candidate_energy": 5.350764066863896,
                "relative_energy_error_percent": 0.05658961245998713,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.097492587286979e-06,
                  "p95": 7.008442116784863e-05,
                  "p99": 0.00022117514163255692,
                  "maximum": 0.0005130055360496044
                },
                "worst": {
                  "global_sensor_index": 100,
                  "local_sensor_index": 12,
                  "sky_patch_index": 31,
                  "rgb_channel": 0,
                  "reference": 0.005076173925772309,
                  "candidate": 0.005589179461821914
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.1854299575941695,
                "cvrmse_percent": 19.356200246743608,
                "rms_normalized_rmse_percent": 1.8832886557749668,
                "reference_energy": 4.075663416182621,
                "candidate_energy": 4.08322091712693,
                "relative_energy_error_percent": 0.1854299575941695,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4035484127816744e-05,
                  "p90": 6.031567772879498e-05,
                  "p95": 0.00011042431287933141,
                  "p99": 0.000381669495254755,
                  "maximum": 0.0011267699301242828
                },
                "worst": {
                  "global_sensor_index": 96,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0596638098359108,
                  "candidate": 0.058537039905786514
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 265.68491698708385,
            "full": 7410.062624956481
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 284.95425009168684,
            "full": 7398.624583031051
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 285.74366704560816,
            "full": 7465.450625051744
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 269.2602910101414,
            "full": 7446.3720000348985
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.09082760135969706,
                "cvrmse_percent": 8.799101275978277,
                "rms_normalized_rmse_percent": 1.9042839880723992,
                "reference_energy": 5.729812548899503,
                "candidate_energy": 5.72460829759893,
                "relative_energy_error_percent": 0.09082760135969707,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.0042739404525491e-06,
                  "p95": 4.614901263266802e-05,
                  "p99": 0.00019695658447744802,
                  "maximum": 0.0005550910718739033
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "sky_patch_index": 64,
                  "rgb_channel": 0,
                  "reference": 0.009009032975882292,
                  "candidate": 0.009564124047756195
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.03718927936527066,
                "cvrmse_percent": 19.68445996525426,
                "rms_normalized_rmse_percent": 1.7990563230252898,
                "reference_energy": 4.394833977242655,
                "candidate_energy": 4.396468384328092,
                "relative_energy_error_percent": 0.03718927936527066,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.119213629863225e-05,
                  "p90": 4.907466791337356e-05,
                  "p95": 9.749422315508127e-05,
                  "p99": 0.00031181618105620207,
                  "maximum": 0.0007942859083414078
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04188333451747894,
                  "candidate": 0.041089048609137535
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.10793180786624387,
                "cvrmse_percent": 9.3595668180552,
                "rms_normalized_rmse_percent": 2.024116543263583,
                "reference_energy": 5.72767267379534,
                "candidate_energy": 5.7214906931298515,
                "relative_energy_error_percent": 0.1079318078662439,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.658956408500671e-07,
                  "p95": 4.673143848776817e-05,
                  "p99": 0.0001998209801968194,
                  "maximum": 0.0005472195334732533
                },
                "worst": {
                  "global_sensor_index": 43,
                  "local_sensor_index": 11,
                  "sky_patch_index": 76,
                  "rgb_channel": 0,
                  "reference": 0.009094334673136473,
                  "candidate": 0.009641554206609726
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.14761496013312364,
                "cvrmse_percent": 19.97482961837496,
                "rms_normalized_rmse_percent": 1.8296928863052606,
                "reference_energy": 4.392835806536702,
                "candidate_energy": 4.399320289361235,
                "relative_energy_error_percent": 0.14761496013312364,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.1506519967952045e-05,
                  "p90": 5.0918906708830036e-05,
                  "p95": 0.00010096002370119095,
                  "p99": 0.0002862833993276585,
                  "maximum": 0.0010092854499816895
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 4,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05222273990511894,
                  "candidate": 0.05323202535510063
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.10092690503666586,
                "cvrmse_percent": 9.925030113872783,
                "rms_normalized_rmse_percent": 2.4203327739290867,
                "reference_energy": 5.350580352621485,
                "candidate_energy": 5.355980527772886,
                "relative_energy_error_percent": 0.10092690503666588,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.567335392697714e-06,
                  "p95": 7.926346734166145e-05,
                  "p99": 0.0002575374674052,
                  "maximum": 0.000672126654535532
                },
                "worst": {
                  "global_sensor_index": 68,
                  "local_sensor_index": 4,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.005712452344596386,
                  "candidate": 0.005040325690060854
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.22377834633305937,
                "cvrmse_percent": 18.5467700874238,
                "rms_normalized_rmse_percent": 1.8116964456709908,
                "reference_energy": 4.139436750682442,
                "candidate_energy": 4.130173587574262,
                "relative_energy_error_percent": 0.22377834633305935,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4081944925692369e-05,
                  "p90": 6.381981074810028e-05,
                  "p95": 0.00012935593258589506,
                  "p99": 0.000371866044588387,
                  "maximum": 0.0007037799805402756
                },
                "worst": {
                  "global_sensor_index": 77,
                  "local_sensor_index": 13,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04586451128125191,
                  "candidate": 0.04516073130071163
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05563489777624719,
                "cvrmse_percent": 8.409378293271564,
                "rms_normalized_rmse_percent": 2.017589654004021,
                "reference_energy": 5.354422919496564,
                "candidate_energy": 5.357401847214334,
                "relative_energy_error_percent": 0.05563489777624719,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 5.813883490191074e-06,
                  "p95": 6.933254189789295e-05,
                  "p99": 0.00023233378306031227,
                  "maximum": 0.0004646703600883484
                },
                "worst": {
                  "global_sensor_index": 103,
                  "local_sensor_index": 15,
                  "sky_patch_index": 60,
                  "rgb_channel": 0,
                  "reference": 0.006086350651457906,
                  "candidate": 0.005621680291369557
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.21748076463316715,
                "cvrmse_percent": 19.4703879375996,
                "rms_normalized_rmse_percent": 1.8999213295645956,
                "reference_energy": 4.087193035919768,
                "candidate_energy": 4.078304177253216,
                "relative_energy_error_percent": 0.21748076463316715,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4010741324455012e-05,
                  "p90": 6.065471097826958e-05,
                  "p95": 0.00011736294254660606,
                  "p99": 0.00041365552169736475,
                  "maximum": 0.0009663291275501251
                },
                "worst": {
                  "global_sensor_index": 93,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.041975636035203934,
                  "candidate": 0.04294196516275406
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 275.084541994147,
            "full": 7928.1254169764
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 275.8228749735281,
            "full": 7954.623416997492
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 269.27900000009686,
            "full": 7751.720124972053
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 267.6597499521449,
            "full": 7776.4756249962375
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.001649797556755332,
                "cvrmse_percent": 5.239109698873702,
                "rms_normalized_rmse_percent": 1.1332625848670852,
                "reference_energy": 5.724457768582063,
                "candidate_energy": 5.7243633266176595,
                "relative_energy_error_percent": 0.001649797556755332,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.839363777544349e-07,
                  "p95": 3.095483407378197e-05,
                  "p99": 0.00012580573675222815,
                  "maximum": 0.00027485424652695656
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 66,
                  "rgb_channel": 0,
                  "reference": 0.006825165823101997,
                  "candidate": 0.007100020069628954
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.007150696685725031,
                "cvrmse_percent": 12.74220780577428,
                "rms_normalized_rmse_percent": 1.1636290597947,
                "reference_energy": 4.385236730615951,
                "candidate_energy": 4.384923155638393,
                "relative_energy_error_percent": 0.007150696685725032,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.084046385192778e-06,
                  "p90": 3.416529216337949e-05,
                  "p95": 6.006609328323975e-05,
                  "p99": 0.0001942530157975853,
                  "maximum": 0.0006806142628192902
                },
                "worst": {
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05017397925257683,
                  "candidate": 0.04949336498975754
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.039798792730740086,
                "cvrmse_percent": 5.139047651292963,
                "rms_normalized_rmse_percent": 1.1119390227799137,
                "reference_energy": 5.728246589912285,
                "candidate_energy": 5.73052636289971,
                "relative_energy_error_percent": 0.039798792730740086,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.387915737424919e-07,
                  "p95": 3.154511796310544e-05,
                  "p99": 0.00011212986428290651,
                  "maximum": 0.00026648142375051975
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 5,
                  "sky_patch_index": 54,
                  "rgb_channel": 0,
                  "reference": 0.0032921750098466873,
                  "candidate": 0.003558656433597207
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.21507862144014223,
                "cvrmse_percent": 12.26954134922028,
                "rms_normalized_rmse_percent": 1.123301921080098,
                "reference_energy": 4.395891893314062,
                "candidate_energy": 4.386437269629923,
                "relative_energy_error_percent": 0.21507862144014225,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 7.983944669831544e-06,
                  "p90": 3.53462019120343e-05,
                  "p95": 5.906770456931554e-05,
                  "p99": 0.0001930693630129133,
                  "maximum": 0.0005234237760305405
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.053308019414544106,
                  "candidate": 0.052784595638513565
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.15505397050175554,
                "cvrmse_percent": 5.395759779889091,
                "rms_normalized_rmse_percent": 1.3160512172079848,
                "reference_energy": 5.347740534995523,
                "candidate_energy": 5.356032419027166,
                "relative_energy_error_percent": 0.15505397050175554,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.788907918078621e-06,
                  "p95": 4.678010009229183e-05,
                  "p99": 0.000151041429489851,
                  "maximum": 0.00035845953971147537
                },
                "worst": {
                  "global_sensor_index": 69,
                  "local_sensor_index": 5,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.0064455855172127485,
                  "candidate": 0.006804045056924224
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.29661747428931706,
                "cvrmse_percent": 12.17837551752828,
                "rms_normalized_rmse_percent": 1.1900589259886032,
                "reference_energy": 4.144221439511284,
                "candidate_energy": 4.131928954548449,
                "relative_energy_error_percent": 0.29661747428931706,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 9.6531402959954e-06,
                  "p90": 4.320134758017957e-05,
                  "p95": 8.320529013872147e-05,
                  "p99": 0.00023749517276883125,
                  "maximum": 0.00048687634989619255
                },
                "worst": {
                  "global_sensor_index": 79,
                  "local_sensor_index": 15,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.000558370491489768,
                  "candidate": 7.149414159357548e-05
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.11659036288621233,
                "cvrmse_percent": 4.926155574583324,
                "rms_normalized_rmse_percent": 1.1820973664842829,
                "reference_energy": 5.353661998326853,
                "candidate_energy": 5.3599038522784035,
                "relative_energy_error_percent": 0.11659036288621233,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.5133682558807777e-06,
                  "p95": 4.5918626710772514e-05,
                  "p99": 0.00013285060413181782,
                  "maximum": 0.0002425860147923231
                },
                "worst": {
                  "global_sensor_index": 94,
                  "local_sensor_index": 6,
                  "sky_patch_index": 32,
                  "rgb_channel": 0,
                  "reference": 0.006572761340066791,
                  "candidate": 0.0063301753252744675
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.0016185535926009332,
                "cvrmse_percent": 11.795981526618583,
                "rms_normalized_rmse_percent": 1.1493156647228846,
                "reference_energy": 4.0772953615237135,
                "candidate_energy": 4.077361354734268,
                "relative_energy_error_percent": 0.001618553592600933,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.0291154467267916e-05,
                  "p90": 4.333138349466026e-05,
                  "p95": 7.56348017603159e-05,
                  "p99": 0.00021278578788042068,
                  "maximum": 0.0006085354834794998
                },
                "worst": {
                  "global_sensor_index": 106,
                  "local_sensor_index": 18,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0392799936234951,
                  "candidate": 0.0398885291069746
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 464.3620830029249,
            "full": 13980.362917063758
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 485.89637503027916,
            "full": 13657.821125001647
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 457.75275002233684,
            "full": 13787.673041922972
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 462.77520805597305,
            "full": 13699.085082975216
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 5246.5399579377845,
      "worker_pool_size": 12,
      "invocation_count": 7
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 20139.219042030163,
      "worker_pool_size": 12,
      "invocation_count": 7
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      112,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013834637858816393,
            "cvrmse_percent": 7.8009695731736555,
            "rms_normalized_rmse_percent": 1.6874446985176825,
            "reference_energy": 5.720563088525353,
            "candidate_energy": 5.71977166933857,
            "relative_energy_error_percent": 0.013834637858816393,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3441857049656392e-07,
              "p95": 4.4327229261398315e-05,
              "p99": 0.00016583710676059215,
              "maximum": 0.0005219951272010803
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008402213454246521,
              "candidate": 0.008924208581447601,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.16802755618433932,
            "cvrmse_percent": 14.864802266343341,
            "rms_normalized_rmse_percent": 1.3598072617375652,
            "reference_energy": 4.388927399595616,
            "candidate_energy": 4.381552792143371,
            "relative_energy_error_percent": 0.1680275561843393,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.3284403394209221e-05,
              "p90": 4.9649686843622476e-05,
              "p95": 7.357978029176593e-05,
              "p99": 0.00019310000352561505,
              "maximum": 0.0007547549903392792
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04118795320391655,
              "candidate": 0.04043319821357727,
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
            "nmbe_percent": -0.08077584769107186,
            "cvrmse_percent": 5.7807893989629004,
            "rms_normalized_rmse_percent": 1.2180811947031984,
            "reference_energy": 10.109490488120969,
            "candidate_energy": 10.10132446148194,
            "relative_energy_error_percent": 0.08077584769107185,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3113093700667378e-05,
              "p90": 4.752492532134056e-05,
              "p95": 6.412414950318635e-05,
              "p99": 0.00016044070944190055,
              "maximum": 0.0007547549903392792
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04118795320391655,
              "candidate": 0.04043319821357727,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "full_identifier": "courtyard_rooms_east_grid",
        "start_sensor_index": 32,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08641747279699226,
            "cvrmse_percent": 7.714186058286733,
            "rms_normalized_rmse_percent": 1.6690328869185542,
            "reference_energy": 5.717453602238049,
            "candidate_energy": 5.712512723326654,
            "relative_energy_error_percent": 0.08641747279699226,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7066562324762344e-07,
              "p95": 4.211164923617616e-05,
              "p99": 0.00014806110411882427,
              "maximum": 0.00043502962216734886
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 10,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.005379220470786095,
              "candidate": 0.0058142500929534435,
              "position": [
                11.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.6891696678100772,
            "cvrmse_percent": 16.827531033822485,
            "rms_normalized_rmse_percent": 1.5432797603642383,
            "reference_energy": 4.4030974375391345,
            "candidate_energy": 4.372752625555492,
            "relative_energy_error_percent": 0.6891696678100772,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.3716242392547429e-05,
              "p90": 4.7651963541284204e-05,
              "p95": 6.963178748264909e-05,
              "p99": 0.00019531365251168695,
              "maximum": 0.0010974127799272537
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029604032635688782,
              "candidate": 0.028506619855761528,
              "position": [
                11.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3486538505300009,
            "cvrmse_percent": 6.987388591735932,
            "rms_normalized_rmse_percent": 1.472939877396179,
            "reference_energy": 10.120551039777183,
            "candidate_energy": 10.085265348882146,
            "relative_energy_error_percent": 0.3486538505300009,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.3550166841014288e-05,
              "p90": 4.566257121041417e-05,
              "p95": 6.637629849137738e-05,
              "p99": 0.00015652528963983086,
              "maximum": 0.0010974127799272537
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029604032635688782,
              "candidate": 0.028506619855761528,
              "position": [
                11.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "full_identifier": "courtyard_rooms_north_grid",
        "start_sensor_index": 64,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.3821225108837679,
            "cvrmse_percent": 6.386477548129004,
            "rms_normalized_rmse_percent": 1.5580886651593073,
            "reference_energy": 5.366319870222696,
            "candidate_energy": 5.345813953992547,
            "relative_energy_error_percent": 0.3821225108837679,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.835232049226761e-06,
              "p95": 5.678832530975342e-05,
              "p99": 0.00016435328871011734,
              "maximum": 0.0003651715815067291
            },
            "worst": {
              "global_sensor_index": 82,
              "local_sensor_index": 18,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.008710086345672607,
              "candidate": 0.009075257927179337,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.6718297102070195,
            "cvrmse_percent": 18.492060985096572,
            "rms_normalized_rmse_percent": 1.7987673870363292,
            "reference_energy": 4.123641816791178,
            "candidate_energy": 4.095937965923454,
            "relative_energy_error_percent": 0.6718297102070195,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.5974814232322387e-05,
              "p90": 5.743935616919771e-05,
              "p95": 8.927888120524585e-05,
              "p99": 0.00022201472893357277,
              "maximum": 0.0014107301831245422
            },
            "worst": {
              "global_sensor_index": 79,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.058588530868291855,
              "candidate": 0.05717780068516731,
              "position": [
                7.5,
                8.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5080080266693144,
            "cvrmse_percent": 7.7178924853240005,
            "rms_normalized_rmse_percent": 1.7277143332914644,
            "reference_energy": 9.489961687013874,
            "candidate_energy": 9.441751919916001,
            "relative_energy_error_percent": 0.5080080266693144,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5775731299072504e-05,
              "p90": 5.676255386788398e-05,
              "p95": 7.892919529695064e-05,
              "p99": 0.00020378222689032555,
              "maximum": 0.0014107301831245422
            },
            "worst": {
              "global_sensor_index": 79,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.058588530868291855,
              "candidate": 0.05717780068516731,
              "position": [
                7.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "full_identifier": "courtyard_rooms_south_grid",
        "start_sensor_index": 88,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2276783952661703,
            "cvrmse_percent": 5.926218621798515,
            "rms_normalized_rmse_percent": 1.4217865934738816,
            "reference_energy": 5.3559874540273995,
            "candidate_energy": 5.3437930277414125,
            "relative_energy_error_percent": 0.22767839526617026,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.64267349243164e-06,
              "p95": 5.051555490354076e-05,
              "p99": 0.0001460714265704155,
              "maximum": 0.0003647543489933014
            },
            "worst": {
              "global_sensor_index": 92,
              "local_sensor_index": 4,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008932281285524368,
              "candidate": 0.00929703563451767,
              "position": [
                5.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.4690790649641675,
            "cvrmse_percent": 14.198567898005802,
            "rms_normalized_rmse_percent": 1.3827497485997373,
            "reference_energy": 4.078123799341483,
            "candidate_energy": 4.097253424327516,
            "relative_energy_error_percent": 0.46907906496416746,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.514541327196639e-05,
              "p90": 5.871399480383843e-05,
              "p95": 8.914800127968192e-05,
              "p99": 0.00022498471662402153,
              "maximum": 0.0010032877326011658
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03621876239776611,
              "candidate": 0.03722205013036728,
              "position": [
                6.5,
                -3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.07351194525683263,
            "cvrmse_percent": 5.686139075689222,
            "rms_normalized_rmse_percent": 1.2810235426916006,
            "reference_energy": 9.434111253368883,
            "candidate_energy": 9.441046452068928,
            "relative_energy_error_percent": 0.07351194525683263,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.5004059605416842e-05,
              "p90": 5.582661833614111e-05,
              "p95": 8.464278653264046e-05,
              "p99": 0.0001981481909751892,
              "maximum": 0.0010032877326011658
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03621876239776611,
              "candidate": 0.03722205013036728,
              "position": [
                6.5,
                -3.5,
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
      112,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.013834637858816393,
            "cvrmse_percent": 7.8009695731736555,
            "rms_normalized_rmse_percent": 1.6874446985176825,
            "reference_energy": 5.720563088525353,
            "candidate_energy": 5.71977166933857,
            "relative_energy_error_percent": 0.013834637858816393,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.3441857049656392e-07,
              "p95": 4.4327229261398315e-05,
              "p99": 0.00016583710676059215,
              "maximum": 0.0005219951272010803
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008402213454246521,
              "candidate": 0.008924208581447601,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.76953910953678,
            "cvrmse_percent": 499.6057120444106,
            "rms_normalized_rmse_percent": 31.07749710172106,
            "reference_energy": 2.4104989282626654,
            "candidate_energy": 4.381552792143371,
            "relative_energy_error_percent": 81.76953910953678,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.632284278864972e-05,
              "p90": 0.00022044000877485814,
              "p95": 0.0003199340561650388,
              "p99": 0.0005476604666910136,
              "maximum": 0.013894692063331604
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02070508897304535,
              "candidate": 0.03459978103637695,
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
            "nmbe_percent": 24.231305094291084,
            "cvrmse_percent": 148.10000181454015,
            "rms_normalized_rmse_percent": 31.075207279639574,
            "reference_energy": 8.131062016788018,
            "candidate_energy": 10.10132446148194,
            "relative_energy_error_percent": 24.231305094291084,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.561148923836299e-05,
              "p90": 0.00022061389699956635,
              "p95": 0.00031860731542110443,
              "p99": 0.0005745709611801516,
              "maximum": 0.013894692063331604
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02070508897304535,
              "candidate": 0.03459978103637695,
              "position": [
                0.5,
                4.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "full_identifier": "courtyard_rooms_east_grid",
        "start_sensor_index": 32,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.08641747279699226,
            "cvrmse_percent": 7.714186058286733,
            "rms_normalized_rmse_percent": 1.6690328869185542,
            "reference_energy": 5.717453602238049,
            "candidate_energy": 5.712512723326654,
            "relative_energy_error_percent": 0.08641747279699226,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.7066562324762344e-07,
              "p95": 4.211164923617616e-05,
              "p99": 0.00014806110411882427,
              "maximum": 0.00043502962216734886
            },
            "worst": {
              "global_sensor_index": 42,
              "local_sensor_index": 10,
              "sky_patch_index": 102,
              "rgb_channel": 0,
              "reference": 0.005379220470786095,
              "candidate": 0.0058142500929534435,
              "position": [
                11.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.36875083358507,
            "cvrmse_percent": 493.9345647094644,
            "rms_normalized_rmse_percent": 30.76632108218619,
            "reference_energy": 2.4109735582662264,
            "candidate_energy": 4.372752625555492,
            "relative_energy_error_percent": 81.36875083358507,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.6752289531705173e-05,
              "p90": 0.00021943000319879502,
              "p95": 0.0003158915787935257,
              "p99": 0.0005355472184248814,
              "maximum": 0.013603977859020233
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021172720938920975,
              "candidate": 0.03477669879794121,
              "position": [
                13.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.074007796810616,
            "cvrmse_percent": 146.53328207576877,
            "rms_normalized_rmse_percent": 30.772054839828996,
            "reference_energy": 8.128427160504275,
            "candidate_energy": 10.085265348882146,
            "relative_energy_error_percent": 24.074007796810616,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.5839611882693134e-05,
              "p90": 0.00022195999918039888,
              "p95": 0.00031388000934384763,
              "p99": 0.0005597163923084748,
              "maximum": 0.013603977859020233
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021172720938920975,
              "candidate": 0.03477669879794121,
              "position": [
                13.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "full_identifier": "courtyard_rooms_north_grid",
        "start_sensor_index": 64,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.3821225108837679,
            "cvrmse_percent": 6.386477548129004,
            "rms_normalized_rmse_percent": 1.5580886651593073,
            "reference_energy": 5.366319870222696,
            "candidate_energy": 5.345813953992547,
            "relative_energy_error_percent": 0.3821225108837679,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.835232049226761e-06,
              "p95": 5.678832530975342e-05,
              "p99": 0.00016435328871011734,
              "maximum": 0.0003651715815067291
            },
            "worst": {
              "global_sensor_index": 82,
              "local_sensor_index": 18,
              "sky_patch_index": 76,
              "rgb_channel": 0,
              "reference": 0.008710086345672607,
              "candidate": 0.009075257927179337,
              "position": [
                8.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.67559779790355,
            "cvrmse_percent": 501.2841341070828,
            "rms_normalized_rmse_percent": 34.17886530142513,
            "reference_energy": 2.254533914059161,
            "candidate_energy": 4.095937965923454,
            "relative_energy_error_percent": 81.67559779790356,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.525588934711777e-05,
              "p90": 0.0002672907794476487,
              "p95": 0.00038079998921602964,
              "p99": 0.0006859523709863424,
              "maximum": 0.014455929398536682
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022517260164022446,
              "candidate": 0.03697318956255913,
              "position": [
                6.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.89362382715933,
            "cvrmse_percent": 148.23585612695663,
            "rms_normalized_rmse_percent": 34.16440046690893,
            "reference_energy": 7.620853784281858,
            "candidate_energy": 9.441751919916001,
            "relative_energy_error_percent": 23.893623827159335,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.4323905058263335e-05,
              "p90": 0.0002670416724868119,
              "p95": 0.0003710599849000573,
              "p99": 0.0006217854097485542,
              "maximum": 0.014455929398536682
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022517260164022446,
              "candidate": 0.03697318956255913,
              "position": [
                6.5,
                11.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "full_identifier": "courtyard_rooms_south_grid",
        "start_sensor_index": 88,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2276783952661703,
            "cvrmse_percent": 5.926218621798515,
            "rms_normalized_rmse_percent": 1.4217865934738816,
            "reference_energy": 5.3559874540273995,
            "candidate_energy": 5.3437930277414125,
            "relative_energy_error_percent": 0.22767839526617026,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 8.64267349243164e-06,
              "p95": 5.051555490354076e-05,
              "p99": 0.0001460714265704155,
              "maximum": 0.0003647543489933014
            },
            "worst": {
              "global_sensor_index": 92,
              "local_sensor_index": 4,
              "sky_patch_index": 64,
              "rgb_channel": 0,
              "reference": 0.008932281285524368,
              "candidate": 0.00929703563451767,
              "position": [
                5.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 87.06116098617608,
            "cvrmse_percent": 552.4295897733616,
            "rms_normalized_rmse_percent": 37.059150925060436,
            "reference_energy": 2.190328234213357,
            "candidate_energy": 4.097253424327516,
            "relative_energy_error_percent": 87.06116098617606,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.249335324857384e-05,
              "p90": 0.0002925400040112436,
              "p95": 0.000388401560485363,
              "p99": 0.0005986360683891689,
              "maximum": 0.01573396846652031
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02148808166384697,
              "candidate": 0.03722205013036728,
              "position": [
                6.5,
                -3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 25.10802412865771,
            "cvrmse_percent": 160.29502773790148,
            "rms_normalized_rmse_percent": 37.047964430841574,
            "reference_energy": 7.546315688240757,
            "candidate_energy": 9.441046452068928,
            "relative_energy_error_percent": 25.10802412865771,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.211271516396664e-05,
              "p90": 0.0002866140566766262,
              "p95": 0.00037938327477604616,
              "p99": 0.000626767985522747,
              "maximum": 0.01573396846652031
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02148808166384697,
              "candidate": 0.03722205013036728,
              "position": [
                6.5,
                -3.5,
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
      "bias_percent": -0.025870228784340553,
      "rms_normalized_error_percent": 0.297769365670421,
      "absolute_error": {
        "p95": 0.12985160793363526,
        "p99": 0.17455830083281984,
        "maximum": 0.17503145921224217
      },
      "worst_index": [
        61
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 14.545498010210869,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.297769365670421
    },
    "overcast": {
      "bias_percent": 0.02315164457519982,
      "rms_normalized_error_percent": 0.24789789084930497,
      "absolute_error": {
        "p95": 0.07287445068359374,
        "p99": 0.1023407554626465,
        "maximum": 0.10753035545349121
      },
      "worst_index": [
        61
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.026803016662598,
      "reference_fraction_of_uniform": 0.6893406510353088,
      "rms_normalized_to_uniform_percent": 0.1814624330027265
    },
    "horizon": {
      "bias_percent": -2.7309329252588284,
      "rms_normalized_error_percent": 8.118275443179671,
      "absolute_error": {
        "p95": 0.04549179890761147,
        "p99": 0.056313481539377944,
        "maximum": 0.05723274301138634
      },
      "worst_index": [
        104
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.2517562724328503,
      "reference_fraction_of_uniform": 0.017308192009384528,
      "rms_normalized_to_uniform_percent": 0.10454486446217656
    },
    "north": {
      "bias_percent": -0.1719625570434118,
      "rms_normalized_error_percent": 0.4107752267991057,
      "absolute_error": {
        "p95": 0.05586757659912104,
        "p99": 0.10017057895660401,
        "maximum": 0.12990951538085938
      },
      "worst_index": [
        101
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8354251384735107,
      "reference_fraction_of_uniform": 0.2636846899986267,
      "rms_normalized_to_uniform_percent": 0.14074936960614456
    },
    "east": {
      "bias_percent": -0.00046802447885094917,
      "rms_normalized_error_percent": 0.3955200981703499,
      "absolute_error": {
        "p95": 0.053784739971160844,
        "p99": 0.078940589427948,
        "maximum": 0.08370602130889893
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7700958251953125,
      "reference_fraction_of_uniform": 0.2591933012008667,
      "rms_normalized_to_uniform_percent": 0.13365077552781654
    },
    "south": {
      "bias_percent": 0.02919482882240281,
      "rms_normalized_error_percent": 0.4328298202482696,
      "absolute_error": {
        "p95": 0.06087583303451531,
        "p99": 0.12498308420181276,
        "maximum": 0.16529560089111328
      },
      "worst_index": [
        76
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7373173236846924,
      "reference_fraction_of_uniform": 0.2569397985935211,
      "rms_normalized_to_uniform_percent": 0.14414280771277438
    },
    "west": {
      "bias_percent": -0.11261126564354795,
      "rms_normalized_error_percent": 0.35522028014679813,
      "absolute_error": {
        "p95": 0.050105547904968156,
        "p99": 0.08241703987121583,
        "maximum": 0.1007833480834961
      },
      "worst_index": [
        61
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6978726387023926,
      "reference_fraction_of_uniform": 0.25422799587249756,
      "rms_normalized_to_uniform_percent": 0.11873249149252343
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
        "identifier": "courtyard_rooms_west_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": 0.07282663199925965,
          "cvrmse_percent": 2.473143061271837,
          "absolute_error_percentiles_lux": {
            "p50": 3.505889892578125,
            "p90": 26.415844726562504,
            "p95": 40.68400421142574,
            "p99": 86.66576416015627
          },
          "maximum_absolute_error_lux": 270.5400390625,
          "worst": {
            "sensor_index": 17,
            "position": [
              2.5,
              6.5,
              0.75
            ],
            "hour_of_year": 2961.5,
            "foton_lux": 6700.42041015625,
            "radiance_lux": 6429.88037109375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5083005136986298,
            "maximum_error_percentage_points": 3.315205479452054,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.28752585871204883,
            "maximum_error_percentage_points": 2.052140348665212,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.224109589041096,
            "maximum_error_percentage_points": 1.374794520547944,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.23724315068493151,
            "maximum_error_percentage_points": 1.374794520547944,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.01869863013698627,
            "maximum_error_percentage_points": 0.13493150684931532,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 34.375,
          "radiance_percent": 34.375,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": -0.024731656663592658,
          "cvrmse_percent": 2.251157324586253,
          "absolute_error_percentiles_lux": {
            "p50": 3.4634971618652344,
            "p90": 25.504135131835938,
            "p95": 37.15369567871092,
            "p99": 67.78411560058602
          },
          "maximum_absolute_error_lux": 224.3349609375,
          "worst": {
            "sensor_index": 3,
            "position": [
              10.5,
              4.5,
              0.75
            ],
            "hour_of_year": 6086.5,
            "foton_lux": 16141.302734375,
            "radiance_lux": 15916.9677734375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5538270547945213,
            "maximum_error_percentage_points": 2.7927397260273956,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.21371398826950694,
            "maximum_error_percentage_points": 0.7546773379525007,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.20383133561643818,
            "maximum_error_percentage_points": 0.7704109589041153,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22294092465753335,
            "maximum_error_percentage_points": 0.7704109589041082,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.02938356164383562,
            "maximum_error_percentage_points": 0.13465753424657478,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 43.75,
          "radiance_percent": 46.875,
          "difference_percentage_points": 3.125,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.09112305911925396,
          "cvrmse_percent": 1.877191668170733,
          "absolute_error_percentiles_lux": {
            "p50": 5.1031646728515625,
            "p90": 38.04822998046876,
            "p95": 57.0909240722656,
            "p99": 114.49462890624989
          },
          "maximum_absolute_error_lux": 328.8076171875,
          "worst": {
            "sensor_index": 17,
            "position": [
              8.5,
              10.5,
              0.75
            ],
            "hour_of_year": 6829.5,
            "foton_lux": 9800.328125,
            "radiance_lux": 10129.1357421875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.26330479452054867,
            "maximum_error_percentage_points": 0.7369863013698676,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1384132310149481,
            "maximum_error_percentage_points": 0.5625649003895177,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.10330479452054786,
            "maximum_error_percentage_points": 0.30630136986301437,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.12926940639269593,
            "maximum_error_percentage_points": 0.3276712328767246,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.07607305936073029,
            "maximum_error_percentage_points": 0.2753424657534236,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 95.83333333333333,
          "difference_percentage_points": 4.166666666666657,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.0021554524244297574,
          "cvrmse_percent": 3.290056629377081,
          "absolute_error_percentiles_lux": {
            "p50": 2.7802734375,
            "p90": 18.354235839843764,
            "p95": 26.34221954345702,
            "p99": 47.63429260253905
          },
          "maximum_absolute_error_lux": 130.979736328125,
          "worst": {
            "sensor_index": 8,
            "position": [
              6.5,
              -0.5,
              0.75
            ],
            "hour_of_year": 4936.5,
            "foton_lux": 1359.1705322265625,
            "radiance_lux": 1490.1502685546875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.4308447488584472,
            "maximum_error_percentage_points": 1.6454794520547935,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1781493521062997,
            "maximum_error_percentage_points": 0.6050434994805656,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.11676940639269422,
            "maximum_error_percentage_points": 0.40712328767123296,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.11676940639269429,
            "maximum_error_percentage_points": 0.40712328767123296,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 41.666666666666664,
          "radiance_percent": 41.666666666666664,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
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
      "maximum_error_percentage_points": 0.004980468750005684,
      "metrics": {
        "da": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004963345462329016,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004980468750005684,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004779537671240064,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.0048598030821978,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
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
      "study_preparation_seconds": 0.015182708040811121,
      "weather_seconds": 0.10514704091474414,
      "metric_reduction_seconds": 0.0993990000570193,
      "write_seconds": 0.10628837498370558,
      "total_seconds": 0.3110082090133801,
      "cold_end_to_end_seconds": 0.32619091705419123,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.06818029202986509,
      "engine_upload_seconds": 0.000270542,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.07928262511268258,
      "engine_annual_reduction_seconds": 0.0008627916686236858,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.07928262511268258
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.015182708040811121,
      "weather_seconds": 0.1543400000082329,
      "metric_reduction_seconds": 0.014723124913871288,
      "write_seconds": 0.05914341693278402,
      "total_seconds": 0.2284272500546649,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2284272500546649,
      "raw_export_seconds": 0.027125874999910593,
      "engine_upload_seconds": 6.3e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0010989999864250422,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.010454833973199129,
      "full": 0.0708980830386281
    }
  },
  "elapsed_seconds": 151.11841133399867,
  "result_class": "passed"
}
```
