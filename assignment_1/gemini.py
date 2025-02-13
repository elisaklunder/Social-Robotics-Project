import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # Load the environment variables from .env
api_key = os.getenv("GOOGLE_API")


class Blabber:
    def __init__(self):
        client = genai.Client(api_key=api_key)
        
        with open("verbal/prompt.txt", "r") as file:
            sys_instruct = file.read()

        self.chat = client.chats.create(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                max_output_tokens=150, temperature=0.1, system_instruction=sys_instruct
            ),
        )

    def ask(self, input):
        response = self.chat.send_message(input)
        return response.text
