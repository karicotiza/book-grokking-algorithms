"""Chapter 9. Dijkstra's algorithm. Dijkstra algorithm."""
from __future__ import annotations

from dataclasses import dataclass
from math import inf


@dataclass(frozen=True, slots=True)
class DijkstraResult:
    """Dijkstra result structure."""

    path: list[str]
    length: float


def dijkstra(
    graph: dict[str, dict[str, float]],
    start: str,
    end: str,
) -> DijkstraResult:
    """Perform dijkstra algorithm.

    Args:
        graph (dict[str, dict[str, int]]): graph.
        start (str): start node.
        end (str): end node.

    Returns:
        DijkstraResult: result.

    """
    costs: dict[str, float] = _calculate_costs(graph, start)
    parents: dict[str, str | None] = _calculate_parents(graph, start)
    processed: set[str] = set()
    path: list[str] = [start]

    node: str | None = _find_lowest_cost_node(costs, processed)

    while node is not None:
        path.append(node)
        _update_neighbors(node, graph, costs, parents)
        processed.add(node)
        node = _find_lowest_cost_node(costs, processed)

    return DijkstraResult(
        path=path,
        length=costs[end],
    )


def _calculate_costs(
    graph: dict[str, dict[str, float]],
    node: str,
) -> dict[str, float]:
    memory: dict[str, float] = dict(graph[node].items())

    for key in graph:
        if key != node and key not in memory:
            memory[key] = inf

    return memory


def _calculate_parents(
    graph: dict[str, dict[str, float]],
    node: str,
) -> dict[str, str | None]:
    memory: dict[str, str | None] = {key: node for key in graph[node]}

    for key in graph:
        if key != node and key not in memory:
            memory[key] = None

    return memory


def _find_lowest_cost_node(
    costs: dict[str, float],
    processed: set[str],
) -> str | None:
    lowest_cost: float = inf
    lowest_cost_node: str | None = None

    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def _update_neighbors(
    node: str,
    graph: dict[str, dict[str, float]],
    costs: dict[str, float],
    parents: dict[str, str | None],
) -> None:
    neighbors: dict[str, float] = graph[node]
    cost: float = costs[node]

    for neighbor, neighbor_cost in neighbors.items():
        new_cost: float = cost + neighbor_cost

        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[node] = node
