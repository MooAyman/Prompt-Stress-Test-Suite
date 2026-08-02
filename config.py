import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    API_KEY = os.getenv("GROQ_API_KEY")
    PROVIDER = "groq"

    AVAILABLE_MODELS = [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "qwen/qwen3.6-27b",
        "openai/gpt-oss-120b"
    ]      

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# models = client.models.list()

# for model in models.data:
#     print(model.id)

