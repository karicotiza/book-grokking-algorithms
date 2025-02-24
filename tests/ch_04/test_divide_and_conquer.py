"""Tests for Chapter 4. Recursion. Divide and conquer."""

from src.ch_04.divide_and_conquer import (
    recursive_len,
    recursive_max,
    recursive_sum,
)


def test_exercise_4_1() -> None:
    """Test exercise 4.1."""
    sequence: list[int] = [2, 4, 6]
    expected: int = 12

    assert recursive_sum(sequence) == expected


def test_exercise_4_2() -> None:
    """Test exercise 4.2."""
    sequence: list[int] = [2, 4, 6]
    expected: int = 3

    assert recursive_len(sequence) == expected


def test_exercise_4_3() -> None:
    """Test exercise 4.3."""
    sequence: list[int] = [2, 4, 6]
    expected: int = 6

    assert recursive_max(sequence) == expected
