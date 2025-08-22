from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

loader = TextLoader(r"A:\Langchain\intro_RAG\DocumentLoaders\files\cricket_poem.txt")

docs = loader.load()
splitter = CharacterTextSplitter(
    chunk_size = 125,
    chunk_overlap =0,
    separator=""
)
splitted_text = splitter.split_text(docs[0].page_content)
print(splitted_text)
print(len(splitted_text))
