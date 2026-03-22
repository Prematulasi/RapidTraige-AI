import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";


function App() {
  const [patientId, setPatientId] = useState("");
  const [query, setQuery] = useState("");
  const [data, setData] = useState([]);

  
    const API = "http://127.0.0.1:8000";

const submit = async () => {
  try {
    await axios.post(`${API}/triage`, {
      patient_id: patientId,
      query: query
    });
    load();
  } catch (err) {
    console.error(err);
    alert("Backend not connected!");
  }
};

  const load = async () => {
  try {
    const res = await axios.get(`${API}/dashboard`);
    setData(res.data);
  } catch (err) {
    console.error(err);
  }
};

  useEffect(() => {
  const interval = setInterval(() => {
    load();
  }, 2000);

  return () => clearInterval(interval);
}, []);

  // 🎤 Voice input
 const startListening = () => {
  const recognition = new window.webkitSpeechRecognition();
  recognition.lang = "en-US";

  recognition.onresult = (event) => {
    const speech = event.results[0][0].transcript;
    setQuery(speech);
  };

  recognition.start();
};

  return (
    <div className="container">
      <h1>🚑 RapidTriage AI</h1>

      <div className="inputBox">
        <input
          placeholder="Patient ID"
          onChange={(e) => setPatientId(e.target.value)}
        />

        <input
          placeholder="Enter symptoms..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />

       <button onClick={startListening}>🎤</button>
        <button onClick={submit}>Analyze</button>
      </div>

      <h2>Live Triage Dashboard</h2>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Symptoms</th>
            <th>Priority</th>
            <th>Action</th>
            <th>Latency</th>
          </tr>
        </thead>

        <tbody>
          {data.map((p, i) => (
            <tr key={i}>
              <td>{p.patient_id}</td>
              <td>{p.query}</td>
              <td>{p.priority}</td>
              <td>{p.action}</td>
              <td>{p.latency_ms} ms</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App