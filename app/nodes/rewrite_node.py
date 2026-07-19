from app.graph.state import GraphState


def rewrite_query_node(state: GraphState):
    """
    Rewrite the query before retrying retrieval.
    """

    print("\n" + "=" * 80)
    print("QUERY REWRITE NODE")
    print("=" * 80)

    question = state["question"]

    prefix = "Technical documentation about "

    if not question.startswith(prefix):
        question = prefix + question

    state["question"] = question
    state["retry_count"] += 1

    print("Rewritten Question:", state["question"])
    print("Retry Count:", state["retry_count"])

    return state