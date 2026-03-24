### An AI-powered chatbot that answers school-related queries using Retrieval-Augmented Generation (RAG).
### It retrieves relevant information from a knowledge base and generates accurate, context-aware responses.

# Features

 Chat-based interface for user queries
 Context-aware answers using RAG
 FastAPI backend for real-time responses
 ChromaDB vector database for semantic search
 Streamlit UI for interactive experience
 Secure API key handling using .env

 # Architecture
User → Streamlit UI → FastAPI → RAG Pipeline  
→ Retriever (ChromaDB) → OpenAI LLM → Response → UI

# Tech Stack
Language: Python
LLM: OpenAI (GPT-4.1-nano)
Framework: LangChain
Vector DB: ChromaDB
Backend: FastAPI
Frontend: Streamlit

# Example Query
What are the school timings?

# Key Learnings
Built an end-to-end AI system using RAG
Integrated LLMs with vector databases
Developed REST APIs using FastAPI
Created interactive UI with Streamlit

# Author
Omkar Jadhav
