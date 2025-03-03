import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import uvicorn

from dotenv import load_dotenv

load_dotenv()

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma(
    embedding_function=embeddings,
    collection_name="research_docs",
    persist_directory="./chroma_db" 
)

class Document(BaseModel):
    content: str
    metadata: Dict[str, Any] = {}

class Query(BaseModel):
    query: str
    top_k: int = 5

app = FastAPI()

@app.post("/documents/")
def add_document(doc: Document):
    try:
        vector_store.add_texts([doc.content], metadatas=[doc.metadata])
        vector_store.persist()  # saves to disk
        return {"status": "Document indexed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search/")
def search(query: Query):
    try:
        results = vector_store.similarity_search(query.query, k=query.top_k)
        formatted_results = [
            {"content": res.page_content, "metadata": res.metadata} for res in results
        ]
        return {"results": formatted_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
