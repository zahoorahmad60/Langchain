from langchain_ollama import OllamaLLM
from typing import TypedDict, Annotated,Optional,Literal
import json

llm = OllamaLLM(model='gemma3:1b')

# output_scheema
class Reviews_scheema(TypedDict):
    sentiment: Annotated[str, "Provide the sentiment more perfectly"]
    summery: Annotated[str, "Provide a perfect and conscise summery"]
    

prompt = (
    """Analyze the following text and return a JSON object with the following fields: 
    - sentiment (string): The overall sentiment of the text.
    - summery (string): A brief summary of the text.
    Text: Please, don't stop this GenAI series or make any of the videos course-oriented or members-only content I request you. Let alone this Langchain playlist is so good and helpful. It is difficult to keep up and make content consistently but I request you to keep posting the videos with the same effort and quality. Your channel is a gem and you are making a huge difference already so you have all the support you need please continue and keep pushing.
    Return only the JSON object."""
)

response = llm.invoke(prompt)

try:
    result: Reviews_scheema = json.loads(response)
    print(result)
except Exception as e:
    print("Failed to parse response as JSON:", e)
    print("Raw response:\n", response)


"""Note:
        This typeDict is not a valid method for structured output, because this is just the representation
        of the data types not the validation. for validation we use Pydantic.
"""