from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = """
Question:
What is middleware?

Context:
Middleware is software that executes before and after every HTTP request.

Answer:
"""

response = llm.invoke(prompt)

print(response.content)