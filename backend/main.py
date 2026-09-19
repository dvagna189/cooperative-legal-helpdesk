from fastapi import FastAPI
from pydantic import BaseModel

from router import classify_query
from rag import search_documents
from grievance import generate_grievance_letter

app = FastAPI()


class ChatRequest(BaseModel):
    message: str
    language: str = "English"


@app.get("/")
def home():
    return {
        "message": "Cooperative & Legal Helpdesk is running"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    category = classify_query(request.message)

    documents = search_documents(request.message)

    return {
        "question": request.message,
        "category": category,
        "documents": documents,
        "language": request.language
    }
