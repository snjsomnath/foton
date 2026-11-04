"""Checks on the Grasshopper component sources that need no Rhino."""

import struct
from pathlib import Path

import pytest

from scripts import build_grasshopper, package_yak

ROOT = Path(__file__).resolve().parents[2]

# The example definition wires ports by position, so their order is fixed.
EXPECTED_PORTS = {
    "Foton Settings": (
        ["executable_", "backend_", "python_", "install_", "_check"],
        ["report", "executable", "engine_version", "protocol_version", "backend", "capabilities", "cache_folder"],
    ),
    "Foton Annual Daylight": (
        ["_model", "_wea", "schedule_", "north_", "thresholds_", "grid_filter_", "quality_", "sky_density_",
         "backend_", "output_folder_", "executable_", "reuse_", "direct_samples_", "indirect_samples_",
         "bounces_", "seed_", "live_", "_run"],
        ["report", "results", "DA", "cDA", "UDI", "UDI_low", "UDI_up", "sDA", "grid_ids", "room_ids",
         "manifest", "timings", "timings_text", "warnings", "folder"],
    ),
    "Foton Annual Results": (
        ["_manifest", "_load"],
        ["report", "results", "DA", "cDA", "UDI", "UDI_low", "UDI_up", "sDA", "grid_ids", "room_ids",
         "manifest", "timings", "timings_text", "warnings", "folder"],
    ),
    "Foton Daylight Factor": (
        ["_model", "grid_filter_", "quality_", "sky_density_", "backend_", "output_folder_", "executable_",
         "bounces_", "live_", "_run"],
        ["report", "results", "DF", "mean_DF", "grid_ids", "room_ids", "timings_text", "folder"],
    ),
}


def png_size(path):
    data = Path(path).read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    return struct.unpack(">II", data[16:24])


@pytest.mark.parametrize("name", build_grasshopper.COMPONENT_NAMES)
def test_component_ports_come_from_the_docstring(name):
    spec = build_grasshopper.component_spec(name)
    inputs, outputs = EXPECTED_PORTS[name]
    assert [port for port, _ in spec["inputs"]] == inputs
    assert [port for port, _ in spec["outputs"]] == outputs
    for port, hint in spec["inputs"] + spec["outputs"]:
        assert len(hint) > 15, port
        assert "``" not in hint, port


@pytest.mark.parametrize("name", build_grasshopper.COMPONENT_NAMES)
def test_component_has_help_icon_and_ribbon_place(name):
    spec = build_grasshopper.component_spec(name)
    source = (ROOT / "grasshopper_foton/components" / (name + ".py")).read_text()
    assert spec["category"] == "HB-Foton"
    assert spec["subcategory"] in ("Settings", "Recipes", "Results")
    assert len(spec["description"]) > 60
    assert source.startswith("# Foton: GPU daylight simulation for Grasshopper.")
    assert "MIT licence" in source.splitlines()[1]
    assert "ghenv.Component.Message = COMPONENT_VERSION" in source
    assert png_size(ROOT / spec["icon"]) == (24, 24)


def test_component_version_matches_the_release():
    from grasshopper_foton import foton_gh

    assert build_grasshopper.component_version() == foton_gh.COMPONENT_VERSION
    assert foton_gh.COMPONENT_VERSION == package_yak.project_version(ROOT)


def test_package_icon_is_listed_in_the_yak_manifest():
    text = (ROOT / "grasshopper_foton/yak/manifest.yml").read_text()
    assert "\nicon: icon.png\n" in text
    assert png_size(ROOT / "grasshopper_foton/yak/icon.png") == (128, 128)
