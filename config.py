import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    OPENAI_MODEL = "gpt-5.5"
    GEMINI_MODEL = "gemini-3.5-flash"
    