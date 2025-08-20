from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


chat_model = ChatOllama(model="deepseek-r1:1.5b")

tempelate_One = PromptTemplate(
    template="write a detailed report on this {topic}",
    input_variables=['topic']
)
tempelate_two = PromptTemplate(
    template="write a 3 line summery on this \n {text}",
    input_variables=['text']
)
user_input = input("Enter any topic here")
prompt_one = tempelate_One.invoke({"topic":user_input})

result = chat_model.invoke(prompt_one)

prompt_two = tempelate_two.invoke({"text":result.content})

summerised_text = chat_model.invoke(prompt_two)

print(summerised_text.content)