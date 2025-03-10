"""Chapter 11. Dynamic programming. Longest common subsequence."""


def longest_common_subsequence(
    reference: str,
    compared: str,
) -> int:
    """Perform longest common subsequence algorithm.

    Args:
        reference (str): reference.
        compared (str): compared.

    Returns:
        int: score.

    """
    reference_length: int = len(reference)
    compared_length: int = len(compared)

    matrix: list[list[int]] = _create_empty_matrix(
        rows=reference_length,
        columns=compared_length,
    )

    for row in range(reference_length + 1):
        for column in range(compared_length + 1):
            if row == 0 or column == 0:
                matrix[row][column] = 0
            elif reference[row - 1] == compared[column - 1]:
                matrix[row][column] = matrix[row - 1][column - 1] + 1
            else:
                matrix[row][column] = max(
                    matrix[row - 1][column],
                    matrix[row][column - 1],
                )

    return matrix[reference_length][compared_length]


def _create_empty_matrix(
    rows: int,
    columns: int,
) -> list[list[int]]:
    return [
        [0 for _ in range(columns + 1)]
        for _ in range(rows + 1)
    ]
