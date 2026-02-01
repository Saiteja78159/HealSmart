import streamlit as st
import requests
import google.generativeai as genai
from geopy.distance import geodesic
import folium
from streamlit_folium import st_folium
from api_key import GEMINI_API_KEY, GEOAPIFY_API_KEY
from rag_retriever import load_retriever

# ---------------- CONFIG ----------------
st.set_page_config("HealSmart", layout="centered")
st.title("🩺 HealSmart – AI Diagnosis & Hospital Finder")

genai.configure(api_key=GEMINI_API_KEY)
retriever = load_retriever()

# ---------------- UTILITIES ----------------
@st.cache_data
def get_location(address):
    url = f"https://api.geoapify.com/v1/geocode/search?text={address}&apiKey={GEOAPIFY_API_KEY}"
    res = requests.get(url).json()
    if res.get("features"):
        lon, lat = res["features"][0]["geometry"]["coordinates"]
        return lat, lon
    return None

@st.cache_data
def get_hospitals(lat, lon):
    url = f"https://api.geoapify.com/v2/places?categories=healthcare.hospital&filter=circle:{lon},{lat},5000&limit=10&apiKey={GEOAPIFY_API_KEY}"
    return requests.get(url).json()

# ---------------- IMAGE UPLOAD ----------------
image = st.file_uploader("Upload a medical image", ["png", "jpg", "jpeg"])

if image:
    img_bytes = image.read()
    st.image(img_bytes, caption="Uploaded Image", use_column_width=True)

    # ---------------- RAG CONTEXT ----------------
    docs = retriever.get_relevant_documents(
        "medical image diagnosis symptoms and conditions"
    )
    context = "\n\n".join(d.page_content for d in docs)

    system_prompt = f"""
You are an AI medical assistant.

Use the following verified medical knowledge:
--------------------------------
{context}
--------------------------------

Instructions:
- Analyze the image carefully
- Identify possible medical conditions
- Suggest precautions and next steps
- Do NOT provide final diagnosis

Always include:
"Consult a qualified doctor before making any decisions."
"""

    # ---------------- GEMINI CALL ----------------
    model = genai.GenerativeModel("gemini-1.5-pro-002")
    chat = model.start_chat(
        history=[{
            "role": "user",
            "parts": [
                {"inline_data": {"mime_type": image.type, "data": img_bytes}},
                {"text": system_prompt}
            ]
        }]
    )

    response = chat.send_message("Analyze the image using medical context.")
    st.subheader("🧠 AI Medical Insights")
    st.write(response.text)

    # ---------------- HOSPITAL FINDER ----------------
    location = get_location("Medchal")  # can be replaced by GPS/IP
    if location:
        lat, lon = location
        hospital_data = get_hospitals(lat, lon)

        map_ = folium.Map(location=[lat, lon], zoom_start=13)
        folium.Marker([lat, lon], tooltip="Your Location").add_to(map_)

        st.sidebar.header("🏥 Nearby Hospitals")

        for h in hospital_data.get("features", []):
            name = h["properties"].get("name", "Hospital")
            h_lat = h["geometry"]["coordinates"][1]
            h_lon = h["geometry"]["coordinates"][0]
            dist = geodesic((lat, lon), (h_lat, h_lon)).km

            folium.Marker(
                [h_lat, h_lon],
                tooltip=f"{name} ({dist:.2f} km)",
                icon=folium.Icon(color="red")
            ).add_to(map_)

            st.sidebar.write(f"{name} – {dist:.2f} km")

        st_folium(map_, width=700, height=500)
