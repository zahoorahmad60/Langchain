from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



chat_model = ChatOllama(model="deepseek-r1:1.5b")

tempelate_One = PromptTemplate(
    template="write a detailed report on this {topic}",
    input_variables=['topic']
)
tempelate_two = PromptTemplate(
    template="write a 3 line summery on this \n {text}",
    input_variables=['text']
)
user_input = input("Enter any topic here:\b")

parser = StrOutputParser()

chain = tempelate_One | chat_model | parser | tempelate_two | chat_model | parser


result = chain.invoke({"topic":user_input})

print(result)