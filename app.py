import streamlit as st
import requests
from bs4 import BeautifulSoup
import io

st.title("🌐 Website Content Extractor (No JS Support)")

url = st.text_input("Enter a website URL:", placeholder="https://www.handelsblatt.com")

SCRAPERAPI_KEY = "YOUR_API_KEY"  # Get from https://www.scraperapi.com/

if url:
    try:
        api_url = f"http://api.scraperapi.com?api_key={SCRAPERAPI_KEY}&url={url}"
        response = requests.get(api_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text(separator="\n", strip=True)

        st.subheader("📄 Extracted Content")
        st.text_area("Page Text", content, height=400)

        buffer = io.BytesIO(content.encode("utf-8"))
        st.download_button(
            label="📥 Download .txt",
            data=buffer,
            file_name="website_content.txt",
            mime="text/plain"
        )
    except Exception as e:
        st.error(f"Error extracting content: {e}")

