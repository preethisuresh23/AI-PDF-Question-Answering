from fastapi import FastAPI, UploadFile, File
from pdf_processor import extract_text_from_pdf, chunk_text
from rag_pipeline import create_vector_store

app = FastAPI()

vector_store = None


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global vector_store

    with open("uploaded.pdf", "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf("uploaded.pdf")
    chunks = chunk_text(text)
    vector_store = create_vector_store(chunks)

    return {"message": "PDF processed successfully!"}


@app.post("/ask")
def ask_question(question: str):
    global vector_store

    if vector_store is None:
        return {"error": "No PDF uploaded yet."}

    results = vector_store.similarity_search(question)

    if not results:
        return {"answer": "No relevant information found."}

    return {
        "answer": results[0].page_content
    }



