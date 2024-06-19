import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load environment variables from .env file

load_dotenv()

model = ChatOpenAI (model="gpt-3.5-turbo")

chunks = []
for chunk in model.stream("what color is the sky?"):
    chunks.append(chunk)
    print(chunk.content, end="|", flush=True)


