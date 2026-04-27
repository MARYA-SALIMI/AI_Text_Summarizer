# AI Text Summarizer (Full-Stack Project)

## 🚀 Overview
This is a full-stack AI-powered text summarization web application.  
Users can paste long text and receive an AI-generated summary.

The system processes input text using a transformer-based model and stores generated summaries in a database for later access.

---

## ✨ Features

- 🧠 AI-powered text summarization
- ⚡ Automatic summary generation from user input
- 💾 Persistent storage using PostgreSQL
- 📜 History of previous summaries
- 🌐 Full-stack architecture (React + FastAPI)

---

## 🧰 Tech Stack

### Frontend:
- React (Vite)
- JavaScript
- Fetch API

### Backend:
- FastAPI
- Python
- SQLAlchemy

### Database:
- PostgreSQL

### AI:
- HuggingFace Transformers (summarization model)

---

## 🏗️ Architecture

User → React Frontend → FastAPI Backend → AI Model → PostgreSQL Database

---

## ⚙️ How to Run the Project

### 1. Clone repository
```
git clone <your-repo-url>
```

### 2. Environment Setup
```
Update your backend database URL:
postgresql://postgres:password@localhost:5433/ai_summarizer
```


### 3. Backend setup
```
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```


### 4. Frontend setup
```
cd frontend
npm install
npm run dev
```


