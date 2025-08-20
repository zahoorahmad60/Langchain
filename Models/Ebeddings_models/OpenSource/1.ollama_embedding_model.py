from langchain_ollama import OllamaEmbeddings

embeding_model = OllamaEmbeddings(model="nomic-embed-text:latest")

query = "Hello there is the embedings of this sentence"


result = embeding_model.embed_query(query)

print(result)