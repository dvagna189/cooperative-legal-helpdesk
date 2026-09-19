from fastapi import FastAPI
from pydantic import BaseModel

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
    return {
        "reply": "I received your question.",
        "language": request.language
    }
