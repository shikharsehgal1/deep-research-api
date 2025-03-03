# Deep Research API

A FastAPI-based service for semantic (RAG) document search. This project indexes documents with local embeddings (Hugging Face) and allows you to query them via a REST API.

## Features

- **Document Indexing**: `POST /documents/` to store new documents in the vector store  
- **Semantic Search**: `POST /search/` to retrieve the most relevant documents for a given query  
- **Local Embeddings**: Uses Hugging Face sentence-transformers instead of OpenAI (no API key needed)  
- **ChromaDB**: Stores embeddings locally in the `chroma_db` folder  

## Installation

1. **Clone or Download** this repo
2. **Create a Virtual Environment**
3. **Install Dependencies**

## Running Locally

Start the FastAPI Server: uvicorn main:app --reload
Access the API at http://127.0.0.1:8000.
Interactive Docs are available at http://127.0.0.1:8000/docs.

For Documents, after you click 'Try it Out', use: 
{
  "content": "Text of your document here...",
  "metadata": {
    "title": "Optional Title",
    "author": "Optional Author"
  }
}

To search documents:
{
  "query": "Question?",
  "top_k": 3
}
