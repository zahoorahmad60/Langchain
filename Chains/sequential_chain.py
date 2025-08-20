from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="gemma3:1b")

template1 = PromptTemplate(
    template="Give me a detail report on the {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Give me the 5 points summery on the given {output}",
    input_variables=["output"]
)

parser = StrOutputParser()

chain = template1 | llm | parser | template2 | llm | parser
result = chain.invoke({"topic":"black hole"})

print(result)