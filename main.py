from tarotnpc.card import draw, get_deck
from tarotnpc.llm import Conversation, get_chat_completion
from tarotnpc.prompts import format_prompt, load_prompts

if __name__ == "__main__":
    prompts = load_prompts()

    deck = get_deck()
    major_trait_card, minor_trait_card, past_card, present_card, future_card = draw(
        deck, 5
    )

    print("Major Trait Card:", major_trait_card)
    print("Minor Trait Card:", minor_trait_card)
    print("Past Card:", past_card)
    print("Present Card:", present_card)
    print("Future Card:", future_card)

    """
    starter_prompt = (
        prompts.get("SYSTEM_PROMPT")
        + "\n"
        + prompts.get("NAME").format("Her name is Katja Everheart.")
        + format_prompt(prompts.get("MAJOR_TRAIT"), major_trait_card)
    )

    conversation = Conversation([
        {
            "role": "user",
            "content": starter_prompt,
        }
    ])
    response = get_chat_completion(conversation)
    conversation.add_ai_message(response.choices[0].message.content)
    print("Major Trait Response:\n")
    print(response.choices[0].message.content)
    print("\n")

    minor_prompt = format_prompt(prompts.get("MINOR_TRAIT"), minor_trait_card)
    conversation.add_user_message(minor_prompt)
    minor_response = get_chat_completion(conversation)
    conversation.add_ai_message(minor_response.choices[0].message.content)
    print("Minor Trait Response:\n")
    print(minor_response.choices[0].message.content)
    print("\n")

    personality_summary = prompts.get("PERSONALITY_SUMMARY")
    conversation.add_user_message(personality_summary)
    personality_response = get_chat_completion(conversation)
    conversation.add_ai_message(personality_response.choices[0].message.content)
    print("Personality Summary:\n")
    print(personality_response.choices[0].message.content)
    print("\n")

    past_prompt = format_prompt(prompts.get("PAST"), past_card)
    conversation.add_user_message(past_prompt)
    past_response = get_chat_completion(conversation)
    conversation.add_ai_message(past_response.choices[0].message.content)
    print("Past Response:\n")
    print(past_response.choices[0].message.content)
    print("\n")
    """
    starter_prompt = (
        prompts.get("SYSTEM_PROMPT")
        + "\n"
        + prompts.get("NAME").format("Her name is Katja Everheart.")
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
        conversation.add_ai_message(card_response.choices[0].message.content)
        print(f"{prompt} Response:\n")
        print(card_response.choices[0].message.content)
        print("\n")
