from pathlib import Path
from collections import Counter

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]
DOCS_DIR = BASE_DIR / "documents"
CHROMA_DIR = BASE_DIR / "chroma_db"


# ==========================================================
# Ingest Documents Function
# ==========================================================

def ingest_documents():

    print(f"Loading documents from:\n{DOCS_DIR}")

    # ======================================================
    # Load Documents
    # ======================================================

    loader = DirectoryLoader(
        str(DOCS_DIR),
        glob="*.md",
        loader_cls=TextLoader
    )

    documents = loader.load()

    print(f"\nLoaded {len(documents)} documents.\n")

    # ======================================================
    # Split Documents
    # ======================================================

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.\n")

    # ======================================================
    # Preview Chunks
    # ======================================================

    print("=" * 80)
    print("FIRST 5 CHUNKS")
    print("=" * 80)

    for i, chunk in enumerate(chunks[:5], start=1):

        print(f"\nChunk {i}")
        print(f"Source : {Path(chunk.metadata['source']).name}")
        print("-" * 80)
        print(chunk.page_content)
        print("=" * 80)

    # ======================================================
    # Count Chunks
    # ======================================================

    counts = Counter()

    for chunk in chunks:
        filename = Path(chunk.metadata["source"]).name
        counts[filename] += 1

    print("\n" + "=" * 80)
    print("CHUNKS PER DOCUMENT")
    print("=" * 80)

    for filename, count in sorted(counts.items()):
        print(f"{filename:<20} : {count} chunks")

    # ======================================================
    # Load Embedding Model
    # ======================================================

    print("\n" + "=" * 80)
    print("LOADING EMBEDDING MODEL")
    print("=" * 80)

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Embedding model loaded successfully!")

    # ======================================================
    # Store Embeddings
    # ======================================================

    print("\n" + "=" * 80)
    print("GENERATING AND STORING EMBEDDINGS IN CHROMADB")
    print("=" * 80)

    Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(CHROMA_DIR),
        collection_name="technical_rag"
    )

    print("Embeddings generated and stored successfully!")

    # ======================================================
    # Summary
    # ======================================================

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    print(f"Total Documents : {len(documents)}")
    print(f"Total Chunks    : {len(chunks)}")
    print("Collection Name : technical_rag")
    print(f"Database Path   : {CHROMA_DIR}")

    print("\nChromaDB database created successfully!")

    return {
        "documents": len(documents),
        "chunks": len(chunks)
    }


# ==========================================================
# Run Directly
# ==========================================================

if __name__ == "__main__":
    ingest_documents()