"""Chapter 1. Introduction to algorithms. Binary search algorithm."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from time import perf_counter_ns
from typing import TYPE_CHECKING

from src.utils.log import log

if TYPE_CHECKING:
    from collections.abc import Sequence

    from src.utils.comparable import Comparable


@dataclass
class BinarySearchDebug:
    """Debug structure for binary search algorithm.

    Args:
        iterations (int): Number of iterations required to complete the
            algorithm.
        time_in_nanoseconds (int): Time in nanoseconds required to complete
            the algorithm.
        left_border (int): Value of left border.
        right_border (int): Value of right border.
        cursor (int): Cursor value.
        index (int | None): Final result of the algorithm's operation.

    """

    iterations: int = 0
    time_in_nanoseconds: int = 0

    left_border: int = 0
    right_border: int = 0
    cursor: int = 0

    index: int | None = None

    def start_timer(self) -> None:
        """Start timer for algorithm speed measure."""
        self._start_time_in_nanoseconds: int = perf_counter_ns()

    def stop_timer(self) -> None:
        """Stop timer for algorithm speed measure."""
        if self._start_time_in_nanoseconds:
            self.time_in_nanoseconds = (
                perf_counter_ns() - self._start_time_in_nanoseconds
            )

    def as_dict(self) -> dict[str, int]:
        """Get debug information. mostly for printing.

        Returns:
            dict[str, int]: dict of attributes from this structure.

        """
        return asdict(self)


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
    left_border: int = 0
    right_border: int = len(sequence) - 1

    while left_border <= right_border:
        cursor = (left_border + right_border) // 2
        guess: Comparable = sequence[cursor]

        if guess > element:
            right_border = cursor - 1

        elif guess < element:
            left_border = cursor + 1

        else:
            return cursor

    return None


def lower_bound_binary_search(
    sequence: Sequence[Comparable],
    element: Comparable,
) -> int | None:
    """Perform lower bound binary search of element on a sequence.

    Args:
        sequence (Sequence[Comparable]): Any sequence compatible type.
        element (Comparable): Any element

    Returns:
        int | None: index of an element in sequence. None if element not in
            sequence

    """
    left_border: int = 0
    right_border: int = len(sequence) - 1

    while left_border < right_border:
        cursor = (left_border + right_border) // 2
        guess: Comparable = sequence[cursor]

        if guess < element:
            left_border = cursor + 1

        else:
            right_border = cursor

    if (
        left_border < len(sequence)
        and sequence[left_border] == element
    ):
        return left_border

    return None


def binary_search_debug(
    sequence: Sequence[Comparable],
    element: Comparable,
    *,
    verbose: bool = False,
) -> BinarySearchDebug:
    """Perform binary search of element on a sequence, with debug.

    Please note that debug version is slower than original.

    Args:
        sequence (Sequence[Comparable]): Any sequence compatible type.
        element (Comparable): Any element
        verbose (bool): Print debug to console at every step.

    Returns:
        BinarySearchDebug: debug structure for binary search algorithm.

    """
    debug: BinarySearchDebug = BinarySearchDebug()
    debug.start_timer()
    debug.right_border = len(sequence) - 1

    while debug.left_border <= debug.right_border:
        debug.iterations += 1
        debug.cursor = (debug.left_border + debug.right_border) // 2
        guess: Comparable = sequence[debug.cursor]
        log(str(debug.as_dict()), verbose=verbose)

        if guess > element:
            debug.right_border = debug.cursor - 1

        elif guess < element:
            debug.left_border = debug.cursor + 1

        else:
            debug.index = debug.cursor
            debug.stop_timer()
            log(str(debug.as_dict()), verbose=verbose)

            return debug

    debug.stop_timer()
    log(str(debug.as_dict()), verbose=verbose)
    return debug


def lower_bound_binary_search_debug(
    sequence: Sequence[Comparable],
    element: Comparable,
    *,
    verbose: bool = False,
) -> BinarySearchDebug:
    """Perform lower bound binary search of element on a sequence, with debug.

    Please note that debug version is slower than original.

    Args:
        sequence (Sequence[Comparable]): Any sequence compatible type.
        element (Comparable): Any element
        verbose (bool): Print debug to console at every step.

    Returns:
        BinarySearchDebug: debug structure for binary search algorithm.

    """
    debug: BinarySearchDebug = BinarySearchDebug()
    debug.start_timer()
    debug.right_border = len(sequence) - 1

    while debug.left_border < debug.right_border:
        debug.iterations += 1
        debug.cursor = (debug.left_border + debug.right_border) // 2
        guess: Comparable = sequence[debug.cursor]
        log(str(debug.as_dict()), verbose=verbose)

        if guess < element:
            debug.left_border = debug.cursor + 1

        else:
            debug.right_border = debug.cursor

    if (
        debug.left_border < len(sequence)
        and sequence[debug.left_border] == element
    ):
        debug.index = debug.left_border
        debug.stop_timer()
        log(str(debug.as_dict()), verbose=verbose)
        return debug

    debug.stop_timer()
    log(str(debug.as_dict()), verbose=verbose)
    return debug
