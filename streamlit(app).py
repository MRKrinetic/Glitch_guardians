import streamlit as st
from PIL import Image
import pytesseract
import requests
from googletrans import Translator
import re

# Configure Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Define language options
LANGUAGES = {"English": "en", "Hindi": "hi", "Marathi": "mr"}

st.title("🌍 AI-Powered OCR + Distance + Translation Tool")

uploaded_image = st.file_uploader("Upload an image (handwritten or printed text)", type=["jpg", "png", "jpeg"])
extracted_text = ""

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    extracted_text = pytesseract.image_to_string(image)
    st.write("*Extracted Text:*", extracted_text)

text_input = st.text_area("Or enter text manually", extracted_text if extracted_text else "")

def clean_location(text):
    text = re.sub(r'[^a-zA-Z0-9\s,]', '', text)
    return text.strip()

if text_input.strip():
    # Extract source and destination manually from input
    st.markdown("### Enter Source and Destination")
    source = st.text_input("Source Location")
    destination = st.text_input("Destination Location")

    if source and destination:
        source_clean = clean_location(source)
        destination_clean = clean_location(destination)

        st.write(f"**Source (cleaned):** {source_clean}")
        st.write(f"**Destination (cleaned):** {destination_clean}")

        # GoMap API for distance
        gomap_api_key = "AlzaSyz7hvFYjBQHPCMGvRLqzlog7l5qW4UZHnr"
        gomap_url = f"https://gomapapi.com/api/distance?origin={source_clean}&destination={destination_clean}&key={gomap_api_key}"
        try:
            gomap_response = requests.get(gomap_url, timeout=10)
            gomap_response.raise_for_status()
            dist = gomap_response.json()
            st.info(f"Distance: {dist.get('distance', 'N/A')} | Duration: {dist.get('duration', 'N/A')}")
        except requests.exceptions.RequestException as e:
            st.error(f"GoMap API failed: {e}")

    # Translation section
    st.markdown("### Translate the Extracted Text")
    source_lang = st.selectbox("Select source language", options=list(LANGUAGES.keys()), index=0)
    target_lang = st.selectbox("Select target language", options=list(LANGUAGES.keys()), index=1)

    if st.button("Translate Text"):
        try:
            translator = Translator()
            translated_text = translator.translate(text_input, src=LANGUAGES[source_lang], dest=LANGUAGES[target_lang])
            st.success(f"*Translated Text:* {translated_text.text}")
        except Exception as e:
            st.error(f"Translation failed: {e}")
else:
    st.info("Upload an image or enter text manually.")

st.markdown("Powered by Google Translate API, Tesseract OCR, and GoMap API")
