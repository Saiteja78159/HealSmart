import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS

def load_documents(folder="medical_docs"):
    docs = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if file.endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())
        elif file.endswith(".txt"):
            docs.extend(TextLoader(path).load())
    return docs

def build_vector_db():
    documents = load_documents()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("medical_vector_db")

if __name__ == "__main__":
    build_vector_db()
