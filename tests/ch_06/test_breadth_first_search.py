"""Tests for Chapter 6. Breadth-first search. Breadth-first search."""

from src.ch_06.breadth_first_search import Node, breadth_first_search


def test_breadth_first_search() -> None:
    """Test breadth-first search."""
    graph: dict[Node, list[Node]] = {
        "you": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": [],
    }

    expected_distance: int = 2
    expected_node = "thom"

    assert breadth_first_search(
        graph=graph,
        start="you",
        specification=lambda node: node[-1] == "m",
    ) == (expected_distance, expected_node)
