import streamlit as st
from chatbot import process_uploaded_files

st.header('''VartaVault Maestro :star:''')
st.sidebar.header("PDF Chatbot :brain:")
st.sidebar.markdown('''
## About
Elevate your document experience with this sleek PDF Chatbot, powered by Python, Spacy, Langchain, and Streamlit.:rocket:''')
pdf = st.sidebar.file_uploader("Upload or drag PDF here :point_down:", type = "pdf", accept_multiple_files=True)
st.sidebar.button("Upload")

@st.cache
def process_and_cache_results(pdf, user_query):
    return process_uploaded_files(pdf, user_query)

if st.button("Start"):  
  user_query = st.text_input("Enter your query:", key="user_query_input")
  if st.button("Process"):
    st.write(user_query)
    st.write(f"Debug: User Query - {user_query}")
    if pdf and user_query:
      result = process_and_cache_results(pdf, user_query)
      if result:
        st.write('### Results:')
        st.write(result)
      else:
        st.write('No results found.')

