

import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS


# Get your API keys from openai, y ouwill need to create an account. 
# Here is the link to get the keys: https://platform.openai.com/account/billing/overview
import os


os.environ["OPENAI_API_KEY"] = "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"

# connect your Google Drive

#pdf_file = st.file_uploader("Upload a PDF document", type=["pdf"])
# location of the pdf file/files.

# Create a file uploader for the PDF document


reader = PdfReader("input.pdf")



# read data from the file and put them into a variable called raw_text
raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

# raw_text

raw_text[:100]

# We need to split the text that we read into smaller chunks so that during information retreival we don't hit the token size limits. 

text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

len(texts)





# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()

docsearch = FAISS.from_texts(texts, embeddings)



from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

chain = load_qa_chain(OpenAI(), chain_type="stuff")



def llm(prompt):
    query=prompt
    docs = docsearch.similarity_search(query)
    return chain.run(input_documents=docs, question=query)


