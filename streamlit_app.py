import streamlit as st
import spacy
nlp = spacy.load("en_core_web_md")
@st.cache(allow_output_mutation=True)

def main():
  st.header("PDF Chatbot")

st.sidebar.header("Hi there!")
st.sidebar.file_uploader("Upload or drag PDF here", type = "pdf")
