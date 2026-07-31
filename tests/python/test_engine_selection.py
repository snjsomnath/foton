import pytest


def test_default_engine_uses_a_known_backend():
    from foton import Engine

    capabilities = Engine().capabilities()
    assert capabilities["name"].split(" device:", 1)[0] in {
        "Metal",
        "Vulkan",
        "deterministic-cpu-reference",
    }


def test_unknown_backend_is_rejected():
    from foton import Engine

    with pytest.raises(ValueError, match="unknown backend"):
        Engine({"backend": "unsupported"})


def test_legacy_import_remains_compatible():
    from daylight_engine import Engine as LegacyEngine
    from foton import Engine

    assert LegacyEngine is Engine
