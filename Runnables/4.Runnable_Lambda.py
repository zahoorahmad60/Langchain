from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableSequence

def word_counts(text):
    return len(text["topic"].split())



llm = ChatOllama(model="deepseek-r1:1.5b")

prompt = PromptTemplate(
    template="Write a joke on the topic: {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = RunnableParallel({
    'joke': RunnableSequence(prompt,llm,parser),
    'words_counts': RunnableLambda(word_counts)
})

result = chain.invoke({"topic":"AI"})

print(result)