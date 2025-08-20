from langchain_ollama import OllamaLLM # type: ignore


model = OllamaLLM(model="gemma3:1b")

while True:
    user_input = input("You:")
    if user_input == "/q":
        break
    result = model.invoke(user_input)
    print(f"AI: {result}")

#this is very basic chatbot which has not any memeory or context to hold.