"""Tests for Chapter 5. Hash tables. Hash Table."""

from src.ch_05.hash_table import HashTable


def test_hash_table() -> None:
    """Test hash table."""
    expected_value: str = "apples"
    expected_key: float = 0.67

    hash_table: HashTable[str, float] = HashTable()
    hash_table[expected_value] = expected_key

    assert hash_table[expected_value] == expected_key
