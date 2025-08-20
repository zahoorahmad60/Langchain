from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1:1.5b")

result = model.invoke("Hello! how are you?") # static prompt here full control is given to the user to enetr any prompt but this is not a good practice

print(result)
