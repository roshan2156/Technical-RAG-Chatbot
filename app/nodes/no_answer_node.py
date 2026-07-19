from app.graph.state import GraphState


def no_answer_node(state: GraphState):

    state["answer"] = (
        "I don't know based on the available documentation."
    )

    return state