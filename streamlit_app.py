import streamlit as st

st.title("PDF Chatbot")
st.sidebar.header("Hi there!")
st.sidebar.file_uploader("Upload or drag PDF here", type = "pdf")
