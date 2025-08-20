from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence


llm = ChatOllama(model="deepseek-r1:1.5b")

prompt1 = PromptTemplate(
    template="Give me a detailed report on the topic: {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Give me 5 questions and answers that are frequently asked questions on the topic: {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain_parallel = RunnableParallel({
    'report': RunnableSequence(prompt1,llm,parser),
    'F&Q': RunnableSequence(prompt2,llm,parser),
})

result = chain_parallel.invoke({"topic":"AI"})
print(result)
print(chain_parallel.get_graph().draw_ascii())