# 🩺 HealSmart: AI Diagnosis & Hospital Finder

HealSmart is an AI-powered medical assistant that analyzes uploaded medical images using **Gemini multimodal models**, enhances reliability using **Retrieval-Augmented Generation (RAG)** with verified medical literature, and helps users locate **nearby hospitals** based on their location.

This project is designed to be **interview-ready**, ethically safe, and technically sound.

---

## 🚀 Key Features

* 🧠 **AI Medical Image Analysis**
  Analyzes uploaded medical images (X-rays, skin images, etc.) using Gemini 1.5 Pro and provides possible medical insights.

* 📚 **Retrieval-Augmented Generation (RAG)**
  Grounds AI responses with verified medical documents (PDF/TXT) using LangChain + FAISS to reduce hallucinations.

* 🧬 **Medical Knowledge Base**
  Supports WHO/NIH-style guidelines and curated medical PDFs.

* 🏥 **Hospital Finder**
  Uses Geoapify API to find nearby hospitals and displays them on an interactive map.

* ⚡ **Optimized & Secure**
  Caching for faster responses and secure API key management.

---

## 🧠 System Architecture

```
User → Streamlit UI → RAG Pipeline → Gemini AI → Medical Insights
                          ↓
                     Geoapify API
                          ↓
                    Nearby Hospitals
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **AI Model:** Gemini 1.5 Pro (Multimodal)
* **RAG Framework:** LangChain
* **Vector Store:** FAISS
* **Embeddings:** Google Embedding-001
* **Maps:** Folium
* **Location Services:** Geoapify API

---

## 📁 Project Structure

```
HealSmart/
│
├── app.py                  # Main Streamlit application
├── rag_setup.py             # Builds FAISS vector database (run once)
├── rag_retriever.py         # Loads retriever for RAG
├── api_key.py               # API keys (not committed)
├── medical_docs/            # Medical PDFs/TXT for RAG
│     ├── skin_diseases.pdf
│     ├── xray_guidelines.pdf
│
└── medical_vector_db/       # FAISS vector store
```

---

## 🔑 API Keys Setup

Create a file called `api_key.py`:

```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
GEOAPIFY_API_KEY = "YOUR_GEOAPIFY_API_KEY"
```

---

## 📚 Building the Medical Knowledge Base (RAG)

Run **once** to build the vector database:

```bash
python rag_setup.py
```

This step:

* Loads medical PDFs/TXT
* Splits text into chunks
* Generates embeddings
* Stores them in FAISS

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Steps:

1. Upload a medical image
2. AI analyzes image using medical context
3. View AI-generated insights
4. See nearby hospitals on the map

---


## 🔮 Future Enhancements

* Hospital ratings using Google Places API
* Confidence scoring for AI predictions
* Chat-based follow-up medical Q&A
* Cloud deployment (Docker / GCP / AWS)
* User GPS-based location detection

---

## 👨‍💻 Author

**Sai Teja**
AI / ML Engineer | Computer Vision | GenAI | RAG Systems

---

⭐ If you find this project useful, consider starring the repository!
