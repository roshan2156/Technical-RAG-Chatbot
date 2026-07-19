from pathlib import Path
import json

from fastapi import FastAPI

from .schemas import (
    QueryRequest,
    QueryResponse,
    FeedbackRequest,
)

from app.graph.workflow import graph
from app.ingestion.ingest import ingest_documents

app = FastAPI(
    title="Technical RAG Chatbot",
    version="1.0.0"
)

BASE_DIR = Path(__file__).resolve().parent
DOCUMENT_DIR = BASE_DIR.parent / "documents"
FEEDBACK_FILE = BASE_DIR / "data" / "feedback.json"

FEEDBACK_FILE.parent.mkdir(exist_ok=True)


# ==========================================================
# Root Endpoint
# ==========================================================

@app.get("/")
def root():
    return {
        "message": "Technical RAG Chatbot API"
    }


# ==========================================================
# Query Endpoint
# ==========================================================

@app.post(
    "/query",
    response_model=QueryResponse
)
def query(request: QueryRequest):

    state = {
        "question": request.question,
        "retrieved_docs": [],
        "relevant_docs": [],
        "answer": "",
        "retry_count": 0
    }

    result = graph.invoke(state)

    return QueryResponse(
        question=result["question"],
        answer=result["answer"]
    )


# ==========================================================
# Ingest Endpoint
# ==========================================================

@app.post("/ingest")
def ingest():

    ingest_documents()

    return {
        "message": "Documents indexed successfully."
    }


# ==========================================================
# Documents Endpoint
# ==========================================================

@app.get("/documents")
def documents():

    docs = [
        file.name
        for file in DOCUMENT_DIR.glob("*.md")
    ]

    return {
        "count": len(docs),
        "documents": docs
    }


# ==========================================================
# Feedback Endpoint
# ==========================================================

@app.post("/feedback")
def feedback(request: FeedbackRequest):

    data = []

    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, "r") as f:
            data = json.load(f)

    data.append(request.model_dump())

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return {
        "message": "Feedback stored successfully."
    }