"""Tests for Chapter 10. Greedy algorithms. Set covering problem."""

from src.ch_10.set_covering import set_covering


def test_set_covering() -> None:
    """Test set covering problem."""
    states_needed: set[str] = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

    stations: dict[str, set[str]] = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"},
    }

    expected_result: set[str] = {"ktwo", "kthree", "kone", "kfive"}

    assert set_covering(states_needed, stations) == expected_result
