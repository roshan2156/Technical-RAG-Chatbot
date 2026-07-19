# ChromaDB Documentation

# Introduction

ChromaDB is an open-source vector database designed for AI applications. It provides the infrastructure needed to store documents, generate and manage embeddings, and retrieve information using semantic similarity.

ChromaDB is commonly used in Retrieval-Augmented Generation (RAG) systems, chatbots, recommendation systems, document search, and AI assistants.

Unlike traditional databases that search using exact keywords, ChromaDB searches based on the meaning of the text using vector embeddings.

---

# Key Features

- Store documents and metadata
- Store vector embeddings
- Semantic similarity search
- Metadata filtering
- Full-text search
- Support for multiple embedding models
- Persistent vector storage
- Fast retrieval
- Integration with LangChain and LangGraph
- Support for multimodal data

---

# Collections

A Collection is the primary storage unit in ChromaDB.

Collections store:

- Documents
- Embeddings
- Metadata
- Unique document IDs

Every document inserted into ChromaDB belongs to a collection.

A collection acts like a table in a relational database but is optimized for vector search.

### Collection Components

Each record inside a collection contains:

- Document ID
- Document Text
- Embedding Vector
- Metadata

Example:

| ID | Document | Metadata |
|----|----------|----------|
| doc1 | FastAPI Introduction | category = API |
| doc2 | LangGraph Nodes | category = AI |
| doc3 | Pydantic Validation | category = Python |

---

# Creating Collections

A collection is created by providing a unique name.

Collection names should:

- Be unique
- Contain lowercase letters, numbers, underscores, or hyphens
- Be between 3 and 512 characters

Collections can also include:

- Metadata
- Embedding functions
- Index configuration

---

# Collection Operations

Common collection operations include:

### Create Collection

Creates a new collection for storing documents.

### Get Collection

Retrieves an existing collection.

### Get or Create Collection

Returns the collection if it exists, otherwise creates a new one.

### List Collections

Returns all collections stored in the database.

### Modify Collection

Updates collection metadata or configuration.

### Delete Collection

Removes the collection and all associated documents and embeddings.

---

# Adding Documents

Documents can be added to a collection along with unique IDs and optional metadata.

Each document may contain:

- Text
- Metadata
- Embedding
- Document ID

If embeddings are not provided, ChromaDB automatically generates them using the collection's embedding function.

---

# Metadata

Metadata provides additional information about documents.

Examples include:

- Category
- Author
- Source
- Date
- Language
- Topic

Metadata can be used to filter search results.

Example metadata:

```
Category = "FastAPI"
Language = "English"
Author = "Documentation"
```

---

# Embeddings

Embeddings are numerical vector representations of data.

Instead of storing only text, ChromaDB converts documents into vectors that represent their semantic meaning.

Similar documents have vectors that are close together in vector space.

Embeddings can represent:

- Text
- Images
- Audio
- Other multimodal data

---

# Embedding Functions

Embedding functions convert raw data into vector embeddings.

ChromaDB supports many embedding providers, including:

- OpenAI
- Sentence Transformers
- Hugging Face
- Cohere
- Google Generative AI
- Mistral

If no embedding function is specified, ChromaDB uses a default embedding function based on Sentence Transformers.

---

# Default Embedding Model

By default, ChromaDB uses the **all-MiniLM-L6-v2** Sentence Transformers model.

This model creates high-quality sentence and document embeddings suitable for semantic search.

---

# Similarity Search

Similarity Search is the process of finding documents that have meanings similar to a user's query.

Instead of matching exact keywords, ChromaDB compares embedding vectors.

Documents with the smallest vector distance are considered the most relevant.

### Search Process

```
User Query
      |
      v
Generate Query Embedding
      |
      v
Compare with Stored Embeddings
      |
      v
Find Most Similar Documents
      |
      v
Return Results
```

---

# Vector Search

Vector search compares embeddings using mathematical distance.

Common distance metrics include:

- Cosine Similarity
- Euclidean Distance (L2)
- Inner Product

The closest vectors represent the most semantically similar documents.

---

# Querying Collections

Users search collections by submitting a query.

The query is converted into an embedding.

ChromaDB compares the query embedding with stored document embeddings and returns the closest matches.

Returned results may include:

- Documents
- IDs
- Metadata
- Distances
- Embeddings

---

# Metadata Filtering

Metadata filtering narrows search results.

Instead of searching every document, users can filter by metadata.

Examples:

- Category = "Machine Learning"
- Author = "OpenAI"
- Language = "English"

Filtering improves retrieval accuracy.

---

# Updating Data

Existing records can be modified.

Updated information may include:

- Documents
- Embeddings
- Metadata

If a document changes and embeddings are not supplied, ChromaDB automatically recomputes the embedding.

---

# Upsert

Upsert combines update and insert.

If the document exists:

- Update it.

If the document does not exist:

- Create it.

This simplifies data synchronization.

---

# Deleting Data

Documents can be removed by:

- Document ID
- Metadata filter

Deleting a document also removes its associated embeddings and metadata.

Deletion is permanent.

---

# Persistence

ChromaDB supports persistent storage.

Unlike in-memory databases, persistent storage allows data to remain available after the application restarts.

This is especially useful for production RAG systems.

---

# Multimodal Retrieval

ChromaDB supports storing and retrieving multiple data types.

Supported modalities include:

- Text
- Images

The same collection can contain both textual and image data when using a multimodal embedding function.

---

# Advantages of ChromaDB

- Easy to use
- Open source
- Fast vector search
- Automatic embedding generation
- Metadata filtering
- Persistent storage
- Supports multiple embedding models
- Scalable architecture
- Excellent for RAG applications
- Integrates with LangChain and LangGraph

---

# Common Use Cases

ChromaDB is commonly used for:

- Retrieval-Augmented Generation (RAG)
- AI Chatbots
- Document Search
- Knowledge Bases
- Semantic Search
- Question Answering Systems
- Recommendation Systems
- Enterprise Search
- Code Search
- AI Assistants

---

# Summary

ChromaDB is an open-source vector database built for AI applications. It organizes information into collections that store documents, embeddings, metadata, and unique identifiers. Using embedding functions, ChromaDB converts data into vectors and performs similarity search to retrieve semantically relevant information. Features such as metadata filtering, persistent storage, and support for multiple embedding models make ChromaDB an ideal choice for Retrieval-Augmented Generation (RAG) systems and intelligent search applications.