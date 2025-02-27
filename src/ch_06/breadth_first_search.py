"""Chapter 6. Breadth-first search. Breadth-first search."""
from __future__ import annotations

from collections import deque
from typing import Callable, TypeVar

Node = TypeVar("Node")


def breadth_first_search(
    graph: dict[Node, list[Node]],
    start: Node,
    specification: Callable[[Node], bool],
) -> tuple[int | None, Node | None]:
    """Perform breadth-first search on a graph.

    Args:
        graph (dict[Node, list[Node]]): graph defined as dict of Nodes.
        start (Node): start node.
        specification (Callable[[Node], bool]): specification that must be
            true.

    Returns:
        int | None: distance from start to node that satisfies the
            specification. None if no such node exists.

    """
    search_queue: deque[tuple[Node, int]] = deque([(start, 0)])
    searched: set[Node] = set()

    while search_queue:
        current_node, distance = search_queue.popleft()

        if current_node not in searched and specification(current_node):
            return (distance, current_node)

        searched.add(current_node)

        for neighbor in graph[current_node]:
            search_queue.append((neighbor, distance + 1))

    return None, None
