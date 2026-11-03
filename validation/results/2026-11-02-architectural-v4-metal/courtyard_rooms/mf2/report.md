# Foton report

Status: **failed**

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
  "sky_density": 2,
  "status": "failed",
  "passed": false,
  "model_sha256": "737b82fa2d38d04afbb827f4135a443643b051683e395176dec1609c75cebfad",
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
      "scene_fingerprint": 16353448696249269853,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": -0.0617870580197302,
        "rms_normalized_error_percent": 2.0054789116540115,
        "absolute_error": {
          "p95": 2.225817434009452e-06,
          "p99": 5.3780851885676384e-05,
          "maximum": 0.000219903071410954
        },
        "worst_index": [
          20,
          257,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": -0.03877125199078907,
        "rms_normalized_error_percent": 1.7126260034441043,
        "absolute_error": {
          "p95": 1.8526833628129107e-06,
          "p99": 4.403468687087163e-05,
          "maximum": 0.00020035728812217712
        },
        "worst_index": [
          20,
          281,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": -0.02912038507049746,
        "rms_normalized_error_percent": 1.791155159210393,
        "absolute_error": {
          "p95": 6.941612809896469e-06,
          "p99": 5.37758693099015e-05,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          11,
          543,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": 0.1452845527800859,
        "rms_normalized_error_percent": 1.8407748647989366,
        "absolute_error": {
          "p95": 6.831385235273046e-06,
          "p99": 5.762645887443718e-05,
          "maximum": 0.0001625253353267908
        },
        "worst_index": [
          14,
          285,
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
        "bias_percent": 0.04980082835284329,
        "rms_normalized_error_percent": 1.3836624562235846,
        "absolute_error": {
          "p95": 2.706860243506514e-05,
          "p99": 9.505293681286262e-05,
          "maximum": 0.000647764652967453
        },
        "worst_index": [
          27,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": 0.09659109432140972,
        "rms_normalized_error_percent": 1.419352139733467,
        "absolute_error": {
          "p95": 2.6671383602660974e-05,
          "p99": 0.00010061996639706192,
          "maximum": 0.0007602870464324951
        },
        "worst_index": [
          4,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": 0.08680548336933441,
        "rms_normalized_error_percent": 1.3503012492690953,
        "absolute_error": {
          "p95": 3.4428565413691103e-05,
          "p99": 0.00011759129702113519,
          "maximum": 0.0005689971148967743
        },
        "worst_index": [
          8,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": -0.08991826840435414,
        "rms_normalized_error_percent": 1.3709280567738926,
        "absolute_error": {
          "p95": 3.5525066778063774e-05,
          "p99": 0.00011577801778912518,
          "maximum": 0.00045374780893325806
        },
        "worst_index": [
          22,
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
        "bias_percent": 0.016150318592904375,
        "rms_normalized_error_percent": 1.1934702419939236,
        "absolute_error": {
          "p95": 2.2625734709436052e-05,
          "p99": 8.049028459936373e-05,
          "maximum": 0.000686347484588623
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
        "bias_percent": -0.0702210601960604,
        "rms_normalized_error_percent": 1.137963517666008,
        "absolute_error": {
          "p95": 2.306550404682638e-05,
          "p99": 8.657037862576519e-05,
          "maximum": 0.0004341714084148407
        },
        "worst_index": [
          18,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": -0.00628757130402933,
        "rms_normalized_error_percent": 1.1255207217844527,
        "absolute_error": {
          "p95": 2.9905742849223316e-05,
          "p99": 9.560059988871171e-05,
          "maximum": 0.00048730894923210144
        },
        "worst_index": [
          12,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": 0.06358785883160176,
        "rms_normalized_error_percent": 1.1831269163255718,
        "absolute_error": {
          "p95": 3.0784751288592815e-05,
          "p99": 9.91913955658672e-05,
          "maximum": 0.0004726201295852661
        },
        "worst_index": [
          6,
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
        "run_count": 8,
        "half_run_count": 4,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.16891835219367182,
                "cvrmse_percent": 26.789868749936897,
                "rms_normalized_rmse_percent": 5.346634500374126,
                "reference_energy": 5.726045466407776,
                "candidate_energy": 5.716373124760059,
                "relative_energy_error_percent": 0.16891835219367182,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1635150642395478e-05,
                  "p99": 0.000154865038275602,
                  "maximum": 0.0004236722888890654
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 202,
                  "rgb_channel": 0,
                  "reference": 0.001630413724342361,
                  "candidate": 0.0020540860132314265
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.5669925535748187,
                "cvrmse_percent": 92.83688856180656,
                "rms_normalized_rmse_percent": 3.538726590838042,
                "reference_energy": 2.399996109212939,
                "candidate_energy": 2.4136039084382617,
                "relative_energy_error_percent": 0.5669925535748187,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.277340487211177e-05,
                  "p95": 4.540652516880067e-05,
                  "p99": 0.0002087206438591234,
                  "maximum": 0.0008733021095395088
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04244955535978079,
                  "candidate": 0.0433228574693203
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
                "nmbe_percent": 0.03952248909902072,
                "cvrmse_percent": 26.756409813447043,
                "rms_normalized_rmse_percent": 5.337067675317053,
                "reference_energy": 5.72480557941075,
                "candidate_energy": 5.727068165071813,
                "relative_energy_error_percent": 0.039522489099020716,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2236778750084236e-05,
                  "p99": 0.00015614885487593694,
                  "maximum": 0.00046056380961090326
                },
                "worst": {
                  "global_sensor_index": 51,
                  "local_sensor_index": 19,
                  "sky_patch_index": 279,
                  "rgb_channel": 0,
                  "reference": 0.0030323414830490947,
                  "candidate": 0.003492905292659998
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.006714081878035444,
                "cvrmse_percent": 99.28681441897662,
                "rms_normalized_rmse_percent": 3.7907126712971375,
                "reference_energy": 2.409562699371671,
                "candidate_energy": 2.4094009193591326,
                "relative_energy_error_percent": 0.006714081878035443,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.2383320356311742e-05,
                  "p95": 4.551979363895948e-05,
                  "p99": 0.00023551216407213303,
                  "maximum": 0.0006678943755105138
                },
                "worst": {
                  "global_sensor_index": 63,
                  "local_sensor_index": 31,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.008061855449341238,
                  "candidate": 0.008729749824851751
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.04975046669785846,
                "cvrmse_percent": 24.673496744576365,
                "rms_normalized_rmse_percent": 5.53332504395156,
                "reference_energy": 5.355747863537275,
                "candidate_energy": 5.353083353980004,
                "relative_energy_error_percent": 0.049750466697858466,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.4203592551639304e-05,
                  "p99": 0.00017548249161336376,
                  "maximum": 0.0006277601351030171
                },
                "worst": {
                  "global_sensor_index": 71,
                  "local_sensor_index": 7,
                  "sky_patch_index": 405,
                  "rgb_channel": 0,
                  "reference": 0.003312593966256827,
                  "candidate": 0.003940354101359844
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.5284883661115933,
                "cvrmse_percent": 88.07251818501537,
                "rms_normalized_rmse_percent": 3.6626868475368517,
                "reference_energy": 2.2535805822205806,
                "candidate_energy": 2.2654904934185662,
                "relative_energy_error_percent": 0.5284883661115933,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.646121330002643e-07,
                  "p90": 2.5337074617937105e-05,
                  "p95": 6.0975755332037807e-05,
                  "p99": 0.0002493948253686528,
                  "maximum": 0.0012779319658875465
                },
                "worst": {
                  "global_sensor_index": 79,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04534436296671629,
                  "candidate": 0.046622294932603836
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
                "nmbe_percent": 0.1990774288138831,
                "cvrmse_percent": 25.805739726902672,
                "rms_normalized_rmse_percent": 5.761213886656625,
                "reference_energy": 5.353519198775693,
                "candidate_energy": 5.364176847147673,
                "relative_energy_error_percent": 0.19907742881388307,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.5772912926622666e-05,
                  "p99": 0.0001812817994505164,
                  "maximum": 0.0005506005545612425
                },
                "worst": {
                  "global_sensor_index": 91,
                  "local_sensor_index": 3,
                  "sky_patch_index": 128,
                  "rgb_channel": 0,
                  "reference": 0.0006637959741055965,
                  "candidate": 0.001214396528666839
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.19196653161450636,
                "cvrmse_percent": 96.53111102792535,
                "rms_normalized_rmse_percent": 3.9956761387605773,
                "reference_energy": 2.1935355517697737,
                "candidate_energy": 2.18932469765131,
                "relative_energy_error_percent": 0.19196653161450633,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 9.851896720647346e-07,
                  "p90": 2.6010709916590713e-05,
                  "p95": 6.633251177845523e-05,
                  "p99": 0.0002753806489636188,
                  "maximum": 0.0007017919269856066
                },
                "worst": {
                  "global_sensor_index": 98,
                  "local_sensor_index": 10,
                  "sky_patch_index": 181,
                  "rgb_channel": 0,
                  "reference": -0.00042088344343937933,
                  "candidate": 0.0002809084835462272
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 298.4334579668939,
            "full": 858.9319169986993
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 254.76545910350978,
            "full": 877.1405840525404
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 245.36066700238734,
            "full": 613.1347910268232
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 201.96887501515448,
            "full": 583.0918340943754
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 299.7404170455411,
            "full": 851.9797080662102
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 276.1942090000957,
            "full": 883.2502090372145
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 243.15887491684407,
            "full": 874.0641659824178
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 276.0514169931412,
            "full": 846.3157499209046
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.07239615970176687,
                "cvrmse_percent": 23.103525836255454,
                "rms_normalized_rmse_percent": 4.608763823389752,
                "reference_energy": 5.723634562273077,
                "candidate_energy": 5.727778253891525,
                "relative_energy_error_percent": 0.07239615970176687,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1623221709886892e-05,
                  "p99": 0.00013584362284745975,
                  "maximum": 0.0003360580885782838
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 249,
                  "rgb_channel": 0,
                  "reference": 0.002673955517821014,
                  "candidate": 0.00233789742924273
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.21029319219896114,
                "cvrmse_percent": 50.248379202965374,
                "rms_normalized_rmse_percent": 2.6338305020469974,
                "reference_energy": 4.384465234308333,
                "candidate_energy": 4.375245002406253,
                "relative_energy_error_percent": 0.21029319219896114,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.541340786090586e-06,
                  "p90": 2.350744034629315e-05,
                  "p95": 4.2894797365987256e-05,
                  "p99": 0.00019402693782466878,
                  "maximum": 0.0014491844922304153
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04188578017055988,
                  "candidate": 0.04043659567832947
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
                "nmbe_percent": 0.04476145557350953,
                "cvrmse_percent": 22.789532152119275,
                "rms_normalized_rmse_percent": 4.546012479081476,
                "reference_energy": 5.7212058211253165,
                "candidate_energy": 5.7237667161272086,
                "relative_energy_error_percent": 0.04476145557350953,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.0921965187881118e-05,
                  "p99": 0.0001340909286227535,
                  "maximum": 0.00033837242517620325
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 5,
                  "sky_patch_index": 424,
                  "rgb_channel": 0,
                  "reference": 0.003632241510786116,
                  "candidate": 0.003970613935962319
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.3561423890602463,
                "cvrmse_percent": 47.751244917557194,
                "rms_normalized_rmse_percent": 2.502406936233265,
                "reference_energy": 4.386291079905703,
                "candidate_energy": 4.401912521748816,
                "relative_energy_error_percent": 0.3561423890602463,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.631642354979704e-06,
                  "p90": 2.3185576537798624e-05,
                  "p95": 4.1871023677230925e-05,
                  "p99": 0.00018720802036113917,
                  "maximum": 0.0009152218699455261
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 13,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04094566963613033,
                  "candidate": 0.04186089150607586
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
                "nmbe_percent": -0.05556132280982044,
                "cvrmse_percent": 21.508452004384086,
                "rms_normalized_rmse_percent": 4.823449819431822,
                "reference_energy": 5.3564605104565,
                "candidate_energy": 5.353484390141105,
                "relative_energy_error_percent": 0.05556132280982044,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.069387796334922e-05,
                  "p99": 0.00015336836222559183,
                  "maximum": 0.0004095176700502634
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 10,
                  "sky_patch_index": 263,
                  "rgb_channel": 0,
                  "reference": 0.0025130995782092214,
                  "candidate": 0.002103581908158958
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.009643323647369605,
                "cvrmse_percent": 44.773899290186435,
                "rms_normalized_rmse_percent": 2.4611988744806172,
                "reference_energy": 4.1281852703584825,
                "candidate_energy": 4.128583364624866,
                "relative_energy_error_percent": 0.009643323647369605,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.110341189469182e-06,
                  "p90": 2.8385928089846857e-05,
                  "p95": 5.901024678678368e-05,
                  "p99": 0.0002290172407811022,
                  "maximum": 0.0008197203278541565
                },
                "worst": {
                  "global_sensor_index": 76,
                  "local_sensor_index": 12,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03767319396138191,
                  "candidate": 0.036853473633527756
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
                "nmbe_percent": 0.11133451233917058,
                "cvrmse_percent": 21.956792033965737,
                "rms_normalized_rmse_percent": 4.904647748578659,
                "reference_energy": 5.353040452765434,
                "candidate_energy": 5.359000234248839,
                "relative_energy_error_percent": 0.11133451233917058,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.0615908801555634e-05,
                  "p99": 0.00015787929878570132,
                  "maximum": 0.00037756707752123475
                },
                "worst": {
                  "global_sensor_index": 96,
                  "local_sensor_index": 8,
                  "sky_patch_index": 337,
                  "rgb_channel": 0,
                  "reference": 0.001428732997737825,
                  "candidate": 0.0018063000752590597
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.055829577098918365,
                "cvrmse_percent": 49.028801786106754,
                "rms_normalized_rmse_percent": 2.7195495239178515,
                "reference_energy": 4.08403401939799,
                "candidate_energy": 4.081753920476384,
                "relative_energy_error_percent": 0.055829577098918365,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.942627410604473e-06,
                  "p90": 3.0077892006374896e-05,
                  "p95": 6.506545469164848e-05,
                  "p99": 0.0002324012224562466,
                  "maximum": 0.0013277307152748108
                },
                "worst": {
                  "global_sensor_index": 93,
                  "local_sensor_index": 5,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04224951006472111,
                  "candidate": 0.04357724077999592
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
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 357.2061250451952,
            "full": 11331.166041898541
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 443.35616705939174,
            "full": 11086.231332970783
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 437.21545801963657,
            "full": 12031.180083053187
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 463.2107079960406,
            "full": 9275.105874985456
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.10339894957572822,
                "cvrmse_percent": 22.94026789805031,
                "rms_normalized_rmse_percent": 4.575232210814478,
                "reference_energy": 5.718889914532131,
                "candidate_energy": 5.724803186631149,
                "relative_energy_error_percent": 0.10339894957572823,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.182432363042603e-05,
                  "p99": 0.0001361324195750048,
                  "maximum": 0.00033560750307515264
                },
                "worst": {
                  "global_sensor_index": 26,
                  "local_sensor_index": 26,
                  "sky_patch_index": 262,
                  "rgb_channel": 0,
                  "reference": 0.0017331945127807558,
                  "candidate": 0.0013975870097056031
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.1696376331877153,
                "cvrmse_percent": 46.383753552459964,
                "rms_normalized_rmse_percent": 2.433362024854824,
                "reference_energy": 4.392473253364599,
                "candidate_energy": 4.385021965699188,
                "relative_energy_error_percent": 0.1696376331877153,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.4570450654646265e-06,
                  "p90": 2.3222420622914797e-05,
                  "p95": 4.2035884689538865e-05,
                  "p99": 0.0001934648019960143,
                  "maximum": 0.0005337093025445938
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05246854946017265,
                  "candidate": 0.05193484015762806
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
                "nmbe_percent": 0.03651864114640476,
                "cvrmse_percent": 22.690721053871865,
                "rms_normalized_rmse_percent": 4.530549776598434,
                "reference_energy": 5.730007261574958,
                "candidate_energy": 5.732099782364475,
                "relative_energy_error_percent": 0.03651864114640477,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.149122610717302e-05,
                  "p99": 0.0001306682426366023,
                  "maximum": 0.00036812142934650183
                },
                "worst": {
                  "global_sensor_index": 57,
                  "local_sensor_index": 25,
                  "sky_patch_index": 162,
                  "rgb_channel": 0,
                  "reference": 0.0011492945486679673,
                  "candidate": 0.0015174159780144691
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.20107499518365712,
                "cvrmse_percent": 45.970546404059995,
                "rms_normalized_rmse_percent": 2.411444532906694,
                "reference_energy": 4.390891779454286,
                "candidate_energy": 4.399720764888343,
                "relative_energy_error_percent": 0.20107499518365712,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.6504977717631846e-06,
                  "p90": 2.3433818569174036e-05,
                  "p95": 4.2483406559766775e-05,
                  "p99": 0.000193912190734405,
                  "maximum": 0.0005353335291147232
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05233265087008476,
                  "candidate": 0.052867984399199486
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
                "nmbe_percent": -0.09849708235598041,
                "cvrmse_percent": 21.145311543211644,
                "rms_normalized_rmse_percent": 4.741401678952671,
                "reference_energy": 5.354866948378952,
                "candidate_energy": 5.349592560670754,
                "relative_energy_error_percent": 0.09849708235598043,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.0697515942156315e-05,
                  "p99": 0.00015123650664463636,
                  "maximum": 0.00039331987500190735
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 10,
                  "sky_patch_index": 209,
                  "rgb_channel": 0,
                  "reference": 0.002035281388089061,
                  "candidate": 0.0016419615130871534
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.0818294101025873,
                "cvrmse_percent": 45.10171289930913,
                "rms_normalized_rmse_percent": 2.48995937969813,
                "reference_energy": 4.137666202508694,
                "candidate_energy": 4.141052030354221,
                "relative_energy_error_percent": 0.0818294101025873,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.185047823237255e-06,
                  "p90": 2.9030472433078103e-05,
                  "p95": 6.040995504008606e-05,
                  "p99": 0.00022930050718059604,
                  "maximum": 0.0009544417262077332
                },
                "worst": {
                  "global_sensor_index": 76,
                  "local_sensor_index": 12,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03746148571372032,
                  "candidate": 0.03650704398751259
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
                "nmbe_percent": -0.0515095087965214,
                "cvrmse_percent": 22.325170324395206,
                "rms_normalized_rmse_percent": 4.979614540104741,
                "reference_energy": 5.357349102602136,
                "candidate_energy": 5.354589558394871,
                "relative_energy_error_percent": 0.05150950879652141,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.335744597483426e-05,
                  "p99": 0.00015850825875531773,
                  "maximum": 0.0004306264454498887
                },
                "worst": {
                  "global_sensor_index": 100,
                  "local_sensor_index": 12,
                  "sky_patch_index": 286,
                  "rgb_channel": 0,
                  "reference": 0.002167319064028561,
                  "candidate": 0.00259794550947845
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.055899913476584094,
                "cvrmse_percent": 45.81850151431186,
                "rms_normalized_rmse_percent": 2.5392199387865135,
                "reference_energy": 4.075596763657181,
                "candidate_energy": 4.073318508592642,
                "relative_energy_error_percent": 0.05589991347658409,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.143125574453734e-06,
                  "p90": 2.8540506718854886e-05,
                  "p95": 6.219453644007444e-05,
                  "p99": 0.00023081102335708955,
                  "maximum": 0.0010936949402093887
                },
                "worst": {
                  "global_sensor_index": 96,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05834941007196903,
                  "candidate": 0.05944310501217842
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
              "40000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 314.4885830115527,
            "full": 11487.347249989398
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 479.2953330324963,
            "full": 11175.557457958348
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 304.2166670784354,
            "full": 8342.533875023946
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 422.20062494743615,
            "full": 12568.339542020112
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.017794533771859432,
                "cvrmse_percent": 13.068129989387282,
                "rms_normalized_rmse_percent": 2.6092986925531414,
                "reference_energy": 5.722877453406586,
                "candidate_energy": 5.723895812767754,
                "relative_energy_error_percent": 0.01779453377185943,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.091766098397782e-05,
                  "p99": 7.538879770436322e-05,
                  "maximum": 0.0002088345354422927
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 143,
                  "rgb_channel": 0,
                  "reference": 0.0012500325101427734,
                  "candidate": 0.0010411979747004807
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.17922325964083263,
                "cvrmse_percent": 29.326806954230833,
                "rms_normalized_rmse_percent": 1.5372619500104288,
                "reference_energy": 4.384911022887131,
                "candidate_energy": 4.3927698033547,
                "relative_energy_error_percent": 0.17922325964083263,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.5853615827363683e-06,
                  "p90": 1.594900982127001e-05,
                  "p95": 2.7701148655978472e-05,
                  "p99": 0.0001199330724193704,
                  "maximum": 0.0004888642579317093
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.029292240738868713,
                  "candidate": 0.029781104996800423
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
                "nmbe_percent": 0.038448883051801455,
                "cvrmse_percent": 13.139479346051312,
                "rms_normalized_rmse_percent": 2.622663249321478,
                "reference_energy": 5.7270614318136595,
                "candidate_energy": 5.729263422965882,
                "relative_energy_error_percent": 0.038448883051801455,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1078428042310308e-05,
                  "p99": 7.656117726582951e-05,
                  "maximum": 0.00022805656772106886
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 4,
                  "sky_patch_index": 275,
                  "rgb_channel": 0,
                  "reference": 0.0031480230391025543,
                  "candidate": 0.003376079606823623
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.19314396258788855,
                "cvrmse_percent": 29.443379341702563,
                "rms_normalized_rmse_percent": 1.5438971077179198,
                "reference_energy": 4.395331182336712,
                "candidate_energy": 4.386841865522285,
                "relative_energy_error_percent": 0.19314396258788855,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.573706862880499e-06,
                  "p90": 1.6423398847109638e-05,
                  "p95": 2.827469641033528e-05,
                  "p99": 0.00011225719703360881,
                  "maximum": 0.0006253458559513092
                },
                "worst": {
                  "global_sensor_index": 51,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.043133124709129333,
                  "candidate": 0.04375847056508064
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
                "nmbe_percent": -0.052252574820601805,
                "cvrmse_percent": 12.578833271340898,
                "rms_normalized_rmse_percent": 2.8228197491691254,
                "reference_energy": 5.360776846227235,
                "candidate_energy": 5.357975702294695,
                "relative_energy_error_percent": 0.05225257482060181,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1818035747855902e-05,
                  "p99": 8.762033685343328e-05,
                  "maximum": 0.00026842195075005293
                },
                "worst": {
                  "global_sensor_index": 72,
                  "local_sensor_index": 8,
                  "sky_patch_index": 151,
                  "rgb_channel": 0,
                  "reference": 0.0012737110373564065,
                  "candidate": 0.0015421329881064594
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.09587499631152879,
                "cvrmse_percent": 27.62712180510032,
                "rms_normalized_rmse_percent": 1.516161109110276,
                "reference_energy": 4.129636143561129,
                "candidate_energy": 4.133595432061448,
                "relative_energy_error_percent": 0.09587499631152878,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.5339400003285846e-06,
                  "p90": 1.919991336762905e-05,
                  "p95": 3.5584496799856424e-05,
                  "p99": 0.0001312532171141353,
                  "maximum": 0.0006513502448797226
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.053990378975868225,
                  "candidate": 0.0533390287309885
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
                "nmbe_percent": 0.04505154163556318,
                "cvrmse_percent": 13.812181440534923,
                "rms_normalized_rmse_percent": 3.086120282010468,
                "reference_energy": 5.353892871525524,
                "candidate_energy": 5.356304882801663,
                "relative_energy_error_percent": 0.04505154163556317,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2663036361336708e-05,
                  "p99": 9.42775019211693e-05,
                  "maximum": 0.00024350953754037619
                },
                "worst": {
                  "global_sensor_index": 98,
                  "local_sensor_index": 10,
                  "sky_patch_index": 182,
                  "rgb_channel": 0,
                  "reference": 0.0017491739708930254,
                  "candidate": 0.0019926835084334016
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.10527561135038636,
                "cvrmse_percent": 28.999944767926962,
                "rms_normalized_rmse_percent": 1.6095770724569238,
                "reference_energy": 4.079177527675363,
                "candidate_energy": 4.08347190675569,
                "relative_energy_error_percent": 0.10527561135038639,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.692201571288024e-06,
                  "p90": 1.9796354536083527e-05,
                  "p95": 4.016357706859708e-05,
                  "p99": 0.0001381087056870453,
                  "maximum": 0.000638740137219429
                },
                "worst": {
                  "global_sensor_index": 100,
                  "local_sensor_index": 12,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05839955061674118,
                  "candidate": 0.05903829075396061
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
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 760.9740420011804,
            "full": 17583.005041931756
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 520.5673750024289,
            "full": 20393.292292021215
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 804.4552910141647,
            "full": 18556.75349989906
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 525.5189590388909,
            "full": 15113.707832992077
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 20851.15887504071,
      "worker_pool_size": 12,
      "invocation_count": 7
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/courtyard_rooms/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 67871.40870897565,
      "worker_pool_size": 12,
      "invocation_count": 7
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      112,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16359595079582823,
            "cvrmse_percent": 5.954521342765478,
            "rms_normalized_rmse_percent": 1.1885696846093667,
            "reference_energy": 5.72482586030636,
            "candidate_energy": 5.715460277008788,
            "relative_energy_error_percent": 0.1635959507958127,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.174793139099947e-06,
              "p99": 2.9640955126523754e-05,
              "maximum": 0.00012478476855903864
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 257,
              "rgb_channel": 0,
              "reference": 0.001890760031528771,
              "candidate": 0.0020155448000878096,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.13805258964549016,
            "cvrmse_percent": 49.579218205127,
            "rms_normalized_rmse_percent": 2.5967571377248175,
            "reference_energy": 4.387401201780265,
            "candidate_energy": 4.38134428080307,
            "relative_energy_error_percent": 0.13805258964549016,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.042542928075818e-05,
              "p90": 4.43652334070066e-05,
              "p95": 5.876392056052279e-05,
              "p99": 0.00010324196238798308,
              "maximum": 0.002345077693462372
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03731390833854675,
              "candidate": 0.03496883064508438,
              "position": [
                1.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.1525134293373578,
            "cvrmse_percent": 21.417037619629824,
            "rms_normalized_rmse_percent": 2.5854165362675454,
            "reference_energy": 10.112227062086626,
            "candidate_energy": 10.096804557811858,
            "relative_energy_error_percent": 0.15251342933735776,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0397493198865959e-05,
              "p90": 4.413106944411993e-05,
              "p95": 5.820293845317785e-05,
              "p99": 0.00010142854885998465,
              "maximum": 0.002345077693462372
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03731390833854675,
              "candidate": 0.03496883064508438,
              "position": [
                1.5,
                5.5,
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
            "nmbe_percent": -0.2272899414543597,
            "cvrmse_percent": 5.503560873263799,
            "rms_normalized_rmse_percent": 1.0991809066099327,
            "reference_energy": 5.727734971438439,
            "candidate_energy": 5.714716405975196,
            "relative_energy_error_percent": 0.22728994145435583,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.5632256185633095e-06,
              "p99": 2.8286944143474102e-05,
              "maximum": 9.812612552195787e-05
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 11,
              "sky_patch_index": 221,
              "rgb_channel": 0,
              "reference": 0.001702859066426754,
              "candidate": 0.0016047329409047961,
              "position": [
                11.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.6889062948108766,
            "cvrmse_percent": 52.50076994892369,
            "rms_normalized_rmse_percent": 2.7511280615952614,
            "reference_energy": 4.391513994882281,
            "candidate_energy": 4.361260578534036,
            "relative_energy_error_percent": 0.6889062948108816,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0566787068455596e-05,
              "p90": 4.4365646317601204e-05,
              "p95": 5.7826141380701246e-05,
              "p99": 0.0001035506147309202,
              "maximum": 0.0015712175518274307
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02449384704232216,
              "candidate": 0.022922629490494728,
              "position": [
                13.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.42762048799775015,
            "cvrmse_percent": 22.6776299756839,
            "rms_normalized_rmse_percent": 2.7382734079237023,
            "reference_energy": 10.11924896632072,
            "candidate_energy": 10.075976984509232,
            "relative_energy_error_percent": 0.4276204879977501,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0540341008891119e-05,
              "p90": 4.3947216909145936e-05,
              "p95": 5.752420415774387e-05,
              "p99": 0.00010107232454174624,
              "maximum": 0.0015712175518274307
            },
            "worst": {
              "global_sensor_index": 57,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02449384704232216,
              "candidate": 0.022922629490494728,
              "position": [
                13.5,
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
            "nmbe_percent": -0.25301799114452395,
            "cvrmse_percent": 5.308416225741048,
            "rms_normalized_rmse_percent": 1.1914820551251704,
            "reference_energy": 5.357385014545892,
            "candidate_energy": 5.34382986660421,
            "relative_energy_error_percent": 0.2530179911445322,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.207738235592842e-06,
              "p99": 3.3115266705863073e-05,
              "maximum": 0.00013747472257819027
            },
            "worst": {
              "global_sensor_index": 75,
              "local_sensor_index": 11,
              "sky_patch_index": 157,
              "rgb_channel": 0,
              "reference": 0.00013747472257819027,
              "candidate": 0.0,
              "position": [
                6.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.2480545751943732,
            "cvrmse_percent": 55.53885335969458,
            "rms_normalized_rmse_percent": 3.053806905749824,
            "reference_energy": 4.133607053252474,
            "candidate_energy": 4.0820173813038,
            "relative_energy_error_percent": 1.2480545751943624,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2569958926178515e-05,
              "p90": 5.135991523275152e-05,
              "p95": 6.91895475029014e-05,
              "p99": 0.00012150474512964118,
              "maximum": 0.0023445338010787964
            },
            "worst": {
              "global_sensor_index": 79,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05864780396223068,
              "candidate": 0.056303270161151886,
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
            "nmbe_percent": -0.6863857795370415,
            "cvrmse_percent": 24.13204102675015,
            "rms_normalized_rmse_percent": 3.0466399984600314,
            "reference_energy": 9.490992067798366,
            "candidate_energy": 9.42584724790801,
            "relative_energy_error_percent": 0.6863857795370415,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2552160114864819e-05,
              "p90": 5.117161344969645e-05,
              "p95": 6.86226412653923e-05,
              "p99": 0.00012062731466357904,
              "maximum": 0.0023445338010787964
            },
            "worst": {
              "global_sensor_index": 79,
              "local_sensor_index": 15,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05864780396223068,
              "candidate": 0.056303270161151886,
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
            "nmbe_percent": -0.2443124896080307,
            "cvrmse_percent": 5.594357227703874,
            "rms_normalized_rmse_percent": 1.250090429156463,
            "reference_energy": 5.357599610298205,
            "candidate_energy": 5.344510325307056,
            "relative_energy_error_percent": 0.2443124896080307,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 8.114147931337357e-06,
              "p99": 3.4202588722109795e-05,
              "maximum": 0.00013347197091206908
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 8,
              "sky_patch_index": 175,
              "rgb_channel": 0,
              "reference": 0.00013347197091206908,
              "candidate": 0.0,
              "position": [
                6.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.3592533308676683,
            "cvrmse_percent": 42.5469704856554,
            "rms_normalized_rmse_percent": 2.3592870374412285,
            "reference_energy": 4.0788239630573635,
            "candidate_energy": 4.093477274004876,
            "relative_energy_error_percent": 0.3592533308676683,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2592104212671984e-05,
              "p90": 5.1004251872655004e-05,
              "p95": 6.780749390600249e-05,
              "p99": 0.00012063853209838259,
              "maximum": 0.0015959963202476501
            },
            "worst": {
              "global_sensor_index": 102,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04479285329580307,
              "candidate": 0.04638884961605072,
              "position": [
                7.5,
                -2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.016574350909582473,
            "cvrmse_percent": 18.257641265006377,
            "rms_normalized_rmse_percent": 2.3422285688869984,
            "reference_energy": 9.436423573355569,
            "candidate_energy": 9.437987599311931,
            "relative_energy_error_percent": 0.016574350909582473,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.263696822206839e-05,
              "p90": 5.078290996607393e-05,
              "p95": 6.699475488858297e-05,
              "p99": 0.00011512444762047361,
              "maximum": 0.0015959963202476501
            },
            "worst": {
              "global_sensor_index": 102,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.04479285329580307,
              "candidate": 0.04638884961605072,
              "position": [
                7.5,
                -2.5,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16359595079582823,
            "cvrmse_percent": 5.954521342765478,
            "rms_normalized_rmse_percent": 1.1885696846093667,
            "reference_energy": 5.72482586030636,
            "candidate_energy": 5.715460277008788,
            "relative_energy_error_percent": 0.1635959507958127,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.174793139099947e-06,
              "p99": 2.9640955126523754e-05,
              "maximum": 0.00012478476855903864
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 257,
              "rgb_channel": 0,
              "reference": 0.001890760031528771,
              "candidate": 0.0020155448000878096,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.31418224578749,
            "cvrmse_percent": 983.7246125000798,
            "rms_normalized_rmse_percent": 37.51256815516999,
            "reference_energy": 2.4031834642991985,
            "candidate_energy": 4.38134428080307,
            "relative_energy_error_percent": 82.31418224578749,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.6281389738142025e-06,
              "p90": 6.860356370452791e-05,
              "p95": 9.730831508818412e-05,
              "p99": 0.00016855960702116576,
              "maximum": 0.013149911537766457
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01798516884446144,
              "candidate": 0.031135080382227898,
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
            "nmbe_percent": 24.222354509932117,
            "cvrmse_percent": 290.8382018508807,
            "rms_normalized_rmse_percent": 37.51042432860738,
            "reference_energy": 8.12800932460556,
            "candidate_energy": 10.096804557811858,
            "relative_energy_error_percent": 24.222354509932103,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.621945997016155e-06,
              "p90": 6.775080692023039e-05,
              "p95": 9.643199700803916e-05,
              "p99": 0.00016805420378659608,
              "maximum": 0.013149911537766457
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01798516884446144,
              "candidate": 0.031135080382227898,
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
        "identifier": "courtyard_rooms_east_grid",
        "full_identifier": "courtyard_rooms_east_grid",
        "start_sensor_index": 32,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2272899414543597,
            "cvrmse_percent": 5.503560873263799,
            "rms_normalized_rmse_percent": 1.0991809066099327,
            "reference_energy": 5.727734971438439,
            "candidate_energy": 5.714716405975196,
            "relative_energy_error_percent": 0.22728994145435583,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.5632256185633095e-06,
              "p99": 2.8286944143474102e-05,
              "maximum": 9.812612552195787e-05
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 11,
              "sky_patch_index": 221,
              "rgb_channel": 0,
              "reference": 0.001702859066426754,
              "candidate": 0.0016047329409047961,
              "position": [
                11.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.139264745589,
            "cvrmse_percent": 971.2183121419507,
            "rms_normalized_rmse_percent": 37.00580313925636,
            "reference_energy": 2.4076837148806187,
            "candidate_energy": 4.361260578534036,
            "relative_energy_error_percent": 81.13926474558902,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.74000000092201e-06,
              "p90": 6.713000038871542e-05,
              "p95": 9.654130235503513e-05,
              "p99": 0.00016780190169811234,
              "maximum": 0.014222027733922005
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021448401734232903,
              "candidate": 0.03567042946815491,
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
            "nmbe_percent": 23.853207474785748,
            "cvrmse_percent": 287.41170870565577,
            "rms_normalized_rmse_percent": 37.00308231608657,
            "reference_energy": 8.135418686319058,
            "candidate_energy": 10.075976984509232,
            "relative_energy_error_percent": 23.853207474785748,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.71000031818403e-06,
              "p90": 6.68283305458317e-05,
              "p95": 9.578432582202355e-05,
              "p99": 0.00016518650473244426,
              "maximum": 0.014222027733922005
            },
            "worst": {
              "global_sensor_index": 60,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021448401734232903,
              "candidate": 0.03567042946815491,
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
            "nmbe_percent": -0.25301799114452395,
            "cvrmse_percent": 5.308416225741048,
            "rms_normalized_rmse_percent": 1.1914820551251704,
            "reference_energy": 5.357385014545892,
            "candidate_energy": 5.34382986660421,
            "relative_energy_error_percent": 0.2530179911445322,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.207738235592842e-06,
              "p99": 3.3115266705863073e-05,
              "maximum": 0.00013747472257819027
            },
            "worst": {
              "global_sensor_index": 75,
              "local_sensor_index": 11,
              "sky_patch_index": 157,
              "rgb_channel": 0,
              "reference": 0.00013747472257819027,
              "candidate": 0.0,
              "position": [
                6.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.89509074832382,
            "cvrmse_percent": 977.9786495331015,
            "rms_normalized_rmse_percent": 40.61499877329354,
            "reference_energy": 2.256566148046018,
            "candidate_energy": 4.0820173813038,
            "relative_energy_error_percent": 80.89509074832384,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1145758350039614e-05,
              "p90": 8.151999645633623e-05,
              "p95": 0.00011548444990694406,
              "p99": 0.00019602543077326096,
              "maximum": 0.014987420290708542
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022253520786762238,
              "candidate": 0.03724094107747078,
              "position": [
                7.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.79705420515597,
            "cvrmse_percent": 289.8213056191877,
            "rms_normalized_rmse_percent": 40.61153429780787,
            "reference_energy": 7.61395116259191,
            "candidate_energy": 9.42584724790801,
            "relative_energy_error_percent": 23.79705420515597,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1148614156297754e-05,
              "p90": 8.073000208241865e-05,
              "p95": 0.00011438806541264057,
              "p99": 0.0001942683185916393,
              "maximum": 0.014987420290708542
            },
            "worst": {
              "global_sensor_index": 76,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022253520786762238,
              "candidate": 0.03724094107747078,
              "position": [
                7.5,
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
            "nmbe_percent": -0.2443124896080307,
            "cvrmse_percent": 5.594357227703874,
            "rms_normalized_rmse_percent": 1.250090429156463,
            "reference_energy": 5.357599610298205,
            "candidate_energy": 5.344510325307056,
            "relative_energy_error_percent": 0.2443124896080307,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 8.114147931337357e-06,
              "p99": 3.4202588722109795e-05,
              "maximum": 0.00013347197091206908
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 8,
              "sky_patch_index": 175,
              "rgb_channel": 0,
              "reference": 0.00013347197091206908,
              "candidate": 0.0,
              "position": [
                6.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 86.68843605286798,
            "cvrmse_percent": 1088.437592317888,
            "rms_normalized_rmse_percent": 45.1055683919014,
            "reference_energy": 2.192678540006437,
            "candidate_energy": 4.093477274004876,
            "relative_energy_error_percent": 86.68843605286797,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1149586157443991e-05,
              "p90": 8.263741619884968e-05,
              "p95": 0.00011705514043569565,
              "p99": 0.00019934054453187694,
              "maximum": 0.015678467229008675
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02118140272796154,
              "candidate": 0.036859869956970215,
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
            "nmbe_percent": 25.001853063269238,
            "cvrmse_percent": 316.06838275748635,
            "rms_normalized_rmse_percent": 45.10198604718029,
            "reference_energy": 7.550278150304642,
            "candidate_energy": 9.437987599311931,
            "relative_energy_error_percent": 25.001853063269238,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1108792932645883e-05,
              "p90": 8.117999823298305e-05,
              "p95": 0.00011695991270244122,
              "p99": 0.00019488722982714528,
              "maximum": 0.015678467229008675
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02118140272796154,
              "candidate": 0.036859869956970215,
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
      "bias_percent": -0.07131277386364242,
      "rms_normalized_error_percent": 0.47360239436065904,
      "absolute_error": {
        "p95": 0.20227366535384042,
        "p99": 0.25924297515034855,
        "maximum": 0.32920222147807365
      },
      "worst_index": [
        44
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 14.54684796708719,
      "rms_normalized_to_uniform_percent": 0.47360239436065904
    },
    "overcast": {
      "bias_percent": -0.04988415465587469,
      "rms_normalized_error_percent": 0.42394789159629737,
      "absolute_error": {
        "p95": 0.13208862543106073,
        "p99": 0.15214181900024415,
        "maximum": 0.231231689453125
      },
      "worst_index": [
        44
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 10.11129093170166,
      "rms_normalized_to_uniform_percent": 0.3131893275976235
    },
    "horizon": {
      "bias_percent": -2.175116208495793,
      "rms_normalized_error_percent": 15.013352253260537,
      "absolute_error": {
        "p95": 0.06468315035257159,
        "p99": 0.08667814045944414,
        "maximum": 0.12458712290044896
      },
      "worst_index": [
        7
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.20814999712077023,
      "rms_normalized_to_uniform_percent": 0.16459097938959472
    },
    "north": {
      "bias_percent": -0.26440897963064924,
      "rms_normalized_error_percent": 0.5823442902999993,
      "absolute_error": {
        "p95": 0.08620911836624144,
        "p99": 0.12532216787338257,
        "maximum": 0.13378238677978516
      },
      "worst_index": [
        36
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.807612895965576,
      "rms_normalized_to_uniform_percent": 0.19773818745348065
    },
    "east": {
      "bias_percent": 0.0583078366722409,
      "rms_normalized_error_percent": 0.6286299059138256,
      "absolute_error": {
        "p95": 0.09990565478801727,
        "p99": 0.11041590213775634,
        "maximum": 0.13216400146484375
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.6953723430633545,
      "rms_normalized_to_uniform_percent": 0.21067753344491136
    },
    "south": {
      "bias_percent": 0.10199801953256257,
      "rms_normalized_error_percent": 0.681489080296968,
      "absolute_error": {
        "p95": 0.10825655758380887,
        "p99": 0.14216330528259277,
        "maximum": 0.19050216674804688
      },
      "worst_index": [
        72
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.713351011276245,
      "rms_normalized_to_uniform_percent": 0.22679096951564656
    },
    "west": {
      "bias_percent": -0.24357968001402355,
      "rms_normalized_error_percent": 0.5673941012986348,
      "absolute_error": {
        "p95": 0.08292054831981657,
        "p99": 0.12545822739601137,
        "maximum": 0.13167953491210938
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 3.7036502361297607,
      "rms_normalized_to_uniform_percent": 0.1902064004948933
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
        "identifier": "courtyard_rooms_west_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": 0.07742421871401085,
          "cvrmse_percent": 6.746253700715048,
          "absolute_error_percentiles_lux": {
            "p50": 9.964828491210938,
            "p90": 81.5038269042969,
            "p95": 120.72136230468735,
            "p99": 223.91506347656252
          },
          "maximum_absolute_error_lux": 831.489013671875,
          "worst": {
            "sensor_index": 29,
            "position": [
              3.5,
              2.5,
              0.75
            ],
            "hour_of_year": 2960.5,
            "foton_lux": 2322.2568359375,
            "radiance_lux": 1490.767822265625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 1.1601241438356165,
            "maximum_error_percentage_points": 5.592739726027396,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.4891133098598537,
            "maximum_error_percentage_points": 1.8014537484895996,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5345419520547947,
            "maximum_error_percentage_points": 2.0297260273972597,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.5542551369863029,
            "maximum_error_percentage_points": 2.0249315068493203,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03724315068493151,
            "maximum_error_percentage_points": 0.2191780821917817,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 31.25,
          "radiance_percent": 34.375,
          "difference_percentage_points": 3.125,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": -0.03198910710254881,
          "cvrmse_percent": 6.981300575049994,
          "absolute_error_percentiles_lux": {
            "p50": 10.24273681640625,
            "p90": 80.45050048828126,
            "p95": 119.40596160888651,
            "p99": 220.12141845703127
          },
          "maximum_absolute_error_lux": 711.623046875,
          "worst": {
            "sensor_index": 26,
            "position": [
              13.5,
              5.5,
              0.75
            ],
            "hour_of_year": 5752.5,
            "foton_lux": 9565.3056640625,
            "radiance_lux": 8853.6826171875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 1.24708904109589,
            "maximum_error_percentage_points": 4.406027397260274,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.5067018073950411,
            "maximum_error_percentage_points": 1.7383375657420572,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.42596746575342437,
            "maximum_error_percentage_points": 2.057808219178085,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.42187071917808217,
            "maximum_error_percentage_points": 2.057808219178085,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.04475171232876707,
            "maximum_error_percentage_points": 0.24424657534246563,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 43.75,
          "radiance_percent": 43.75,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 0.05893964461798987,
          "cvrmse_percent": 5.079172895491504,
          "absolute_error_percentiles_lux": {
            "p50": 14.289688110351562,
            "p90": 116.02893676757816,
            "p95": 167.56233215332017,
            "p99": 285.76269348144484
          },
          "maximum_absolute_error_lux": 868.89306640625,
          "worst": {
            "sensor_index": 1,
            "position": [
              4.5,
              10.5,
              0.75
            ],
            "hour_of_year": 5843.5,
            "foton_lux": 2203.447998046875,
            "radiance_lux": 1334.554931640625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.4562671232876688,
            "maximum_error_percentage_points": 2.5461643835616385,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.2492292969733961,
            "maximum_error_percentage_points": 0.8683679600719643,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1686586757990871,
            "maximum_error_percentage_points": 0.9354794520547962,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.19051940639269352,
            "maximum_error_percentage_points": 1.0142465753424688,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.09222602739726053,
            "maximum_error_percentage_points": 0.2479452054794522,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 95.83333333333333,
          "radiance_percent": 91.66666666666667,
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
          "nmbe_percent": -0.06747041063663085,
          "cvrmse_percent": 11.80618016298845,
          "absolute_error_percentiles_lux": {
            "p50": 9.086624145507812,
            "p90": 64.94197998046879,
            "p95": 93.9165710449218,
            "p99": 171.9680270385741
          },
          "maximum_absolute_error_lux": 448.13348388671875,
          "worst": {
            "sensor_index": 1,
            "position": [
              4.5,
              -1.5,
              0.75
            ],
            "hour_of_year": 4133.5,
            "foton_lux": 1123.280029296875,
            "radiance_lux": 675.1465454101562
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 1.0417351598173517,
            "maximum_error_percentage_points": 3.643424657534247,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3692039104021531,
            "maximum_error_percentage_points": 1.0413806933137835,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.22781963470319666,
            "maximum_error_percentage_points": 0.6541095890410951,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.22781963470319658,
            "maximum_error_percentage_points": 0.6541095890410986,
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
    "numerical_correctness": "failed",
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
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004895119863014941,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004764019691783972,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.0045943921232805,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004925085616434899,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.00410958904109604,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004794520547945602,
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
      "study_preparation_seconds": 0.018957874970510602,
      "weather_seconds": 0.15187404095195234,
      "metric_reduction_seconds": 0.18426812498364598,
      "write_seconds": 0.09485937491990626,
      "total_seconds": 0.43213262502104044,
      "cold_end_to_end_seconds": 0.45109049999155104,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.046321165980771184,
      "engine_upload_seconds": 0.000887625,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.035685333190485835,
      "engine_annual_reduction_seconds": 0.005063874996267259,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.035685333190485835
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.018957874970510602,
      "weather_seconds": 0.11295266600791365,
      "metric_reduction_seconds": 0.07374454103410244,
      "write_seconds": 0.11119824997149408,
      "total_seconds": 0.29849895799998194,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.29849895799998194,
      "raw_export_seconds": 0.05188974994234741,
      "engine_upload_seconds": 0.000158375,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0060011250898242,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.020435916958376765,
      "full": 0.029725083033554256
    }
  },
  "elapsed_seconds": 266.21248704206664,
  "result_class": "accuracy_failure"
}
```
