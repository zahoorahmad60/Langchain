from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

ollama_model = OllamaLLM(model="gemma3:1b")

prompt = PromptTemplate(
template=""" you are a helpful assistant that can answer questions related to the Pakistan's constitution.Give the anwer in this format:
Thank you for asking the question {question} according to the constitution of Pakistan, the answer is. add the law numbers in the answer.
""")

chain = prompt | ollama_model

result = chain.invoke({"question": "who is the owner of the country?"})
print(result)

# this is a dynamic prompt here the user can enter any question and the model will answer according to the prompt
