from app.graph.state import GraphState

MAX_RETRIES = 2


def decision_node(state: GraphState) -> str:
    """
    Decide the next step in the graph.

    Returns:
        "generate" -> Relevant documents found
        "rewrite"  -> Rewrite query and retry retrieval
        "end"      -> Retry limit reached, return no answer
    """

    print("\n" + "=" * 80)
    print("DECISION NODE")
    print("=" * 80)

    # ======================================================
    # Relevant documents found
    # ======================================================

    if len(state["relevant_docs"]) > 0:

        print("Relevant documents found.")
        print("Next Node: Generate Answer")

        return "generate"

    # ======================================================
    # No relevant documents found
    # ======================================================

    retry_count = state.get("retry_count", 0)

    print("No relevant documents found.")
    print(f"Retry Count: {retry_count}/{MAX_RETRIES}")

    if retry_count < MAX_RETRIES:

        print("Retry limit not reached.")
        print("Next Node: Rewrite Query")

        return "rewrite"

    print("Retry limit reached.")
    print("Next Node: No Answer")

    return "end"