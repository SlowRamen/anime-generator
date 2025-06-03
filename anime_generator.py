# -*- coding: utf-8 -*-
import streamlit as st
import requests
import base64

# === Page Config ===
st.set_page_config(
    page_title="Anime Backstory Generator",
    page_icon="🗡️",
    layout="wide"
)

# === Custom Styling ===
custom_css = """
<style>
body {
    background-color: #0d0d0d;
    background-image: url('fartttttttttt.png');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #f2f2f2;
    font-family: 'Courier New', Courier, monospace;
}

h1, h2, h3, .stTextInput > label, .stSelectbox > label, .stButton > button {
    color: #ff007f !important;
}

.stTextInput, .stSelectbox, .stButton > button {
    background-color: rgba(15, 15, 15, 0.8);
    border: 1px solid #ff007f;
    color: #ffffff;
}

.stTextArea {
    background-color: rgba(10, 10, 10, 0.85);
    border: 1px solid #ff007f;
    color: #ffffff;
}

footer {
    visibility: hidden;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# === Title ===
st.title("Anime Backstory Generator")
st.markdown("_Craft a dramatic origin story for your next anime protagonist._")

# === Input Section ===
name = st.text_input("🧍 Character Name")
setting = st.text_input("🌍 World/Setting (e.g., Neo-Tokyo, magic school)")
theme = st.selectbox("🎭 Theme", ["Revenge", "Love", "Honor", "Power", "Destiny"])

# === Backstory Generator ===
if st.button("✨ Generate Backstory"):
    if not name or not setting:
        st.warning("Please fill in both name and setting.")
    else:
        with st.spinner("Summoning anime plot energy..."):
            prompt = f"""
Create an anime-style backstory for a character named {name} in a setting called {setting}, with a theme of {theme}.
Include:
1. A dramatic origin story (2-3 paragraphs)
2. 3 fake anime episode titles related to their journey
Format it like a fan wiki entry.
"""

            headers = {
                "Authorization": f"Bearer {st.secrets['api_key']}",
                "HTTP-Referer": "https://anime-backstory.streamlit.app",
                "X-Title": "Anime Backstory Generator"
            }

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                json={
                    "model": "mistralai/mistral-7b-instruct",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ]
                },
                headers=headers
            )

            if response.status_code == 200:
                content = response.json()["choices"][0]["message"]["content"]
                st.text_area("📜 Backstory", content, height=400)
            else:
                st.error(f"❌ Failed to generate: {response.status_code}")
