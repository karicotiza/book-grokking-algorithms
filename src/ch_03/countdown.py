"""Chapter 3. Recursion. Countdown."""

from typing import Callable


def countdown(start: int, callback: Callable[[], None]) -> None:
    """Do something n times.

    Args:
        start (int): start value.
        callback (Callable[[], None]): any callable.

    """
    callback()

    if start <= 1:
        return

    countdown(start - 1, callback)
