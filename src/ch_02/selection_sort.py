"""Chapter 2. Selection sort. Selection sort algorithm."""
from __future__ import annotations

from copy import copy
from dataclasses import asdict, dataclass, field
from time import perf_counter_ns
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

    from src.utils.comparable import Comparable


@dataclass
class SelectionSortDebug:
    """Debug structure for selection sort algorithm.

    Args:
        iterations (int): Number of iterations required to complete the
            algorithm.
        time_in_nanoseconds (int): Time in nanoseconds required to complete
            the algorithm.
        sequence (Sequence[Comparable]): Final result of the algorithm's
            operation.

    """

    iterations: int = 0
    time_in_nanoseconds: int = 0

    smallest_element: Comparable = 0
    smallest_element_index: int = 0

    sequence: Sequence[Comparable] = field(default_factory=list)

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


def _find_smallest(sequence: Sequence[Comparable]) -> int:
    smallest_element: Comparable = sequence[0]
    smallest_element_index: int = 0

    for index, _ in enumerate(sequence):
        if sequence[index] < smallest_element:
            smallest_element = sequence[index]
            smallest_element_index = index

    return smallest_element_index


def selection_sort(sequence: Sequence[Comparable]) -> list[Comparable]:
    """Perform selection sort on sequence.

    Args:
        sequence (Sequence[Comparable]): Any sequence compatible type.

    Returns:
        list[Comparable]: sorted list.

    """
    memory: list[Comparable] = []
    copied_sequence: list[Comparable] = copy(list(sequence))

    while copied_sequence:
        smallest: int = _find_smallest(copied_sequence)
        memory.append(copied_sequence.pop(smallest))

    return memory


def selection_sort_debug(sequence: Sequence[Comparable]) -> SelectionSortDebug:
    """Perform selection sort on sequence.

    Args:
        sequence (Sequence[Comparable]): Any sequence compatible type.

    Returns:
        SelectionSortDebug: selection sort debug.

    """
    debug: SelectionSortDebug = SelectionSortDebug()
    memory: list[Comparable] = []
    copied_sequence: list[Comparable] = copy(list(sequence))

    debug.start_timer()

    while copied_sequence:
        debug.smallest_element = copied_sequence[0]
        debug.smallest_element_index = 0

        for index, _ in enumerate(copied_sequence):
            debug.iterations += 1
            if copied_sequence[index] < debug.smallest_element:
                debug.smallest_element = copied_sequence[index]
                debug.smallest_element_index = index

        memory.append(copied_sequence.pop(debug.smallest_element_index))

    debug.stop_timer()
    debug.sequence = memory

    return debug
