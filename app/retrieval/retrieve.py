from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]
CHROMA_DIR = BASE_DIR / "chroma_db"

# ==========================================================
# Global Variables for Lazy Loading
# ==========================================================
# We declare them here, but we DO NOT initialize them yet.
embedding_model = None
vector_store = None

# ==========================================================
# Initialization Function
# ==========================================================
def _initialize_retriever():
    """
    Lazily initializes the embedding model and ChromaDB.
    This prevents OOM crashes on server startup by only 
    loading into memory when the first search is performed.
    """
    global embedding_model, vector_store
    
    # If already loaded, do nothing
    if vector_store is not None:
        return

    print("=" * 80)
    print("LOADING EMBEDDING MODEL (Lazy Load)")
    print("=" * 80)

    # CRITICAL: Force CPU usage to prevent CUDA/GPU errors on Render
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}  # <--- THIS IS MANDATORY FOR RENDER
    )

    print("Embedding model loaded successfully!")

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
    # 1. Ensure resources are loaded BEFORE searching
    _initialize_retriever()

    print("\n" + "=" * 80)
    print("SEARCHING CHROMADB")
    print("=" * 80)

    print(f"Query : {question}")
    print(f"Top K : {k}")

    # 2. MMR Retrieval
    retrieved_docs = vector_store.max_marginal_relevance_search(
        query=question,
        k=k,
        fetch_k=10
    )

    # 3. Remove Duplicate Chunks
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
# Test Retrieval (Only runs if you execute this file directly)
# ==========================================================

if __name__ == "__main__":
    # When testing locally via `python retrieve.py`, 
    # we manually trigger the init since no web server is running.
    _initialize_retriever()

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
