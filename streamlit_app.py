import streamlit as st

st.header('''VartaVault Maestro''')

st.sidebar.header("PDF Chatbot")
st.sidebar.markdown('''
## About
Elevate your document experience with this sleek PDF Chatbot, powered by Python, Spacy, Langchain, and Streamlit. Unleash the synergy of NLP and intuitive design for a seamless interaction journey.''')

st.sidebar.subheader.file_uploader("Upload or drag PDF here", type = "pdf")
st.sidebar.button("Upload")

  
