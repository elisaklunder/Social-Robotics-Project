from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # Load the environment variables from .env
api_key = os.getenv("GOOGLE_API")
print(api_key)  # Test if it loads correctly

client = genai.Client(api_key="AIzaSyDjUIrATdeFsNSkoILYdmyAkNA-_i-nB6U")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)