import streamlit as st
#import spacy as sp
import fitz
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
nlp = spacy.load("en_core_web_md")

def main():

  #STREAMLIT APP
  st.header('''VartaVault Maestro''')
  st.sidebar.header("PDF Chatbot")
  st.sidebar.markdown('''
  ## About
  Elevate your document experience with this sleek PDF Chatbot, powered by Python, Spacy, Langchain, and Streamlit. Unleash the synergy of NLP and intuitive design for a seamless interaction journey.''')
  pdf = st.sidebar.file_uploader("Upload or drag PDF here", type = "pdf", accept_multiple_files=True)
  st.sidebar.button("Upload")

  #EXTRACTING TEXT
  def extract(doc):
    file = fitz.open(doc)
    words = ""
    for page_num in range(file.page_count):
      page = doc[page_num]
      words += page.get_text()
    doc.close()
    return words
  

if __name__ == '__main__':
  main()
  
