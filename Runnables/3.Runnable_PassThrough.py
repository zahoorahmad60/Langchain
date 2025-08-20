from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableSequence,RunnableParallel

llm = ChatOllama(model="deepseek-r1:1.5b")

prompt = PromptTemplate(
    template="Give me the three points summery on the topic: {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = RunnableParallel({
    'summery': RunnableSequence(prompt,llm,parser),
    'topic': RunnablePassthrough()
})

result = chain.invoke({"topic":"Cricket"})

print(result)