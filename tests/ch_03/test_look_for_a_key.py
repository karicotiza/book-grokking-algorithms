"""Tests for Chapter 3. Recursion. Look for a key."""

from src.ch_03.look_for_a_key import (
    Box,
    Key,
    Stuff,
    look_for_key_loop,
    look_for_key_recursion,
)


def test_look_for_a_key() -> None:
    """Test selection sort on list of integers."""
    expected_identifier: int = 9
    main_box: Box = Box(
        identifier=1,
        elements=[
            Box(
                identifier=2,
                elements=[Stuff(), Stuff(), Stuff()],
            ),
            Box(
                identifier=3,
                elements=[
                    Box(
                        identifier=4,
                        elements=[Stuff()],
                    ),
                    Box(
                        identifier=5,
                        elements=[Stuff()],
                    ),
                    Box(
                        identifier=6,
                        elements=[Stuff()],
                    ),
                ],
            ),
            Box(
                identifier=7,
                elements=[
                    Box(
                        identifier=8,
                        elements=[
                            Box(
                                identifier=9,
                                elements=[Key()],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

    assert look_for_key_loop(main_box).identifier == expected_identifier
    assert look_for_key_recursion(main_box).identifier == expected_identifier
