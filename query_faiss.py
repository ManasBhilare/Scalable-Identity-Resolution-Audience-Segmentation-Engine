import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

# Load the cleaned data
df = pd.read_csv("cleaned_data.csv")

# Load the Faiss index
index = faiss.read_index("customer_embeddings.index")

# Load the same model used for encoding
model = SentenceTransformer('all-MiniLM-L6-v2')

# Select a sample user (first row in dataset)
query_text = df.iloc[0]["email"] + " " + df.iloc[0]["ip_address"]
query_embedding = model.encode([query_text])

# Search for similar users
distances, indices = index.search(np.array(query_embedding), k=5)

# Retrieve matching user records
similar_users = df.iloc[indices[0]]

print("\n🔍 Similar Users Found:\n", similar_users)
