from pathlib import Path

import pytest

from scripts import package_yak

ROOT = Path(__file__).resolve().parents[2]


def test_manifest_version_matches_pyproject():
    assert package_yak.manifest_version(ROOT) == package_yak.project_version(ROOT)


def test_manifest_names_the_package():
    text = (ROOT / "grasshopper_foton/yak/manifest.yml").read_text()
    assert "\nname: foton\n" in text
    assert "url: https://github.com/snjsomnath/foton" in text


def test_stage_copies_the_verified_build(tmp_path):
    pytest.importorskip("honeybee")
    staged = package_yak.stage(tmp_path / "yak", ROOT)
    assert staged == sorted(package_yak.STAGED)
    for name in (*package_yak.USER_OBJECTS, "Foton First Analysis.gh", "Foton Interactive Demo.gh"):
        expected = (ROOT / "grasshopper_foton/distribution" / name).read_bytes()
        assert (tmp_path / "yak" / name).read_bytes() == expected
