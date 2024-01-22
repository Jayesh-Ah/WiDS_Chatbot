import streamlit as st
import spacy
#nlp = spacy.load("en_core_web_md")

with st.sidebar:  
  st.header("Hi there!")
  st.file_uploader("Upload or drag PDF here", type = "pdf")

def main():
  st.header("PDF Chatbot")
  
if __name__ =='__main__':
  main()
