from pathlib import Path
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from app.graph.state import GraphState

load_dotenv()

# ==========================================================
# LLM
# ==========================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ==========================================================
# Prompt
# ==========================================================

generation_prompt = ChatPromptTemplate.from_template(
"""
You are a technical documentation assistant.

Answer the user's question using ONLY the provided documentation.

Question:
{question}

Documentation:
{context}

Instructions:

- Answer ONLY using the provided documentation.
- Do NOT use outside knowledge.
- Do NOT infer, speculate, or make assumptions.
- Do NOT add conclusions that are not explicitly supported by the documentation.
- Combine information from multiple documents into one clear answer when appropriate.
- Include definitions, explanations, and common uses if they appear in the documentation.
- If the documentation does not contain enough information to answer the question, respond EXACTLY with:
I don't know based on the available documentation.

Answer:
"""
)

generation_chain = generation_prompt | llm


# ==========================================================
# Generation Node
# ==========================================================

def generate_node(state: GraphState) -> GraphState:

    print("\n" + "=" * 80)
    print("GENERATION NODE")
    print("=" * 80)

    question = state["question"]
    relevant_docs = state["relevant_docs"]

    # ======================================================
    # Build Context
    # ======================================================

    context = "\n\n".join(
        doc.page_content for doc in relevant_docs
    )

    # ======================================================
    # Generate Answer
    # ======================================================

    response = generation_chain.invoke(
        {
            "question": question,
            "context": context
        }
    )

    answer = response.content.strip()

    # Optional cleanup for formatting
    answer = answer.replace("andrate", "and rate")

    # ======================================================
    # Collect Sources
    # ======================================================

    sources = []

    for doc in relevant_docs:

        source = Path(
            doc.metadata.get("source", "Unknown")
        ).name

        if source not in sources:
            sources.append(source)

    # ======================================================
    # Append Sources
    # ======================================================

    if sources:

        answer += "\n\nSources:\n"

        for source in sources:
            answer += f"- {source}\n"

    state["answer"] = answer

    print(answer)

    return state