from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState

from app.nodes.query_node import query_analysis_node
from app.nodes.retrieve_node import retrieve_node
from app.nodes.grade_node import document_grading_node
from app.nodes.decision_node import decision_node
from app.nodes.generate_node import generate_node
from app.nodes.no_answer_node import no_answer_node
from app.nodes.rewrite_node import rewrite_query_node

# ==========================================================
# Build Workflow
# ==========================================================

workflow = StateGraph(GraphState)

# ==========================================================
# Add Nodes
# ==========================================================

workflow.add_node("query", query_analysis_node)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("grade", document_grading_node)
workflow.add_node("rewrite", rewrite_query_node)
workflow.add_node("generate", generate_node)
workflow.add_node("no_answer", no_answer_node)

# ==========================================================
# Connect Nodes
# ==========================================================

workflow.add_edge(START, "query")

workflow.add_edge("query", "retrieve")

workflow.add_edge("retrieve", "grade")

# After rewriting, retrieve again
workflow.add_edge("rewrite", "retrieve")

# ==========================================================
# Conditional Routing
# ==========================================================

workflow.add_conditional_edges(
    "grade",
    decision_node,
    {
        "generate": "generate",
        "rewrite": "rewrite",
        "end": "no_answer"
    }
)

# ==========================================================
# End Nodes
# ==========================================================

workflow.add_edge("generate", END)
workflow.add_edge("no_answer", END)

# ==========================================================
# Compile Graph
# ==========================================================

graph = workflow.compile()