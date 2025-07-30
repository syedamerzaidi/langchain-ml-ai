from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Please set the GEMINI_API_KEY environment variable in your .env file")

embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key,
)

try:
    result = embedding.embed_query("Islamabad is the capital of Pakistan")
    print("Dimensions of the embedding vector:")
    print(result)
    print(f"Total dimensions: {len(result)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")