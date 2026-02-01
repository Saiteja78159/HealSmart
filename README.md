User
 │
 │ Upload Medical Image
 ▼
Streamlit Frontend
 │
 │ 1. Image Display
 │ 2. User Interaction
 ▼
RAG Pipeline (Backend)
 │
 ├── Medical Knowledge Base (PDF / TXT)
 │        ↓
 │   Text Splitter
 │        ↓
 │   Embeddings (Google Embedding-001)
 │        ↓
 │   Vector Store (FAISS)
 │        ↓
 │   Retriever (Top-K medical context)
 │
 ├── Image Analysis (Gemini 1.5 Pro)
 │        ↑
 │   Image + Retrieved Medical Context
 │
 ▼
AI Medical Response
 │
 │ Findings + Precautions + Disclaimer
 ▼
Hospital Finder Module
 │
 ├── Geoapify Geocoding
 ├── Nearby Hospital Search
 ├── Distance Calculation
 └── Map Visualization (Folium)
 │
 ▼
User Output
