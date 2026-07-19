from pathlib import Path

from graph.workflow import graph

# ==========================================================
# Initial Graph State
# ==========================================================

state = {
    "question": "middleware",
    "retrieved_docs": [],
    "relevant_docs": [],
    "answer": "",
    "retry_count": 0
}

# ==========================================================
# Initial State
# ==========================================================

print("=" * 80)
print("INITIAL GRAPH STATE")
print("=" * 80)

print(state)

# ==========================================================
# Run LangGraph Workflow
# ==========================================================

state = graph.invoke(state)

# ==========================================================
# Final State
# ==========================================================

print("\n" + "=" * 80)
print("FINAL GRAPH STATE")
print("=" * 80)

print(f"Question          : {state['question']}")
print(f"Retrieved Docs    : {len(state['retrieved_docs'])}")
print(f"Relevant Docs     : {len(state['relevant_docs'])}")
print(f"Retry Count       : {state['retry_count']}")

print("\nAnswer")
print("-" * 80)
print(state["answer"])

# ==========================================================
# Display Relevant Documents
# ==========================================================

if state["relevant_docs"]:

    print("\n" + "=" * 80)
    print("RELEVANT DOCUMENTS")
    print("=" * 80)

    for i, doc in enumerate(state["relevant_docs"], start=1):

        print(f"\nResult {i}")

        source = doc.metadata.get("source", "Unknown")

        print(f"Source : {Path(source).name}")
        print("-" * 80)
        print(doc.page_content)

else:

    print("\nNo relevant documents found.")