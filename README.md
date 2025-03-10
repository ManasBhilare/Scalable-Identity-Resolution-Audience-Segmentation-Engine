# **Identity Resolution System using Faiss, SingleStoreDB, and FastAPI** 🚀

This project implements a **full identity resolution system** using **Faiss (vector search), SingleStoreDB (high-performance database), and FastAPI (real-time API)**.

## **📌 Features**
✅ **Data Cleaning & Standardization** using Pandas  
✅ **Generate User Embeddings** using Sentence Transformers  
✅ **Fast Similarity Matching** with Faiss  
✅ **Store User Segments** in SingleStoreDB  
✅ **Expose Real-Time API** with FastAPI  
✅ **Retrieve Matched Identities via API**  

---

## **📁 Project Structure**
| File | Description |
|------|------------|
| `data_standardization.py` | Cleans raw customer data (emails, IPs) |
| `faiss_indexing.py` | Generates vector embeddings & stores them in Faiss |
| `query_faiss.py` | Queries Faiss for similar users |
| `fastapi_server.py` | Runs FastAPI service for identity resolution |
| `synthetic_customer_data.csv` | Sample dataset with customer records |
| `cleaned_data.csv` | Processed data after standardization |
| `customer_embeddings.index` | Faiss index storing embeddings |

---

## **📌 Setup & Installation**

### **1️⃣ Install Dependencies**
Ensure you have Python 3.8+ and install required libraries:
```sh
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:
```sh
pip install fastapi uvicorn pandas numpy faiss-cpu sentence-transformers singlestoredb pymysql
```

### **2️⃣ Start SingleStoreDB (Using Docker)**
```sh
docker pull singlestore/cluster-in-a-box
docker run -d --name singlestore -p 3306:3306 -e LICENSE_KEY=YOUR_LICENSE_KEY singlestore/cluster-in-a-box
```

### **3️⃣ Create Database & Table in SingleStoreDB**
```sh
mysql -h 127.0.0.1 -P 3306 -u root --password
```
Then, inside MySQL:
```sql
CREATE DATABASE audience_db;
USE audience_db;

CREATE TABLE audience_segments (
    user_id INT PRIMARY KEY,
    email VARCHAR(255),
    segment VARCHAR(255)
);
```

### **4️⃣ Run Data Processing & Faiss Indexing**
```sh
python data_standardization.py
python faiss_indexing.py
```

### **5️⃣ Start FastAPI Server**
```sh
python fastapi_server.py
```
✅ **Server should be running at:** `http://127.0.0.1:8000/`

---

## **📌 API Endpoints & Usage**

### **1️⃣ Check API Status**
```sh
curl http://127.0.0.1:8000/
```
**Response:**  
```json
{"message": "Identity Resolution API is running with SingleStoreDB!"}
```

### **2️⃣ Get Similar Users (Identity Resolution)**
```sh
curl "http://127.0.0.1:8000/get_similar_users/?email=johndoe@example.com&ip_address=192.168.1.1&k=5"
```
**Response:**  
```json
{
  "query": {"email": "johndoe@example.com", "ip_address": "192.168.1.1"},
  "similar_users": [
    {"user_id": 9914, "email": "john910@gmail.com", "ip_address": "66.86.173.192"},
    {"user_id": 183, "email": "john700@gmail.com", "ip_address": "192.157.184.56"}
  ]
}
```

### **3️⃣ Retrieve Stored Audience Segments**
```sh
curl "http://127.0.0.1:8000/get_segment/9914"
```
**Response:**  
```json
{"user_id": "9914", "segment": "Similar Users"}
```

---

## **📌 Deployment**

### **1️⃣ Deploy Locally with Gunicorn**
```sh
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker fastapi_server:app --bind 0.0.0.0:8000
```

### **2️⃣ Deploy to Cloud (AWS/GCP/Azure)**
- Use **AWS EC2** with a running FastAPI instance
- Deploy as a **serverless function on Google Cloud Run**  
- Use **Render or Railway** for free-tier hosting

---

## **📌 Future Improvements**
🔹 **Scale Faiss for millions of records**  
🔹 **Optimize API for faster lookups**  
🔹 **Deploy to a production cloud server**  
🔹 **Implement user deduplication with LLM-based embeddings**  

---

## **📌 Contributors**
**👤 Manas Bhilare**  
Built for **identity resolution & real-time audience segmentation** 🚀

---

## **📌 License**
This project is **open-source** under the MIT License.

---

