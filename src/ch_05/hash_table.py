"""Chapter 5. Hash tables. Hash table."""

from typing import Self, TypeVar

KeyType = TypeVar("KeyType")
ValueType = TypeVar("ValueType")


class HashTableNode:
    """Hash table node."""

    def __init__(self, key: KeyType, value: ValueType) -> None:
        """Make new instance.

        Args:
            key (KeyType): key.
            value (ValueType): value.

        """
        self.key: KeyType = key
        self.value: ValueType = value
        self.next: Self | None = None


class HashTable[KeyType, ValueType]:
    """Hash table structure."""

    _capacity: int = 4

    def __init__(self) -> None:
        """Make new instance."""
        self._size: int = 0
        self._table: list[HashTableNode | None] = [
            None for _ in range(self._capacity)
        ]

    def __setitem__(self, key: KeyType, value: ValueType) -> None:
        """Set item.

        Args:
            key (KeyType): key.
            value (ValueType): value.

        """
        index: int = self._hash(key)

        if self._table[index] is None:
            self._table[index] = HashTableNode(key, value)
            self._size += 1

        else:
            current: HashTableNode | None = self._table[index]

            while current:
                if current.key == key:
                    current.value = value
                    return

                current = current.next

            new_node: HashTableNode = HashTableNode(key, value)
            new_node.next = self._table[index]
            self._table[index] = new_node
            self._size += 1

    def __getitem__(self, key: KeyType) -> ValueType:
        """Get item.

        Args:
            key (KeyType): key.

        Raises:
            KeyError: on key not in self._table.

        Returns:
            ValueType: value.

        """
        index: int = self._hash(key)

        current: HashTableNode | None = self._table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def _hash(self, key: KeyType) -> int:
        return hash(key) % self._capacity
