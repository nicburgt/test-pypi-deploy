"""example class module."""

from typing import Optional


class Example:
    """Example class."""

    def __init__(self, name: str, count: Optional[int] = None) -> None:
        self.name = name
        self.count = count
