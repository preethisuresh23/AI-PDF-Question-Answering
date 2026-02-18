from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter



def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def chunk_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(text)
    return chunks


if __name__ == "__main__":
    sample_file = "sample.pdf"

    extracted_text = extract_text_from_pdf(sample_file)

    chunks = chunk_text(extracted_text)
    print("Total chunks:", len(chunks))
    print("\nFirst chunk preview:\n")
    print(chunks[0])
