"""Chapter 3. Recursion. Look for key in a box."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator


class Box:
    """Box entity."""

    def __init__(
        self,
        identifier: int,
        elements: list[Box | Key | Stuff],
    ) -> None:
        """Make new instance.

        Args:
            identifier (int): Box ID.
            elements (list[BoxOrKey]): list of Item.

        """
        self._identifier = identifier
        self._elements: list[Box | Key | Stuff] = elements

    def __iter__(self) -> Iterator[Box | Key | Stuff]:
        """Iterate through box.

        Yields:
            Iterator[Item]: Item entity.

        """
        yield from self._elements

    @property
    def identifier(self) -> int:
        """Get box identifier.

        Returns:
            int: box identifier.

        """
        return self._identifier


class Key:
    """Key entity."""


class Stuff:
    """Stuff entity."""


def look_for_key_loop(main_box: Box) -> Box | None:
    """Look for key in a box using loop.

    Args:
        main_box (Box): Box with Boxes

    Returns:
        Key | None: Box with a Key or None.

    """
    pile: list[Box | Key | Stuff] = [main_box]

    while pile:
        box: Box | Key | Stuff = pile.pop(0)

        if isinstance(box, Box):
            for element in box:
                if isinstance(element, Box):
                    pile.append(element)
                elif isinstance(element, Key):
                    return box

    return None


def look_for_key_recursion(main_box: Box) -> Box | None:
    """Look for key in a box using recursion.

    Args:
        main_box (Box): Box with Boxes

    Returns:
        Key | None: Box with a Key or None.

    """
    memory: Box | None = None

    for element in main_box:
        if isinstance(element, Box):
            memory = look_for_key_recursion(element)
        if isinstance(element, Key):
            memory = main_box

    return memory
