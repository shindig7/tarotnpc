from strictyaml import load

from tarotnpc.card import Card


def load_prompts():
    with open("data/prompts.yaml", "r") as F:
        return load(F.read()).data


def format_prompt(prompt: str, card: Card) -> str:
    return prompt.format(
        CARD_NAME=card.__repr__(),
        UPRIGHT_OR_REVERSED=("reversed" if card.is_reversed else "upright"),
        CARD_DESCRIPTION=(
            card.reversed_description if card.is_reversed else card.description
        ),
    )
