"""Chapter 7. Trees. Depth first search."""
from __future__ import annotations

from typing import Callable, TypeVar

Node = TypeVar("Node")


def depth_first_search(
    graph: dict[Node, list[Node]],
    start: Node,
    callback: Callable[[Node], None],
) -> None:
    """Perform breadth-first search on a graph.

    Args:
        graph (dict[Node, list[Node]]): graph defined as dict of Nodes.
        start (Node): start node.
        callback (Callable[[], None]): any callback.

    Returns:
        int | None: distance from start to node that satisfies the
            specification. None if no such node exists.

    """
    for node in graph[start]:
        if node in graph:
            depth_first_search(graph, node, callback)

        else:
            callback(node)
