from fastapi import FastAPI
from app.models import ChatRequest
from app.rag import ask
from app.ingest import ingest_documents

app = FastAPI()

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "answer": ask(request.question)
    }

@app.post("/ingest")
def ingest():
    ingest_documents()
    return {
        "status": "success"
    }