from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "FastAPI is a modern Python web framework."

embedding = embedding_model.embed_query(text)

print("Embedding created successfully!\n")

print("Embedding length:", len(embedding))

print("\nFirst 10 values:")

print(embedding[:10])