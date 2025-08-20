from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate


legal_bot = ChatOllama(model="gemma3:1b")

prompt = PromptTemplate(
    template="""

You’re a legal-research assistant.

User asked: {user_question}

1. If excerpts found:
   - Summarize the rule in plain English.
   - Cite each excerpt: 
   - Add: “This is not legal advice. For advice in your situation, consult an attorney.”

2. If none found:
   - “Sorry, I couldn’t find a clear answer. Please consult a qualified attorney.”
"""
)


while True:
    user_ques = str(input("YOU:"))
    if user_ques == '/q':
        break
    chain = prompt | legal_bot
    response = chain.invoke({"user_question": user_ques})
    print("Legal Bot:", response.content)
