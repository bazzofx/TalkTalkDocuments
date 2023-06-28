import streamlit as st






def main():
    st.set_page_config(page_title="Chat with your PDFs ", page_icon="🙄")
    
    st.header("Chat with your files")
    st.text_input("Ask a question about your documents.")
    
    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload your documnets here")
        st.button("Process")

if __name__ == ('__main__'):
    main()