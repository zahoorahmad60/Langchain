from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import pandas as pd


chat_model = ChatOllama(model="gemma3:1b")

json_parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me name of 1 fictional charactors on the genre {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions":json_parser.get_format_instructions()}
)


prompt = template.invoke({"topic": "Science fiction"})

#print(prompt)

chain = template | chat_model | json_parser

result=chain.invoke({"topic":"Sciense Fiction"})

#print(result)
#print(type(result))

# Create DataFrame
df = pd.DataFrame(result['characters'])

print(df.head(5))

"""Note:
        JsonOutputParser Does not enforce any user specified scheema. Model will choose the Json Scheema and format.
        to give the hold to user for the json scheema structure we have to use structureoutput parser.
"""
