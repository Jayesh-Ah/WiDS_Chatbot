import streamlit as st

st.sidebar.header("PDF Chatbot")
st.sidebar.markdown('''
## About
Elevate your document experience with this sleek PDF Chatbot, powered by Python, Spacy, Langchain, and Streamlit. Unleash the synergy of NLP and intuitive design for a seamless interaction journey.''')
st.sidebar.file_uploader("Upload or drag PDF here", type = "pdf")

st.header('''## VartaVault Maestro''')
  
