from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

llm1 = ChatOllama(model="gemma3:1b")
llm2 = ChatOllama(model="deepseek-r1:1.5b")


promt1 = PromptTemplate(
    template="Give me a report on the topic {topic}",
    input_variables=["topic"]
)

promt2 = PromptTemplate(
    template="Give me a 5 questions and their answers on the text {topic}",
    input_variables=["topic"]
)

promt3 = PromptTemplate(
    template="Give me a combined document of -> {notes} and {quiz}",
    input_variables=["notes","quiz"]
)

parser = StrOutputParser()

chain1 = RunnableParallel(
    {
        'notes' : promt1 | llm1 |  parser,
        'quiz': promt2 | llm2 | parser,
    }
)

chain2 = promt3 | llm1 | parser

final_chain = chain1 | chain2

result = final_chain.invoke({"topic": "Imran khan in Pakistan"})

print(result)

print(final_chain.get_graph().draw_ascii())