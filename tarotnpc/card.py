from enum import Enum
from pathlib import Path

from strictyaml import load


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


def get_major_arcana(path: Path = Path("data/major_arcana.yaml")) -> list[MajorArcana]:
    with open(path, "r") as F:
        data = load(F.read())
    return [MajorArcana(**card) for card in data]


def get_minor_arcana(path: Path = Path("data/minor_arcana.yaml")) -> list[MinorArcana]:
    with open(path, "r") as F:
        data = load(F.read())
    return [MinorArcana(**card) for card in data]


def get_all_cards() -> list[Card]:
    return get_major_arcana() + get_minor_arcana()
