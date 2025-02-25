"""Chapter 4. Quicksort. Divide and conquer."""

from collections.abc import Sequence

from src.utils.comparable import Comparable


def quicksort(sequence: Sequence[Comparable]) -> Sequence[Comparable]:
    """Perform quicksort on sequence.

    Args:
        sequence (Sequence[Comparable]): Any sequence compatible type.

    Returns:
        Sequence[Comparable]: sorted list.

    """
    if len(sequence) < 2:
        return sequence

    pivot: Comparable = sequence[0]
    less: list[Comparable] = [
        element for element in sequence[1:] if element <= pivot
    ]

    greater: list[Comparable] = [
        element for element in sequence[1:] if element > pivot
    ]

    return [*quicksort(less), pivot, *quicksort(greater)]
