"""Tests for Chapter 9. Dijkstra's algorithm. Dijkstra algorithm."""

from src.ch_09.dijkstra import DijkstraResult, dijkstra


def test_dijkstra_algorithm() -> None:
    """Test dijkstra algorithm."""
    expected_length: int = 6
    expected_path: list[str] = ["start", "b", "a", "fin"]
    graph: dict[str, dict[str, float]] = {
        "start": {
            "a": 6,
            "b": 2,
        },
        "a": {
            "fin": 1,
        },
        "b": {
            "a": 3,
            "fin": 5,
        },
        "fin": {},
    }

    result: DijkstraResult = dijkstra(graph, "start", "fin")

    assert result.length == expected_length
    assert result.path == expected_path
