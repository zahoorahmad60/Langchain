from langchain_ollama import OllamaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

Embeding_model = OllamaEmbeddings(model="nomic-embed-text:latest")

document = [
    "Imran khan is the prime minister of Pakistan and He is a great good leader of the people of Pakistan.",
    "Donald.J Trump is the Presisdent of United state of America.He is runnig his countery very well",
    "Tayyab Rajab urdagan is the Leader of Turkiye.He won elections more then 5 time in past 25 years"

]

query = 'Who is Donald.J tRUMP?'

document_embeddings = Embeding_model.embed_documents(document)
query_embeddings = Embeding_model.embed_query(query)

similarty_score = cosine_similarity([query_embeddings],document_embeddings)[0]

index, score = sorted(list(enumerate(similarty_score)),key=lambda x:x[1])[-1]

print(query)
print(document[index])
print("similarity score is:", score)



