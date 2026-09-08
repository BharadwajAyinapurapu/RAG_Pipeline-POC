from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

sentence = "Hi, this is Bharadwaj working on embeddings"
sentences = [
    "The cat sat on the mat",
    "As you sow sow shall you reap",
    "AGI is the new upcoming trend",
    "Python is my fav prog lang"
]
sentence_embedding = embeddings.embed_query(sentence)
sentences_embedding = embeddings.embed_documents(sentences)

print(f"Text: {sentence}")
print(f"Embedding Length: {len(sentence_embedding)}")
print(f"Vector: {sentence_embedding}") 

print(f"Vector 1: {sentences_embedding[0]}")