"""Tests for Chapter 11. Dynamic programming. Longest common subsequence."""

from src.ch_11.longest_common_subsequence import longest_common_subsequence


def test_longest_common_subsequence() -> None:
    """Test longest common subsequence."""
    reference: str = "fish"
    compared: str = "fosh"
    expected_result: int = 3

    assert longest_common_subsequence(reference, compared) == expected_result
