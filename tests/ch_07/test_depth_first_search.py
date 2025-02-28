"""Tests for Chapter 7. Trees. Depth-first search."""

from src.ch_07.depth_first_search import Node, depth_first_search


def test_breadth_first_search() -> None:
    """Test breadth-first search."""
    graph: dict[Node, list[Node]] = {
        "pics": ["2001", "odyssey.png"],
        "2001": ["a.png", "space.png"],
    }

    memory: list[Node] = []
    expected: list[Node] = ["a.png", "space.png", "odyssey.png"]

    depth_first_search(
        graph=graph,
        start="pics",
        callback=lambda node: memory.append(node),
    )

    assert memory == expected
