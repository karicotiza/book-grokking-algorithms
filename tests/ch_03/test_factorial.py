"""Tests for Chapter 3. Recursion. Factorial."""

from src.ch_03.factorial import factorial


def test_factorial() -> None:
    """Test factorial."""
    expected: int = 3628800

    assert factorial(10) == expected
