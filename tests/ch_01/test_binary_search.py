"""Tests for Chapter 1. Introduction to algorithms. Binary search."""

from math import log2

from src.ch_01.binary_search import (
    binary_search,
    binary_search_debug,
    lower_bound_binary_search,
    lower_bound_binary_search_debug,
)


def test_binary_search_on_integers() -> None:
    """Test binary search on integers."""
    sequence: list = [1, 3, 5, 7, 9]

    assert binary_search(sequence, 3) == 1
    assert binary_search(sequence, -1) is None

    assert lower_bound_binary_search(sequence, 3) == 1
    assert lower_bound_binary_search(sequence, -1) is None

    assert binary_search_debug(sequence, 3).index == 1
    assert binary_search_debug(sequence, -1).index is None

    assert lower_bound_binary_search_debug(sequence, 3).index == 1
    assert lower_bound_binary_search_debug(sequence, -1).index is None


def test_binary_search_on_floats() -> None:
    """Test binary search on floats."""
    sequence: list = [0.5, 1.03, 2.55, 3.47, 4.99]

    assert binary_search(sequence, 2.55) == 2
    assert binary_search(sequence, -5) is None

    assert lower_bound_binary_search(sequence, 2.55) == 2
    assert lower_bound_binary_search(sequence, -5) is None

    assert binary_search_debug(sequence, 2.55).index == 2
    assert binary_search_debug(sequence, -5).index is None

    assert lower_bound_binary_search_debug(sequence, 2.55).index == 2
    assert lower_bound_binary_search_debug(sequence, -5).index is None


def test_binary_search_on_strings() -> None:
    """Test binary search on strings."""
    sequence: list = ["a", "b", "c", "d", "e"]

    assert binary_search(sequence, "a") == 0
    assert binary_search(sequence, "d") == 3

    assert lower_bound_binary_search(sequence, "a") == 0
    assert lower_bound_binary_search(sequence, "d") == 3

    assert binary_search_debug(sequence, "a").index == 0
    assert binary_search_debug(sequence, "d").index == 3

    assert lower_bound_binary_search_debug(sequence, "a").index == 0
    assert lower_bound_binary_search_debug(sequence, "d").index == 3


def test_exercise_1_1() -> None:
    """Test exercise 1.1."""
    amount: int = 128
    sequence: list[int] = list(range(1, amount + 1))
    expected_iterations: int = int(log2(amount))

    assert len(sequence) == amount

    assert sequence[0] == 1
    assert sequence[-1] == amount

    assert expected_iterations == 7

    # First element will need log2(n) steps.
    assert binary_search_debug(
        sequence, sequence[0],
    ).iterations == expected_iterations

    # Last element will need log2(n) + 1 steps.
    assert binary_search_debug(
        sequence, sequence[-1],
    ).iterations == expected_iterations + 1

    # But "lower bound binary search" will need log2(n) for that.
    assert lower_bound_binary_search_debug(
        sequence, sequence[-1],
    ).iterations == expected_iterations

    # Element that not in a sequence will need log2(n) + 1 steps.
    assert binary_search_debug(
        sequence, sequence[-1] + 1,
    ).iterations == expected_iterations + 1

    # But "lower bound binary search" will need log2(n) for that.
    assert lower_bound_binary_search_debug(
        sequence, sequence[-1] + 1,
    ).iterations == expected_iterations


def test_exercise_1_2() -> None:
    """Test exercise 1.2."""
    amount: int = 128 * 2
    sequence: list[int] = list(range(1, amount + 1))
    expected_iterations: int = int(log2(amount))

    assert len(sequence) == amount

    assert sequence[0] == 1
    assert sequence[-1] == amount

    assert expected_iterations == 8

    assert binary_search_debug(
        sequence, sequence[0],
    ).iterations == expected_iterations

    assert binary_search_debug(
        sequence, sequence[-1],
    ).iterations == expected_iterations + 1

    assert lower_bound_binary_search_debug(
        sequence, sequence[-1],
    ).iterations == expected_iterations

    assert binary_search_debug(
        sequence, sequence[-1] + 1,
    ).iterations == expected_iterations + 1

    assert lower_bound_binary_search_debug(
        sequence, sequence[-1] + 1,
    ).iterations == expected_iterations
