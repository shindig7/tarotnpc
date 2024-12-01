from tarotnpc.card import draw, get_deck
from tarotnpc.llm import Conversation, get_chat_completion
from tarotnpc.prompts import format_prompt, load_prompts


def generate_npc(seed_prompt: str) -> dict:
    output = {}
    prompts = load_prompts()

    deck = get_deck()
    major_trait_card, minor_trait_card, past_card, present_card, future_card = draw(
        deck, 5
    )

    output["cards"] = {
        "major_trait": major_trait_card,
        "minor_trait": minor_trait_card,
        "past": past_card,
        "present": present_card,
        "future": future_card,
    }

    starter_prompt = (
        prompts.get("SYSTEM_PROMPT") + "\n" + prompts.get("SEED").format(seed_prompt)
    )
    conversation = Conversation(
        [
            {
                "role": "user",
                "content": starter_prompt,
            }
        ]
    )
    for card, prompt in zip(
        [
            major_trait_card,
            minor_trait_card,
            None,
            past_card,
            present_card,
            future_card,
        ],
        [
            "MAJOR_TRAIT",
            "MINOR_TRAIT",
            "PERSONALITY_SUMMARY",
            "PAST",
            "PRESENT",
            "FUTURE",
        ],
    ):
        if card:
            card_prompt = format_prompt(prompts.get(prompt), card)
        else:
            card_prompt = prompts.get(prompt)
        conversation.add_user_message(card_prompt)
        card_response = get_chat_completion(conversation)
        response_text = card_response.choices[0].message.content
        conversation.add_ai_message(response_text)
        output[prompt.lower()] = response_text

    return output
