import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("GEMINI_API_KEY")

if not openai_key:
    raise ValueError("Please set the GEMINI_API_KEY environment variable")

model = ChatGoogleGenerativeAI(
    api_key=openai_key,
    model="gemini-2.0-flash",
)

result = model.invoke("What is the capital of Pakistan")
print(result)