"""Tests for Chapter 1. Introduction to algorithms. Binary search."""

from src.ch_01.binary_search import binary_search, binary_search_debug


def test_binary_search_on_integers() -> None:
    """Test binary search on integers."""
    sequence: list = [1, 3, 5, 7, 9]

    assert binary_search(sequence, 3) == 1
    assert binary_search(sequence, -1) is None

    assert binary_search_debug(sequence, 3).index == 1
    assert binary_search_debug(sequence, -1).index is None


def test_binary_search_on_floats() -> None:
    """Test binary search on floats."""
    sequence: list = [0.5, 1.03, 2.55, 3.47, 4.99]

    assert binary_search(sequence, 2.55) == 2
    assert binary_search(sequence, -5) is None

    assert binary_search_debug(sequence, 2.55).index == 2
    assert binary_search_debug(sequence, -5).index is None


def test_binary_search_on_strings() -> None:
    """Test binary search on strings."""
    sequence: list = ["a", "b", "c", "d", "e"]

    assert binary_search(sequence, "a") == 0
    assert binary_search(sequence, "d") == 3

    assert binary_search_debug(sequence, "a").index == 0
    assert binary_search_debug(sequence, "d").index == 3
