"""Chapter 3. Recursion. Factorial."""

from functools import lru_cache


@lru_cache()
def factorial(number: int) -> int:
    """Get factorial of a number.

    Args:
        number (int): number.

    Returns:
        int: value.

    """
    if number == 1:
        return 1

    return number * factorial(number - 1)
