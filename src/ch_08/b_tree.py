"""Chapter 8. Balanced trees. B-tree."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from collections.abc import Iterator

    from src.utils.comparable import Comparable


@dataclass(frozen=True, slots=True)
class BTreeNodeDebug:
    """B-tree node debug structure."""

    level: int
    elements: list[Comparable]


class BTreeNode:
    """B-tree node structure."""

    def __init__(self, *, is_leaf: bool = True) -> None:
        """Create new instance.

        Args:
            is_leaf (bool, optional): Is node a leaf. Defaults to True.

        """
        self.is_leaf = is_leaf
        self.keys: list[Comparable] = []
        self.children: list[Self] = []


class BTree:
    """B-tree structure."""

    def __init__(self, degree: int) -> None:
        """Create new instance.

        Args:
            degree (int): minimum degree of the tree.

        """
        self._root = BTreeNode(is_leaf=True)
        self._degree: int = degree

    def display(
        self,
        start_node: BTreeNode | None = None,
        level: int = 0,
    ) -> list[BTreeNodeDebug]:
        """Display structure.

        Args:
            start_node (BTreeNode | None, optional): start node.
                Defaults to None.
            level (int, optional): level of tree. Defaults to 0.

        Returns:
            list[BTreeNodeDebug]: level, elements.

        """
        if not start_node:
            start_node = self._root

        memory: list[BTreeNodeDebug] = [BTreeNodeDebug(level, start_node.keys)]

        if not start_node.is_leaf:
            for child in start_node.children:
                memory.extend(self.display(child, level + 1))

        return memory

    def insert(self, element: Comparable) -> None:
        """Insert element in structure.

        Args:
            element (Comparable): element.

        """
        root: BTreeNode = self._root

        if len(root.keys) == (2 * self._degree) - 1:
            temp: BTreeNode = BTreeNode(is_leaf=False)
            self._root = temp
            temp.children.append(root)
            self._split_child(temp, 0)
            self._insert_non_full(temp, element)

        else:
            self._insert_non_full(root, element)

    def __iter__(self) -> Iterator[Comparable]:
        """Iterate over structure.

        Yields:
            Iterator[Comparable]: elements.

        """
        yield from self._in_order(self._root)

    def _insert_non_full(self, node: BTreeNode, element: Comparable) -> None:
        index: int = len(node.keys) - 1

        if node.is_leaf:
            node.keys.append(element)

            while index >= 0 and element < node.keys[index]:
                node.keys[index + 1] = node.keys[index]
                index -= 1

            node.keys[index + 1] = element

        else:
            while index >= 0 and element < node.keys[index]:
                index -= 1

            index += 1

            check: bool = (
                len(node.children[index].keys) == (2 * self._degree) - 1
            )

            if check:
                self._split_child(node, index)

                if element > node.keys[index]:
                    index += 1

            self._insert_non_full(node.children[index], element)

    def _split_child(self, node: BTreeNode, index: int) -> None:
        degree: int = self._degree
        child_node: BTreeNode = node.children[index]
        new_node: BTreeNode = BTreeNode(is_leaf=child_node.is_leaf)

        node.keys.insert(index, child_node.keys[degree - 1])
        new_node.keys = child_node.keys[degree:(2 * degree) - 1]
        child_node.keys = child_node.keys[:degree-1]

        if not child_node.is_leaf:
            new_node.children = child_node.children[degree:2 * degree]
            child_node.children = child_node.children[: degree - 1]

        node.children.insert(index + 1, new_node)

    def _in_order(self, node: BTreeNode) -> Iterator[Comparable]:
        if node.is_leaf:
            yield from node.keys

        else:
            for index, _ in enumerate(node.keys):
                yield from self._in_order(node.children[index])
                yield node.keys[index]
            yield from self._in_order(node.children[-1])
