from pathlib import Path

from app.graph.state import GraphState
from app.retrieval.retrieve import retrieve_documents


# ==========================================================
# Retrieval Node
# ==========================================================

def retrieve_node(state: GraphState) -> GraphState:
    """
    LangGraph Retrieval Node

    Retrieves the most relevant document chunks from ChromaDB
    and stores them in the graph state.
    """

    # ------------------------------------------------------
    # Get the user question
    # ------------------------------------------------------

    question = state["question"]

    print("\n" + "=" * 80)
    print("RETRIEVAL NODE")
    print("=" * 80)

    print(f"Searching for:\n{question}")

    # ------------------------------------------------------
    # Retrieve documents
    # ------------------------------------------------------

    retrieved_docs = retrieve_documents(question, k=3)

    # ------------------------------------------------------
    # Update graph state
    # ------------------------------------------------------

    state["retrieved_docs"] = retrieved_docs

    print(f"\nRetrieved {len(retrieved_docs)} documents.")

    # ------------------------------------------------------
    # Display retrieved documents
    # ------------------------------------------------------

    print("\n" + "=" * 80)
    print("TOP RETRIEVED DOCUMENTS")
    print("=" * 80)

    for i, doc in enumerate(retrieved_docs, start=1):

        source = doc.metadata.get("source", "Unknown")

        print(f"\nResult {i}")
        print(f"Source : {Path(source).name}")
        print("-" * 80)
        print(doc.page_content)

    return state


# ==========================================================
# Test Retrieval Node
# ==========================================================

if __name__ == "__main__":

    state = {
        "question": "How do I add middleware in FastAPI?",
        "retrieved_docs": [],
        "relevant_docs": [],
        "answer": "",
        "retry_count": 0
    }

    updated_state = retrieve_node(state)

    print("\n" + "=" * 80)
    print("UPDATED GRAPH STATE")
    print("=" * 80)

    print(f"Question        : {updated_state['question']}")
    print(f"Retrieved Docs  : {len(updated_state['retrieved_docs'])}")
    print(f"Relevant Docs   : {len(updated_state['relevant_docs'])}")
    print(f"Retry Count     : {updated_state['retry_count']}")
    print(f"Answer          : {updated_state['answer']}")