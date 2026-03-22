from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Medical + protocol data
documents = [
    "Patient has chest pain and sweating",
    "Shortness of breath and dizziness",
    "Unconscious patient no pulse",
    "History of diabetes and hypertension",
    "Severe bleeding from injury",
    "High fever and dehydration",
    "Dental surgery in 2010",
    "Protocol: Administer aspirin immediately",
    "Protocol: Start CPR immediately",
    "Protocol: Provide oxygen support"
]

# Convert to vectors
embeddings = model.encode(documents)

# Create FAISS index
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

# Search function
def search(query, k=5):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)
    return [documents[i] for i in indices[0]]