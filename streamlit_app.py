import streamlit as st
from chatbot import process_uploaded_files

st.header('''VartaVault Maestro''')
st.sidebar.header("PDF Chatbot")
st.sidebar.markdown('''
## About
Elevate your document experience with this sleek PDF Chatbot, powered by Python, Spacy, Langchain, and Streamlit. Unleash the synergy of NLP and intuitive design for a seamless interaction journey.''')
pdf = st.sidebar.file_uploader("Upload or drag PDF here", type = "pdf", accept_multiple_files=True)
st.sidebar.button("Upload")

if st.button("Process"):
  user_query = st.text_input("Enter your query:")
  if pdf and user_query:
    result = process_uploaded_files(pdf, user_query)
    st.write('### Results:')
    st.write(result)
