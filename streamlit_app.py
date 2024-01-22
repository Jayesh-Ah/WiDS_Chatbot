import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.header('''VartaVault Maestro''')

st.sidebar.header("PDF Chatbot")
st.sidebar.markdown('''
## About
Elevate your document experience with this sleek PDF Chatbot, powered by Python, Spacy, Langchain, and Streamlit. Unleash the synergy of NLP and intuitive design for a seamless interaction journey.''')

st.sidebar.add_vertical_space(3)
st.sidebar.file_uploader("Upload or drag PDF here", type = "pdf")
st.sidebar.button("Upload")

  
