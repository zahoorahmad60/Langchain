from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage


chat_model = ChatOllama(model="gemma3:1b ")

chat_promt = ChatPromptTemplate([
    ('system','You are an {domain} expert'),
    ('human','Please explain {topic} for me')
])


final_prompt = chat_promt.invoke({'domain':'Cricket', 'topic':'dusara'})

print(final_prompt)