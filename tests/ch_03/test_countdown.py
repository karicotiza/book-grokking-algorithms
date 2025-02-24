"""Tests for Chapter 3. Recursion. Countdown."""

from src.ch_03.countdown import countdown


def test_countdown() -> None:
    """Test countdown."""
    memory: list[int] = []
    expected: list[int] = [5, 5, 5, 5, 5]

    countdown(
        start=5,
        callback=lambda: memory.append(5),
    )

    assert memory == expected
