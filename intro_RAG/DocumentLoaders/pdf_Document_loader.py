from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"A:\Langchain\intro_RAG\DocumentLoaders\files\Updated_Constitution_Pakistan.pdf")

docs = loader.load()

print(len(docs))
print(docs[3].page_content)