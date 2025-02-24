"""Chapter 4. Quicksort. Divide and conquer."""

from collections.abc import Sequence


def recursive_sum(sequence: Sequence[float]) -> float:
    """Get sum of sequence using recursion.

    Args:
        sequence (Sequence[float]): sequence.

    Returns:
        float: sum of sequence elements.

    """
    if len(sequence) == 1:
        return sequence[0]

    return sequence[0] + recursive_sum(sequence[1:])


def recursive_len(sequence: Sequence[float]) -> int:
    """Get len of sequence using recursion.

    Args:
        sequence (Sequence[float]): sequence.

    Returns:
        int: len of sequence elements.

    """
    if len(sequence) == 1:
        return 1

    return 1 + recursive_len(sequence[1:])


def recursive_max(sequence: Sequence[float]) -> float:
    """Get max of sequence using recursion.

    Args:
        sequence (Sequence[float]): sequence.

    Returns:
        float: max of sequence elements.

    """
    if len(sequence) == 2:
        if sequence[0] > sequence[1]:
            return sequence[0]

        return sequence[1]

    sub_max: float = recursive_max(sequence[1:])

    if sequence[0] > sub_max:
        return sequence[0]

    return sub_max
