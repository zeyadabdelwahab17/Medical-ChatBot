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

bash
Copy
Edit
ollama pull mistral:instruct
▶️ Step 2: Run the Chatbot (CMD)
💬 Option A: Run in Command Line (Text-based)
bash
Copy
Edit
python medical_chatbot.py
🖼️ Option B: Run with Streamlit (Web UI)
bash
Copy
Edit
streamlit run medical_chatbot.py
You’ll see the chatbot at:

arduino
Copy
Edit
http://localhost:8501
