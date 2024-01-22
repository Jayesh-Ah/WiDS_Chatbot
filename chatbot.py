import numpy as np
import scikit-learn as sklearn
#import fitz
#from spacy.lang.en import English
import spacy
from sklearn.metrics.pairwise import cosine_similarity
nlp = spacy.load("en_core_web_sm")

def group_text(text):
    doc = nlp(text)
    groups = [sent.text for sent in doc.sents]
    return groups

def generate_embeddings(groups):
    group_embeddings = []
    for group in groups:
        group_embeddings.append(np.mean([token.vector for token in nlp(group)], axis=0))
    return np.array(group_embeddings)

def retrieve_groups(query_embedding, embeddings_database, groups_database, top_k=3):
    similarities = cosine_similarity([query_embedding], embeddings_database)[0]
    indexes = np.argsort(similarities)[::-1][:top_k]
    similar_groups = [groups_database[i] for i in indexes]
    return similar_groups

def process_uploaded_files(uploaded_files, user_query):
    groups_database = []
    embeddings_database = []

    for file in uploaded_files:
        pdf_text = file.read().decode("utf-8")
        pdf_groups = group_text(pdf_text)
        groups_database.extend(pdf_groups)
        embeddings_database.extend(generate_embeddings(pdf_groups))

    embeddings_database = np.array(embeddings_database)

    query_groups = group_text(user_query)
    query_embedding = generate_embeddings(query_groups)[0]

    similar_groups = retrieve_groups(query_embedding, embeddings_database, groups_database)

    return similar_groups

