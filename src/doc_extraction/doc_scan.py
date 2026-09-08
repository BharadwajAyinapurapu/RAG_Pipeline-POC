from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.documents import Document

file_path = "data/text_files/python_intro.txt"
dir_path = "data/text_files"

file_loader = TextLoader(file_path, encoding="utf-8")
dir_loader = DirectoryLoader(
    dir_path,
    glob = "**/*.txt",
    loader_cls=TextLoader
)
file_doc = file_loader.load()
dir_doc = dir_loader.load()
print("file_doc", file_doc)
print("dir_doc", dir_doc)

print(f"Loaded {len(dir_doc)} documents")
for i, doc in enumerate(dir_doc):
    print(f"\n Document {i+1}")
    print(f"   Source: {doc.metadata}")
    print(f"   Length: {len(doc.page_content)} characters")