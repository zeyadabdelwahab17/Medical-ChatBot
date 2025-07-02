# 🩺 AI Medical Chatbot (Powered by Mistral-instruct via Ollama)

A local, privacy-friendly medical chatbot that uses the `mistral:instruct` model via [Ollama](https://ollama.com). Built with Streamlit and Python, this assistant responds to general medical questions with empathy, clarity, and safety-first reasoning — **without diagnosing**.

---

## 🚀 Features

- Local LLM: Runs fully offline using Ollama + Mistral
- Empathetic responses using a structured thinking process
- Classifies emergencies using keywords
- Identifies likely medical specialties
- Provides safety disclaimers and real health source references
- Live logging: See API call status and timing in terminal

---

## 🧠 Response Thinking Framework

1. Classify if it's an emergency (e.g., chest pain, unconscious)
2. Express empathy
3. Suggest the relevant medical specialty
4. Suggest safe possible causes (not diagnoses)
5. Provide prevention or home-care tips
6. Flag emergency symptoms clearly
7. Recommend seeing a doctor or hospital
8. Cite sources like WHO, NIH, or CDC

---

## 🖥️ Prerequisites

- Python 3.8+
- [Ollama installed](https://ollama.com/download)
- `streamlit` and `requests` libraries

Install Python packages:
```bash
pip install streamlit requests
```

🧠 Step 1: Set Up Ollama & Download Mistral
Make sure Ollama is installed, then run:

```bash
ollama pull mistral:instruct
```

▶️ Step 2: Run the Chatbot (CMD)
💬 Option A: Run in Command Line (Text-based)
```bash
python medical_chatbot.py
```
🖼️ Option B: Run with Streamlit (Web UI)
```bash
streamlit run medical_chatbot.py
```
You’ll see the chatbot at:
```arduino
http://localhost:8501
```
🔍 Step 3: Track API Logs in Terminal
In your terminal, you will see:

``yaml
 Sent to Ollama API:
<full formatted prompt>

API Status: 200
Response Time: 0.87 sec
```
If there's a failure:

```yaml
❌ Network Error: [details...]
OR
✅ API Status: 500
❌ Response Body: {"error": "model not loaded"}
```
These logs help you debug and verify model behavior.

📌 Notes
No diagnosis is ever made — only suggestions and education

You must manually start Ollama:

```bash
ollama run mistral:instruct
```
Streamlit UI works only if Ollama is running

🔐 Local Privacy
All processing is done locally

No data is sent to the cloud

Ideal for secure or offline environments




