from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd

df = pd.read_csv("synthetic_customer_data.csv")

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df["email"].astype(str) + " " + df["ip_address"].astype(str))

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, "customer_embeddings.index")
