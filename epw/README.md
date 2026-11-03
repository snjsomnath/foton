# Weather files

Hourly EPW files used by the examples and the validation suite. All three are
public weather data from the EnergyPlus weather collection
(https://energyplus.net/weather, mirrored at energyplus-weather.s3.amazonaws.com).

| File | Station | Source | Role | SHA-256 |
| --- | --- | --- | --- | --- |
| `gothenburg.epw` | Gothenburg-Landvetter AP, Sweden (WMO 025260) | TMYx | Default: mixed, mostly overcast northern climate; shipped with the Grasshopper package | `98246499f5e0508387c41d22a6f492c76a8ec52c17ceb31712069871a196bcee` |
| `phoenix.epw` | Phoenix Sky Harbor Intl AP, AZ, USA (WMO 722780) | TMY3 | Sunny climate for the teaching-category climate runs | `d6e21c48181f8f154e82514cc5fb46924d2844a9b5984ce6959d4ba6c95ddafe` |
| `seattle.epw` | Seattle-Tacoma Intl AP, WA, USA (WMO 727930) | TMY3 | Overcast climate for the teaching-category climate runs | `67ef83472f8207a15e51875aa6e0f8ccf8b790e4fa9c78142c709d765ff48de1` |

Run the suite under another climate with `--weather epw/<file>.epw`; the
report records the file path and its hash.
