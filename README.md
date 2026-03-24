# School Chatbot using RAG, LangChain, FastAPI & Streamlit

This project is a **School Information Chatbot** built using **LangChain, OpenAI, and RAG (Retrieval-Augmented Generation)**.
It answers user queries by retrieving relevant information from a dataset and generating accurate responses using an LLM.

The system combines **vector search + LLM reasoning** to provide context-aware answers.

---

##  Features

* Answer school-related questions
* RAG-based context-aware responses
* Semantic search using vector database
* FastAPI backend for real-time API
* Streamlit UI for chatbot interface
* Secure API key handling using `.env`
* Persistent vector database (ChromaDB)

---

##  Technologies Used

* Python
* LangChain
* OpenAI (LLM + Embeddings)
* Chroma Vector Database
* FastAPI (Backend API)
* Streamlit (Frontend UI)

---

##  Workflow

1. Load the dataset containing school information
2. Split the text into smaller chunks using a text splitter
3. Convert text chunks into embeddings
4. Store embeddings in a vector database (ChromaDB)

###  Query Flow

5. User asks a question (via UI or API)
6. Convert the query into embeddings
7. Perform similarity search in vector DB
8. Retrieve relevant chunks (context)
9. Send context + query to LLM
10. LLM generates final answer

---

##  System Architecture

```id="7rmk3y"
School Dataset
      │
      ▼
Text Splitter
      │
      ▼
Embeddings Model
      │
      ▼
Vector Database (Chroma)
      │
      ▼
User Query (UI / API)
      │
      ▼
Query Embedding
      │
      ▼
Similarity Search
      │
      ▼
LLM (Generate Answer)
      │
      ▼
Chatbot Response
```

---

## How to Run

### 1. Install dependencies

```bash id="9e7bq4"
pip install -r requirements.txt
```

---

### 2. Add API key

Create `.env` file:

```env id="4z2m1r"
OPENAI_API_KEY=your_api_key_here
```

---

### 3. Run FastAPI backend

```bash id="m3qv9x"
uvicorn app:app --reload
```

---

### 4. Run Streamlit UI

```bash id="g7yt8c"
streamlit run ui.py
```

---

##  Access

* API Docs: http://127.0.0.1:8000/docs
* Chat UI: http://localhost:8501

---

##  Example Query

**User:** What facilities are available in the school?

**Bot:** Our school provides laboratories, a library, sports facilities, and smart classrooms.

 Author

**Omkar Jadhav**
