from fastapi import FastAPI
import singlestoredb as s2
import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

app = FastAPI()

# ✅ Connect to SingleStoreDB
conn = s2.connect(host="127.0.0.1", port=3306, user="root", password="SinglestoreDB", database="audience_db")

# Load customer dataset
df = pd.read_csv("cleaned_data.csv")

# Load Faiss index
index = faiss.read_index("customer_embeddings.index")

# Load SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.get("/")
def home():
    return {"message": "Identity Resolution API is running with SingleStoreDB!"}

# ✅ Identity Resolution Endpoint
@app.get("/get_similar_users/")
def get_similar_users(email: str, ip_address: str, k: int = 5):
    query_text = email + " " + ip_address
    query_embedding = model.encode([query_text])
    distances, indices = index.search(np.array(query_embedding), k)
    similar_users = df.iloc[indices[0]].to_dict(orient="records")

    # ✅ Store resolved identities in SingleStoreDB
    cursor = conn.cursor()
    for user in similar_users:
        cursor.execute(
            "INSERT INTO audience_segments (user_id, email, segment) VALUES (%s, %s, %s) "
            "ON DUPLICATE KEY UPDATE segment=VALUES(segment)",
            (user["user_id"], user["email"], "Similar Users"),
        )
    conn.commit()

    return {"query": {"email": email, "ip_address": ip_address}, "similar_users": similar_users}

# ✅ Start FastAPI Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
