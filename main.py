import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from htmlTemplates import css, bot_template, user_template

#HTML STYLE HERE


repoId = "google/flan-t5-xxl"
#repoId = "abhiramtirumala/DialoGPT-sarcastic"

def get_pdf_text(pdf_docs): #extract pdf pages from all .pdfs
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return text

def get_text_chunks(text): #create chunks from raw pdf pages
    text_spliter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_spliter.split_text(text)
    return chunks

    
def get_vectorstore(text_chunks): #make the embeddings from the chunks
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore    

def get_conversation_chain(vectorstore):
    #llm = ChatOpenAI()
    llm = HuggingFaceHub(repo_id=repoId, model_kwargs={"temperature":0.4, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
    
def handle_userinput(user_question):
    response = st.session_state.conversation({'question':user_question})
    st.session_state.chat_history = response['chat_history']
    
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content),unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content),unsafe_allow_html=True)
    
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with your PDFs ", page_icon="🔐")
    st.write(css,unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.image("cs-white.png", width=400)    
    st.header("Chit-Chat with your files 📁")
    user_question = st.text_input("Ask a question about your documents.")
    if user_question:
        handle_userinput(user_question)
       
    
    st.write(user_template.replace("{{MSG}}","Hello robot"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}","Hello there, upload your file on the left and ask me a question, if you dare.."), unsafe_allow_html=True)
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your documnets here", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                #get pdf text
                raw_text = get_pdf_text(pdf_docs)
                
                #get pdf chunks
                text_chunks = get_text_chunks(raw_text)
                #create vector store
                vectorstore = get_vectorstore(text_chunks)
                
                st.session_state.conversation = get_conversation_chain(vectorstore)

if __name__ == ('__main__'):
    main()