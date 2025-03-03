# Deep Research API

FastAPI service for RAG document search. Uses local embeddings (Hugging Face) since I had no OpenAI credits.

## Installation

1. **Clone or Download** this repo
2. **Create a Virtual Environment**
3. **Install Dependencies (included)**

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
