from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda

llm = ChatOllama(model="deepseek-r1:1.5b")

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="Give the sentiment of the given feedback")


parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template="Classify a sentimant of the given {feedback}  \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)

parser = StrOutputParser()

classifier_chain = prompt1 | llm | parser2


prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | llm| parser),
    (lambda x:x.sentiment == 'negative', prompt3 | llm | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a BAD phone'}))

chain.get_graph().print_ascii()
