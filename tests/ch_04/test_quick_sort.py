"""Tests for Chapter 4. Quicksort. Quicksort."""

from src.ch_04.quicksort import quicksort


def test_quicksort() -> None:
    """Test quicksort."""
    sequence: list[int] = [10, 5, 2, 3]
    expected: list[int] = [2, 3, 5, 10]

    assert quicksort(sequence) == expected
