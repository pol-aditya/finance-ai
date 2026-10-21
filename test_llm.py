import os

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model=os.getenv("GROQ_MODEL", "openai/gpt-oss-20b"))

response = llm.invoke("Say hello")
print(response.content)