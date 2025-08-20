from langchain_openai import  OpenAIEmbeddings
from dotenv import load_dotenv     #make sure your Openai_api is configured well 

load_dotenv()

model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

query = "Hello! this is the embeding query for the closed sourse openai model"

result = model.embed_query("query")

print(result)