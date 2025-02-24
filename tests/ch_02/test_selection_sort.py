"""Tests for Chapter 2. Selection sort. Selection sort."""

from src.ch_02.selection_sort import (
    selection_sort,
    selection_sort_debug,
)


def test_selection_sort_on_list_of_integers() -> None:
    """Test selection sort on list of integers."""
    sequence: list = [5, 3, 6, 2, 10]
    expected: list = [2, 3, 5, 6, 10]

    assert selection_sort_debug(sequence).sequence == expected
    assert selection_sort(sequence) == expected


def test_selection_sort_on_list_of_floats() -> None:
    """Test selection sort on list of floats."""
    sequence: list = [5.6, 3.4, 6.7, 2.3, 10.11]
    expected: list = [2.3, 3.4, 5.6, 6.7, 10.11]

    assert selection_sort(sequence) == expected


def test_selection_sort_on_list_of_str() -> None:
    """Test selection sort on list of strings."""
    sequence: list = ["e", "c", "f", "b", "g"]
    expected: list = ["b", "c", "e", "f", "g"]

    assert selection_sort_debug(sequence).sequence == expected
    assert selection_sort(sequence) == expected


def test_selection_sort_on_tuple_of_integers() -> None:
    """Test selection sort on list of integers."""
    sequence: tuple[int, ...] = (5, 3, 6, 2, 10)
    expected: list = [2, 3, 5, 6, 10]

    assert selection_sort_debug(sequence).sequence == expected
    assert selection_sort(sequence) == expected


def test_selection_sort_on_tuple_of_floats() -> None:
    """Test selection sort on list of floats."""
    sequence: tuple[float, ...] = (5.6, 3.4, 6.7, 2.3, 10.11)
    expected: list = [2.3, 3.4, 5.6, 6.7, 10.11]

    assert selection_sort_debug(sequence).sequence == expected
    assert selection_sort(sequence) == expected


def test_selection_sort_on_tuple_of_str() -> None:
    """Test selection sort on list of strings."""
    sequence: tuple[str, ...] = ("e", "c", "f", "b", "g")
    expected: list = ["b", "c", "e", "f", "g"]

    assert selection_sort_debug(sequence).sequence == expected
    assert selection_sort(sequence) == expected
