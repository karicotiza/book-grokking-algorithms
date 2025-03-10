"""Chapter 10. Greedy algorithms. Set covering problem."""


def set_covering(
    universe: set[str],
    unions: dict[str, set[str]],
) -> set[str]:
    """Perform greedy algorithm on set covering problem.

    Args:
        universe (set[str]): all elements.
        unions (dict[str, set[str]]): possible combinations.

    Returns:
        set[str]: result.

    """
    memory: set[str] = set()

    while universe:
        best_field: str | None = None
        overall_covered: set[str] = set()

        for field, elements in unions.items():
            covered: set[str] = universe & elements

            if len(covered) > len(overall_covered):
                best_field = field
                overall_covered = covered

        universe -= overall_covered

        if best_field:
            memory.add(best_field)

    return memory
