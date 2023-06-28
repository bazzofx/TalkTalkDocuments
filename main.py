import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return text

def get_text_chunk(text):
    text_spliter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_spliter.split_text(text)
    return chunks

def main():
    st.set_page_config(page_title="Chat with your PDFs ", page_icon="🙄")
    
    st.header("Chat with your files")
    st.text_input("Ask a question about your documents.")
    
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your documnets here", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                #get pdf text
                raw_text = get_pdf_text(pdf_docs)
                
                #get pdf chunks
                text_chunks = get_text_chunk(raw_text)
                st.write(text_chunks)
                #create vector store

if __name__ == ('__main__'):
    main()