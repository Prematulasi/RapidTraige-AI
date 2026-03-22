# 🚑 RapidTriage-AI

## 🧠 Real-Time AI-Powered Emergency Triage Assistant

RapidTriage-AI is an intelligent triage system designed for **emergency rooms and disaster response scenarios**, where every second matters. It analyzes unstructured patient symptoms and medical context to recommend the **next best action instantly**.

---

## 🚨 Problem Statement

In critical environments like hospitals and disaster zones, medical staff often deal with:

* Large, unstructured patient records
* Time-sensitive decision making
* Information overload

This leads to **delays in diagnosis and treatment**, which can cost lives.

---

## 💡 Solution

RapidTriage-AI provides:

✔ Instant symptom analysis
✔ Intelligent context pruning (removes irrelevant data)
✔ Priority-based triage (HIGH / MEDIUM / LOW)
✔ Real-time recommendations

All within **sub-500ms response time** ⚡

---

## 🛠️ Tech Stack

### Frontend

* React.js
* CSS (Custom UI Styling)
* Axios

### Backend

* FastAPI
* Python

### AI / ML

* Sentence Transformers
* FAISS (Vector Search)
* Intelligent Context Pruning

---

## ⚙️ Features

### 🎤 Voice & Text Input

* Accepts both typed and voice-based symptoms

### 🧠 Intelligent Context Pruning

* Filters irrelevant patient history
* Focuses only on current critical symptoms

### 🚨 Priority Classification

* 🔴 HIGH → Immediate emergency care
* 🟠 MEDIUM → Urgent medical attention
* 🟢 LOW → Basic care

### 📊 Real-Time Dashboard

* Displays patient data dynamically
* Risk score visualization

### ⚡ Ultra Low Latency

* Optimized for **< 500ms response time**

---

## 🧪 Sample Inputs

```text
Chest pain, sweating, shortness of breath → HIGH
Fever, cough, mild breathing difficulty → MEDIUM
Headache, mild cold → LOW
```

---

## 🏗️ Project Structure

```
RapidTriage-AI/
│
├── backend/
│   ├── main.py
│   ├── vector_store.py
│   ├── model.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│
└── README.md
```

---

## 🚀 How to Run Locally

### 🔹 Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 🔹 Frontend

```bash
cd frontend
npm install
npm start
```

---

## 🌍 Future Scope

* Integration with hospital databases
* Live patient monitoring
* AI-based predictive diagnosis
* Multilingual voice support

---

## 🏆 Hackathon Impact

RapidTriage-AI can:

✔ Reduce diagnosis time
✔ Assist doctors in critical decisions
✔ Improve patient survival rates
✔ Handle disaster-scale data efficiently

---


## 📌 Conclusion

RapidTriage-AI is not just a project — it is a **real-world life-saving solution** designed to bring AI into emergency healthcare systems.

---
