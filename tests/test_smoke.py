"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import templateforge


def test_version_is_set() -> None:
    assert templateforge.__version__
