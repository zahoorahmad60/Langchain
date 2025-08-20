from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path=r"A:\Langchain\intro_RAG\DocumentLoaders\files",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))

# for document in docs:
#     print(document.metadata)