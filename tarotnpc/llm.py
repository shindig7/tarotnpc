from os import environ as env

from dotenv import load_dotenv  # type: ignore
from openai import OpenAI

load_dotenv()


class Conversation:
    def __init__(self, messages: list[dict[str, str]]):
        self.messages = messages

    def append(self, message: dict[str, str]):
        self.messages.append(message)

    def add_user_message(self, content: str):
        self.append({"role": "user", "content": content})

    def add_ai_message(self, content: str):
        self.append({"role": "assistant", "content": content})

    def __repr__(self) -> str:
        return str(self.messages)


def get_openai_client():
    return OpenAI(api_key=env["OPENAI_API_KEY"])


def get_chat_completion(conversation: Conversation) -> dict:
    client = get_openai_client()
    chat_completion = client.chat.completions.create(
        messages=conversation.messages,
        model=env["MODEL"],
        temperature=1.0,
    )
    return chat_completion
