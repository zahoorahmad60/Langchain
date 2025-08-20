from langchain_ollama import ChatOllama
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from typing import TypedDict, Literal, List

chat_model = ChatOllama(model="gemma3:1b")


schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

tempelate = PromptTemplate(
    template="This is the news {news} \n {format_instructions}",
    input_variables=['news'],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain = tempelate | chat_model | parser

result = chain.invoke({'news':"Army Chief visits Kashmir amid rising tensions."})

print(result)


"""Note:
        StructureOutput parser does not perform data/type validation. You have to use pydantic Outputparser for data validation.
"""