# Technical RAG Chatbot

## Project Overview

This project is a **Technical Retrieval-Augmented Generation (RAG) Chatbot** built using **LangGraph**, **FastAPI**, **ChromaDB**, and **Groq LLM**. The chatbot answers questions only from an indexed technical documentation corpus using Retrieval-Augmented Generation (RAG).

The system follows a **self-corrective RAG workflow**. If relevant documents are not retrieved, it automatically rewrites the user's query and retries retrieval. If no relevant information is found after the retry, it returns a safe fallback response instead of generating unsupported answers.

---

# Features

- Retrieval-Augmented Generation (RAG)
- LangGraph workflow orchestration
- ChromaDB vector database
- Semantic document retrieval
- Document relevance grading
- Query rewriting with retry mechanism
- FastAPI REST API
- User feedback endpoint
- Source citations in generated answers
- Swagger/OpenAPI documentation
- Streamlit frontend

---

# Architecture

```
                          User
                            │
                            ▼
                    FastAPI (/query)
                            │
                            ▼
                  Query Analysis Node
                            │
                            ▼
                   Retrieve Documents
                            │
                            ▼
                 Document Grading Node
                     ┌────────┴────────┐
                     │                 │
              Relevant Docs     No Relevant Docs
                     │                 │
                     ▼                 ▼
              Generate Answer    Rewrite Query
                     │                 │
                     │          Retrieve Again
                     │                 │
                     │          Grade Documents
                     │                 │
                     └────────┬────────┘
                              │
                   Relevant After Retry?
                      │                 │
                     Yes               No
                      │                 │
                      ▼                 ▼
               Generate Answer     No Answer
                              │
                              ▼
                         API Response
```

---

# Tech Stack

- Python 3.10+
- FastAPI
- LangGraph
- LangChain
- ChromaDB
- HuggingFace Sentence Transformers
- Groq LLM
- Streamlit

---

# Project Structure

```text
technical-rag/
│
├── app/
│   ├── data/
│   │   └── feedback.json
│   │
│   ├── graph/
│   │   ├── state.py
│   │   └── workflow.py
│   │
│   ├── ingestion/
│   │   ├── embeddings.py
│   │   └── ingest.py
│   │
│   ├── nodes/
│   │   ├── query_node.py
│   │   ├── retrieve_node.py
│   │   ├── grade_node.py
│   │   ├── rewrite_node.py
│   │   ├── decision_node.py
│   │   ├── generate_node.py
│   │   └── no_answer_node.py
│   │
│   ├── retrieval/
│   │   └── retrieve.py
│   │
│   ├── frontend.py
│   ├── main.py
│   ├── schemas.py
│   └── .env
│
├── chroma_db/
├── documents/
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd technical-rag
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Environment Variables

Create a `.env` file inside the `app/` directory.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Running the Application

## Step 1: Start FastAPI

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Step 2: Start Streamlit

```bash
streamlit run app/frontend.py
```

---

# API Endpoints

## GET /

Health Check

### Response

```json
{
  "message": "Technical RAG Chatbot API"
}
```

---

## POST /query

### Request

```json
{
  "question": "What is FastAPI?"
}
```

### Response

```json
{
  "question": "What is FastAPI?",
  "answer": "FastAPI is a modern Python framework...

Sources:
- fastapi.md"
}
```
<img width="752" height="341" alt="Test query (1)- Postive answer" src="https://github.com/user-attachments/assets/9f69f3a6-a544-49fb-8738-ade93325478c" /> 
<img width="752" height="296" alt="Test query(2)- Positive Answer" src="https://github.com/user-attachments/assets/78eb695d-55bd-46be-8f10-3fd61d48e6b9" /> 
<img width="1611" height="755" alt="Test query(3)- Negative Answer" src="https://github.com/user-attachments/assets/752b9d8d-8724-48e2-9508-a310d7eb9171" /> 
<img width="1592" height="681" alt="Test query(4)- Negative Answer" src="https://github.com/user-attachments/assets/0341c651-45b0-4301-8988-9e8814ca4f10" />

---

## POST /ingest

Indexes all documentation into ChromaDB.

### Response

```json
{
  "message": "Documents indexed successfully."
}
```
<img width="752" height="282" alt="POST ingest (1)" src="https://github.com/user-attachments/assets/4eeaf53a-6518-4dfd-b218-69e082ffff4f" /> 
<img width="752" height="395" alt="POST ingest (2)" src="https://github.com/user-attachments/assets/0e2960b3-261e-4332-bff1-23f084fc71be" />

---

## GET /documents

Returns all indexed documents.

### Response

```json
{
  "count": 5,
  "documents": [
    "chromadb.md",
    "fastapi.md",
    "langchain.md",
    "langgraph.md",
    "pydantic.md"
  ]
}
```
<img width="752" height="292" alt="Test documents (1)" src="https://github.com/user-attachments/assets/3be726b5-350b-4ee7-b168-79e4db33c7b6" /> 
<img width="752" height="329" alt="Test documents (2)" src="https://github.com/user-attachments/assets/9bf50cfa-fd99-4ef0-b27e-037a85a09263" />

---

## POST /feedback

Stores user feedback.

### Request

```json
{
  "question": "What is FastAPI?",
  "answer": "...",
  "rating": 5,
  "comment": "Helpful answer"
}
```

### Response

```json
{
  "message": "Feedback stored successfully."
}
```
<img width="752" height="361" alt="POST feedback (1)" src="https://github.com/user-attachments/assets/93f69235-20fe-45c8-b08a-b2a445a9fae8" /> <img width="752" height="406" alt="POST feedback (2)" src="https://github.com/user-attachments/assets/ee1b670f-a569-4531-8965-75baf53a14d8" />

---

# Document Corpus

The chatbot indexes the technical documentation stored inside the **documents/** directory.

Included documentation:

- FastAPI
- LangChain
- LangGraph
- ChromaDB
- Pydantic

These documents are embedded and stored in ChromaDB during ingestion.

---

# Workflow

The chatbot follows a **self-corrective Retrieval-Augmented Generation (RAG)** workflow.

1. The user submits a question through the FastAPI endpoint.
2. The **Query Analysis Node** processes the input.
3. The **Retrieval Node** performs semantic similarity search in ChromaDB.
4. The **Document Grading Node** evaluates whether the retrieved documents are relevant.
5. If relevant documents are found, the **Generation Node** generates an answer using the LLM and includes source citations.
6. If the retrieved documents are not relevant, the **Rewrite Node** reformulates the query and retries retrieval.
7. If relevant documents are found after rewriting, the answer is generated.
8. If no relevant documents are found after the retry, the chatbot returns:

```
I don't know based on the available documentation.
```

This workflow ensures that responses are grounded in the indexed documentation and reduces hallucinations.

---

# Chunking Strategy

The documentation corpus is loaded from the `documents/` directory and split using LangChain's **RecursiveCharacterTextSplitter** before generating embeddings.

The splitter divides documents into overlapping chunks to preserve context between adjacent sections while maintaining efficient retrieval.

**Update the values below to match your implementation:**

- Chunk Size: **1000**
- Chunk Overlap: **200**

---

# Embedding Strategy

Document chunks are converted into dense vector embeddings using a HuggingFace Sentence Transformer model.

Both user queries and document chunks are embedded into the same vector space, enabling semantic similarity search through ChromaDB instead of exact keyword matching.

**Update this with your actual embedding model**, for example:

```
sentence-transformers/all-MiniLM-L6-v2
```

---

# Design Decisions and Tradeoffs

## Why LangGraph?

LangGraph was selected because it provides explicit workflow orchestration with conditional routing between retrieval, grading, query rewriting, and answer generation.

## Why ChromaDB?

ChromaDB is lightweight, open-source, and integrates well with LangChain, making it suitable for local semantic search.

## Why Semantic Search?

Embedding-based retrieval enables the chatbot to retrieve relevant documents even when the wording of the user's question differs from the wording in the documentation.

## Why Query Rewriting?

Instead of immediately returning "No Answer", the chatbot retries retrieval using a rewritten query, increasing the likelihood of retrieving relevant documentation.

## Tradeoffs

- The current query rewriting strategy is rule-based. An LLM-based rewriting approach would improve retrieval quality.
- The project uses a local ChromaDB instance. A cloud-hosted vector database such as Pinecone, Weaviate, or Milvus would improve scalability for larger document collections.

---

# Assumptions

- Users ask questions related to the indexed technical documentation.
- The document corpus is relatively small and suitable for local ChromaDB storage.
- Answers should only be generated from indexed documents.
- If relevant information is unavailable, the chatbot should return a safe fallback response instead of generating unsupported content.

---

## Streamlit Interface
<img width="1877" height="820" alt="Technical RAG Chatbot (1) Postive Answer" src="https://github.com/user-attachments/assets/ce26b5f6-0ed0-4321-bbd7-e8f693d4e98d" />
<img width="1770" height="502" alt="Technical RAG Chatbot (2) Negative Answer" src="https://github.com/user-attachments/assets/7c90768e-6beb-47c8-b608-9ecf75d148d6" />
<img width="1887" height="757" alt="Technical RAG Chatbot " src="https://github.com/user-attachments/assets/c3c047bf-3811-4cbb-aed9-371290c4e880" />

---

# Future Improvements

- LLM-based intelligent query rewriting.
- Hybrid retrieval (keyword + semantic search).
- Metadata-aware document filtering.
- Multi-turn conversational memory.
- Docker containerization.
- CI/CD pipeline.
- Cloud-hosted vector database.
- Support for PDF, DOCX, and HTML documentation.

---

# Author

**Roshan Patil**

AI/ML Engineer Intern Assignment
