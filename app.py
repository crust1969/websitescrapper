import streamlit as st
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import io

st.title("🌐 Website Content Extractor (JS Compatible)")

url = st.text_input("Enter a website URL:", placeholder="https://www.handelsblatt.com")

def extract_with_playwright(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle", timeout=15000)
        html = page.content()
        browser.close()
        return html

if url:
    try:
        html = extract_with_playwright(url)
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text(separator="\n", strip=True)

        st.subheader("📄 Extracted Content")
        st.text_area("Page Text", text, height=400)

        buffer = io.BytesIO(text.encode("utf-8"))
        st.download_button(
            label="📥 Download .txt",
            data=buffer,
            file_name="website_content.txt",
            mime="text/plain"
        )
    except Exception as e:
        st.error(f"Error extracting content: {e}")
