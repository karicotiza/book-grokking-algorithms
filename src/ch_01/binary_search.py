"""Chapter 1. Introduction to algorithms. Binary search algorithm."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

    from src.utils.comparable import Comparable


def binary_search(
    sequence: Sequence[Comparable],
    element: Comparable,
) -> int | None:
    """Perform binary search of element on a sequence.

    Args:
        sequence (Sequence[Comparable]): Any sequence compatible type.
        element (Comparable): Any element

    Returns:
        int | None: index of an element in sequence. None if element not in
            sequence

    """
    start: int = 0
    end: int = len(sequence) - 1

    while start <= end:
        cursor = (start + end) // 2
        guess: Comparable = sequence[cursor]

        if guess > element:
            end = cursor - 1

        elif guess < element:
            start = cursor + 1

        else:
            return cursor

    return None
