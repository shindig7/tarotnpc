import random
from enum import Enum
from pathlib import Path

from strictyaml import load


class Card:
    def __init__(self, title: str, description: str, reversed_description: str):
        self.title = title
        self.description = description
        self.reversed_description = reversed_description
        self.is_reversed = False

    def is_reversed(self) -> bool:
        return self.is_reversed

    def __repr__(self) -> str:
        return self.title.title()


def get_major_arcana(path: Path = Path("data/major_arcana.yaml")) -> list[Card]:
    with open(path, "r") as F:
        data = load(F.read()).data
    return [Card(**card) for card in data]


def get_minor_arcana(path: Path = Path("data/minor_arcana.yaml")) -> list[Card]:
    with open(path, "r") as F:
        data = load(F.read()).data
    return [Card(**card) for card in data]


def get_all_cards() -> list[Card]:
    return get_major_arcana() + get_minor_arcana()


def get_deck() -> list[Card]:
    cards = get_all_cards()
    for card in cards:
        card.is_reversed = random.choice([True, False])
    return cards


def draw(cards: list[Card], n: int) -> list[Card]:
    return random.sample(cards, n)
