from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

chat_model = ChatOllama(model="gemma3:1b")

messages = [
    SystemMessage(content="You are an expert AI Enginner")
]

while True:
    user_input = input("YOU:")
    user_message = HumanMessage(content=user_input)
    messages.append(user_message)
    if user_input == 'q':
        break
    ai_response = chat_model.invoke(messages).content
    messages.append(AIMessage(content=ai_response))
    print(f"AI: {ai_response}")
    print(messages)



