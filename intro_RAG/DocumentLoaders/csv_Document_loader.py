from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='A:\Langchain\intro_RAG\DocumentLoaders\files\Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])