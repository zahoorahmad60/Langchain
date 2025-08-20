from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(model="deepseek-r1:1.5b")

prompt = PromptTemplate(
    template="Give me a two lines summery on the topic: {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

sequential_chain = prompt|llm| parser    #LCEL (Langchain Expression Language)

result = sequential_chain.invoke({"topic","AI"})

print(result)
print(sequential_chain.get_graph().draw_ascii())