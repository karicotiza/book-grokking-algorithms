"""Comparable protocol.

I made this for:
* Use not only integers in binary search.
"""

from typing import Protocol, Self


class Comparable(Protocol):
    """Protocol for object that can be compared."""

    def __lt__(self, other: Self) -> bool:
        """Check if self is less than other.

        Args:
            other (Self): other value that follows same Protocol.

        Returns:
            bool: True if check is success.

        """
        ...

    def __le__(self, other: Self) -> bool:
        """Check if self is less or equal than other.

        Args:
            other (Self): other value that follows same Protocol.

        Returns:
            bool: True if check is success.

        """
        ...

    def __gt__(self, other: Self) -> bool:
        """Check if self is greater than other.

        Args:
            other (Self): other value that follows same Protocol.

        Returns:
            bool: True if check is success.

        """
        ...

    def __ge__(self, other: Self) -> bool:
        """Check if self is greater or equal than other.

        Args:
            other (Self): other value that follows same Protocol.

        Returns:
            bool: True if check is success.

        """
        ...

    def __eq__(self, other: object) -> bool:
        """Check if self is equal with other.

        Args:
            other (Self): other value that follows same Protocol.

        Returns:
            bool: True if check is success.

        """
        ...
