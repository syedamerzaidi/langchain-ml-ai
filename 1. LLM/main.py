import os
from langchain_openai.llms.base import OpenAI 
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

llm = OpenAI(
    api_key=openai_key,
    model_name="gpt-3.5-turbo-instruct",
    temperature=0.7, # controls the randomness (creativity) of the output
    max_tokens=512 # maximum number of tokens to generate
)

result = llm.invoke("What is the capital of Pakistan")
print(result)
