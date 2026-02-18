# 📄 AI PDF Question Answering System

An AI-powered backend system that allows users to upload a PDF and ask questions about its content.

Built using FastAPI, LangChain, FAISS, and HuggingFace Embeddings.

---

## 🚀 Features

- Upload any PDF file
- Extract text from PDF
- Split text into intelligent chunks
- Create vector embeddings using sentence-transformers
- Store embeddings using FAISS
- Ask questions and retrieve relevant answers
- REST API with FastAPI
- Swagger UI documentation available

---

## 🛠 Tech Stack

- Python
- FastAPI
- LangChain
- FAISS
- HuggingFace Embeddings
- Sentence Transformers
- Uvicorn

---

## 📂 Project Structure

SmartDocumentAI/
│── main.py
│── pdf_processor.py
│── rag_pipeline.py
│── requirements.txt
│── .gitignore

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/AI-PDF-Question-Answering.git
cd AI-PDF-Question-Answering
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
