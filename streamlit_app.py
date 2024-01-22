import streamlit as st

st.sidebar.header("##VartaVault Maestro")
st.sidebar.file_uploader("Upload or drag PDF here", type = "pdf")
st.sidebar.markdown('''
##About
Elevate your document experience with this sleek PDF Chatbot, powered by Python, Spacy, Langchain, and Streamlit. Unleash the synergy of NLP and intuitive design for a seamless interaction journey.''')

st.header("PDF Chatbot")
  
