from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from .database import engine, SessionLocal
from .models import Summary
from .database import Base



app = FastAPI()
summarizer = pipeline("summarization",model="google/pegasus-large")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def func():
    return{
        "message": "AI Text Summarizer API is running"
    }
    

class TextRequest(BaseModel):
    text: str


@app.post("/summarize")
def summarize(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    result = summarizer(request.text, do_sample=False)

    db = SessionLocal()
    new_summary = Summary(
    original_text=request.text,
    summary_text=result[0]["summary_text"])
    db.add(new_summary)
    db.commit()
    db.close()
    return {
        "original_text": request.text,
        "summary": result[0]["summary_text"] #pipline returns a list of dictionaries, we take the first one and extract the summary text
    }


@app.get("/history")
def get_history():
    db = SessionLocal()
    summaries = db.query(Summary).all()
    db.close()

    return summaries


