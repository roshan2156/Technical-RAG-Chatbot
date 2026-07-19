from app.graph.state import GraphState

# ==========================================================
# Query Analysis Node
# ==========================================================

def query_analysis_node(state: GraphState) -> GraphState:
    """
    Improves short user queries into more descriptive
    documentation-friendly questions.
    """

    question = state["question"].strip().lower()

    improvements = {
        "middleware": "What is middleware in FastAPI?",
        "fastapi": "What is FastAPI?",
        "langgraph": "What is LangGraph?",
        "chromadb": "What is ChromaDB?",
        "dependency": "What is dependency injection in FastAPI?",
        "dependencies": "What is dependency injection in FastAPI?",
        "pydantic": "What is Pydantic?"
    }

    improved_question = improvements.get(
        question,
        state["question"]
    )

    print("\n" + "=" * 80)
    print("QUERY ANALYSIS NODE")
    print("=" * 80)

    print(f"Original Question : {state['question']}")
    print(f"Improved Question : {improved_question}")

    state["question"] = improved_question

    return state