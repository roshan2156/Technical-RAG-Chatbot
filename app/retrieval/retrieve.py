from pathlib import Path

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]
CHROMA_DIR = BASE_DIR / "chroma_db"

# ==========================================================
# Load Embedding Model
# ==========================================================

print("=" * 80)
print("LOADING EMBEDDING MODEL")
print("=" * 80)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded successfully!")

# ==========================================================
# Load ChromaDB
# ==========================================================

print("\n" + "=" * 80)
print("LOADING CHROMADB")
print("=" * 80)

vector_store = Chroma(
    persist_directory=str(CHROMA_DIR),
    embedding_function=embedding_model,
    collection_name="technical_rag"
)

print("ChromaDB loaded successfully!")

# ==========================================================
# Retrieve Documents Function
# ==========================================================

def retrieve_documents(question: str, k: int = 3):
    """
    Retrieve diverse and relevant document chunks using
    Max Marginal Relevance (MMR).
    """

    print("\n" + "=" * 80)
    print("SEARCHING CHROMADB")
    print("=" * 80)

    print(f"Query : {question}")
    print(f"Top K : {k}")

    # ======================================================
    # MMR Retrieval
    # ======================================================

    retrieved_docs = vector_store.max_marginal_relevance_search(
        query=question,
        k=k,
        fetch_k=10
    )

    # ======================================================
    # Remove Duplicate Chunks
    # ======================================================

    unique_docs = []
    seen = set()

    for doc in retrieved_docs:

        content = doc.page_content.strip()

        if content not in seen:
            unique_docs.append(doc)
            seen.add(content)

    print(f"\nRetrieved {len(unique_docs)} unique documents successfully.")

    return unique_docs


# ==========================================================
# Test Retrieval
# ==========================================================

if __name__ == "__main__":

    query = "What is middleware in FastAPI?"

    docs = retrieve_documents(query)

    print("\n" + "=" * 80)
    print("TOP RETRIEVED DOCUMENTS")
    print("=" * 80)

    for i, doc in enumerate(docs, start=1):

        print(f"\nResult {i}")

        source = doc.metadata.get("source", "Unknown")

        print(f"Source : {Path(source).name}")
        print("-" * 80)
        print(doc.page_content)
