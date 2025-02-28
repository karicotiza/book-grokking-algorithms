"""Tests for Chapter 8.Balanced trees. B-tree."""

from src.ch_08.b_tree import BTree, BTreeNodeDebug


def test_breadth_first_search() -> None:
    """Test breadth-first search."""
    btree: BTree = BTree(3)

    keys: list[int] = [10, 20, 5, 6, 12, 30, 7, 17]
    expected_tree = [
        BTreeNodeDebug(0, [10]),
        BTreeNodeDebug(1, [5, 6, 7]),
        BTreeNodeDebug(1, [12, 17, 20, 30]),
    ]

    for key in keys:
        btree.insert(key)

    assert btree.display() == expected_tree
    assert keys[4] in btree
    assert list(btree) == sorted(keys)
