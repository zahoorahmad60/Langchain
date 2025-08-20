from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

chat_model = ChatOllama(model="deepseek-r1:1.5b")

prompt = PromptTemplate(
    template="Give me this a 5 points summery on the {topic}",
    input_variables=['topic'],
    
)
parser = StrOutputParser()

chain = prompt | chat_model | parser

result = chain.invoke({"topic":"Cricket"})

print(result)
print(chain.get_graph().draw_ascii())