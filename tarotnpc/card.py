from dataclasses import dataclass
from enum import Enum


class Suit(str, Enum):
    WANDS = "wands"
    CUPS = "cups"
    SWORDS = "swords"
    PENTACLES = "pentacles"


class Card:
    def __init__(self, description: str, reversed_description: str):
        self.description = description
        self.reversed_description = reversed_description


class MajorArcana(Card):
    def __init__(self, title: str, description: str, reversed_description: str):
        super().__init__(description, reversed_description)
        self.title = title

    def __repr__(self) -> str:
        return self.title.upper()


class MinorArcana(Card):
    def __init__(
        self, suit: str, value: int, description: str, reversed_description: str
    ):
        super().__init__(description, reversed_description)
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit.upper()}"
