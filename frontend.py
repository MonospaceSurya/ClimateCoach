import streamlit as st
import os
from PyPDF2 import PdfReader
from llm import llm

st.title("PDF GPT-3 Chatbot")

# GPT-3 API endpoint and credentials
endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
api_key = "YOUR_API_KEY"

# Initialize the chat history
history = []

# Create a file uploader for the PDF document
pdf_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if pdf_file is not None:

    reader = PdfReader("input.pdf")

    # read data from the file and put them into a variable called raw_text
    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text

    # Create a text input for the user's message
    message = st.text_input("User")
    #print(llm(message))