from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
loader = TextLoader("A:\Langchain\intro_RAG\DocumentLoaders\\files\cricket_poem.txt",encoding='utf-8')

docs = loader.load()

model = ChatOllama(model="deepseek-r1:1.5b")

promt = PromptTemplate(
    template="Generate a summery of the following text /{text}"
)

parsor = StrOutputParser()

chain = promt | model | parsor

result =chain.invoke({"text":docs[0]})

print(result)
##print(docs[0])

