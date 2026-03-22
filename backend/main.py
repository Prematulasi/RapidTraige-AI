from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from vector_store import search
from pruning import advanced_pruning
from risk_engine import calculate_risk, get_priority
from decision_engine import generate_action
import time

app = FastAPI()

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request body model
class Patient(BaseModel):
    patient_id: str
    query: str

patients_db = []

@app.post("/triage")
def triage(patient: Patient):
    start = time.time()

    patient_id = patient.patient_id
    query = patient.query

    results = search(query)
    pruned = advanced_pruning(results, query)

    risk = calculate_risk(query)
    priority = get_priority(risk)

    action = generate_action(query)

    latency = round((time.time() - start) * 1000, 2)

    data = {
        "patient_id": patient_id,
        "query": query,
        "priority": priority,
        "risk_score": risk,
        "action": action,
        "latency_ms": latency,
        "context": pruned
    }

    patients_db.append(data)

    return data


@app.get("/dashboard")
def dashboard():
    return sorted(patients_db, key=lambda x: x["risk_score"], reverse=True)


@app.get("/")
def home():
    return {"message": "Backend Running"}