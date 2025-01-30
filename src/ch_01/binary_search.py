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
        lower_bound (int): Value of lower bound.
        upper_bound (int): Value of upper bound.
        cursor (int): Cursor value.
        index (int | None): Final result of the algorithm's operation.

    """

    iterations: int = 0
    time_in_nanoseconds: int = 0

    lower_bound: int = 0
    upper_bound: int = 0
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
    lower_bound: int = 0
    upper_bound: int = len(sequence) - 1

    while lower_bound <= upper_bound:
        cursor = (lower_bound + upper_bound) // 2
        guess: Comparable = sequence[cursor]

        if guess > element:
            upper_bound = cursor - 1

        elif guess < element:
            lower_bound = cursor + 1

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
    lower_bound: int = 0
    upper_bound: int = len(sequence) - 1

    while lower_bound < upper_bound:
        cursor = (lower_bound + upper_bound) // 2
        guess: Comparable = sequence[cursor]

        if guess < element:
            lower_bound = cursor + 1

        else:
            upper_bound = cursor

    if (
        lower_bound < len(sequence)
        and sequence[lower_bound] == element
    ):
        return lower_bound

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
    debug.upper_bound = len(sequence) - 1

    while debug.lower_bound <= debug.upper_bound:
        debug.iterations += 1
        debug.cursor = (debug.lower_bound + debug.upper_bound) // 2
        guess: Comparable = sequence[debug.cursor]
        log(str(debug.as_dict()), verbose=verbose)

        if guess > element:
            debug.upper_bound = debug.cursor - 1

        elif guess < element:
            debug.lower_bound = debug.cursor + 1

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
    debug.upper_bound = len(sequence) - 1

    while debug.lower_bound < debug.upper_bound:
        debug.iterations += 1
        debug.cursor = (debug.lower_bound + debug.upper_bound) // 2
        guess: Comparable = sequence[debug.cursor]
        log(str(debug.as_dict()), verbose=verbose)

        if guess < element:
            debug.lower_bound = debug.cursor + 1

        else:
            debug.upper_bound = debug.cursor

    if (
        debug.lower_bound < len(sequence)
        and sequence[debug.lower_bound] == element
    ):
        debug.index = debug.lower_bound
        debug.stop_timer()
        log(str(debug.as_dict()), verbose=verbose)
        return debug

    debug.stop_timer()
    log(str(debug.as_dict()), verbose=verbose)
    return debug
