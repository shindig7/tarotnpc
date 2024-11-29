from os import environ as env

from load_dotenv import load_dotenv  # type: ignore
from openai import OpenAI

load_dotenv()


def get_openai_client():
    return OpenAI(env["OPENAI_API_KEY"])
