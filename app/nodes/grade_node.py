from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from app.graph.state import GraphState

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Load Groq LLM
# ==========================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ==========================================================
# Document Grading Prompt
# ==========================================================

grading_prompt = ChatPromptTemplate.from_template(
"""
You are an expert document relevance grader.

Question:
{question}

Document:
{document}

Instructions:

- Return YES if the document directly discusses the topic in the question.
- Return YES if it contains definitions, explanations, examples, or implementation details related to the question.
- Return NO if it only contains general background information that does not help answer the question.
- Return NO if the topic is different.

Return ONLY one word.

YES

or

NO
"""
)
# ==========================================================
# Create Grading Chain
# ==========================================================

grading_chain = grading_prompt | llm

# ==========================================================
# Document Grading Node
# ==========================================================

def document_grading_node(state: GraphState) -> GraphState:
    """
    Uses Groq to evaluate each retrieved document and
    keeps only the relevant ones.
    """

    question = state["question"]
    retrieved_docs = state["retrieved_docs"]

    relevant_docs = []

    print("\n" + "=" * 80)
    print("DOCUMENT GRADING NODE")
    print("=" * 80)

    for i, doc in enumerate(retrieved_docs, start=1):

        print(f"\nChecking Document {i}")

        response = grading_chain.invoke(
            {
                "question": question,
                "document": doc.page_content
            }
        )

        decision = response.content.strip().lower()

        print(f"LLM Decision : {decision}")

        if "yes" in decision:

            print("Relevant ✅")
            relevant_docs.append(doc)

        else:

            print("Not Relevant ❌")

    # ======================================================
    # Update Graph State
    # ======================================================

    state["relevant_docs"] = relevant_docs

    print("\n" + "=" * 80)
    print("DOCUMENT GRADING COMPLETED")
    print("=" * 80)

    print(f"Retrieved Documents : {len(retrieved_docs)}")
    print(f"Relevant Documents  : {len(relevant_docs)}")

    return state