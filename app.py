import streamlit as st
import requests
from bs4 import BeautifulSoup
import io

st.set_page_config(page_title="Website Content Extractor", layout="centered")

st.title("🌐 Website Content Extractor")

url = st.text_input("Enter a website URL:", placeholder="https://example.com")

if url:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text(separator='\n', strip=True)

        st.subheader("📄 Extracted Text Content:")
        st.text_area("Website Text", content, height=400)

        # Download button
        content_bytes = content.encode('utf-8')
        buffer = io.BytesIO(content_bytes)
        st.download_button(
            label="📥 Download Text as .txt",
            data=buffer,
            file_name="website_content.txt",
            mime="text/plain"
        )

    except requests.exceptions.RequestException as e:
        st.error(f"Error downloading content: {e}")
