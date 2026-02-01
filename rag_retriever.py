from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def load_retriever():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )
    vectorstore = FAISS.load_local(
        "medical_vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vectorstore.as_retriever(search_kwargs={"k": 3})
