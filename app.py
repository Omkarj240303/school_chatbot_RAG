from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import get_answer

app = FastAPI()

# request format
class Query(BaseModel):
    question: str

# home route
@app.get("/")
def home():
    return {"message": "School Chatbot API Running"}
@app.get("/health")
def health():
    return {"status": "ok"}


# main chatbot route
@app.post("/ask")
def ask(query: Query):
    answer = get_answer(query.question)
    return {"answer": answer}
