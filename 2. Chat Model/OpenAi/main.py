import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

model = ChatOpenAI(
    api_key=openai_key,
    model="gpt-4o",
    temperature=0.7,
    max_tokens=512
)

result = model.invoke("What is the capital of Pakistan")
print(result)