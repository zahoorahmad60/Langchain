from langchain_ollama import OllamaLLM # type: ignore

MODEL =OllamaLLM(model="deepseek-r1:1.5b")
result = MODEL.invoke("Hello! what is the capital of Pakistan?")
print(result)