import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv() 
api_key = os.getenv("GOOGLE_API")


class Blabber:
    """
    A class for interacting with the Gemini AI model for chat-based conversations.

    Requirements:
        - A valid Gemini API key
        - A 'prompt.txt' file in the same folder containing system instructions
    """
    def __init__(self, prompt_file="assignment_3/prompt.txt"):
        client = genai.Client(api_key=api_key)
        
        with open(prompt_file, "r") as file:
            sys_instruct = file.read()

        self.chat = client.chats.create(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                max_output_tokens=150, temperature=0.1, system_instruction=sys_instruct
            ),
        )

    def ask(self, input):
        """
        Sends a message to the chat and returns the AI's response

        Args:
            input (str): the input message to send to the AI

        Returns:
            str: the response from the AI
        """
        response = self.chat.send_message(input)
        return response.text
