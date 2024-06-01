import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    raw_text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            raw_text += page.extract_text()
    return raw_text 


def main():
    load_dotenv()
    st.set_page_config(page_title='Chat with PDF', page_icon=':book:')
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Enter your message here:")
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here", type="pdf", accept_multiple_files=True)
        if st.button("Upload"):
            with st.spinner("Processing PDFs..."):
                raw_text  = get_pdf_text(pdf_docs)


if __name__ == '__main__':
    main()