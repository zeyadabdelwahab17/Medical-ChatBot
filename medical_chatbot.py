import streamlit as st
import requests
import time


EMERGENCY_KEYWORDS = [
    "chest pain", "can't breathe", "severe pain", 
    "unconscious", "heavy bleeding", "stroke symptoms"
]

medical_fields = [
    "Anesthesiology", "Cardiology", "Dermatology", "Emergency Medicine",
    "Family Medicine", "Internal Medicine", "Neurology", "Obstetrics & Gynecology",
    "Oncology", "Ophthalmology", "Orthopedics", "Pathology", "Pediatrics",
    "Psychiatry", "Radiology", "Surgery"
]

SYSTEM_PROMPT = f"""
You are an AI medical assistant with expertise in general health and the following specialties:
{', '.join(medical_fields)}

Your job is to respond to patient questions carefully, using the following reasoning steps:

---

**Reasoning Steps**:
1. Classify if the issue is an emergency (based on keywords: {', '.join(EMERGENCY_KEYWORDS)})
2. Express sympathy and calm the user
3. Identify the most likely medical specialty that handles this issue
4. Suggest safe and possible causes (not diagnoses)
5. Provide basic home care or prevention tips (if safe)
6. Clearly flag any "red flag" symptoms that require immediate care
7. Advise seeing a licensed doctor or going to the hospital if the situation may be serious
8. Cite credible sources like NIH, WHO, or CDC

---

**Rules**:
- NEVER diagnose
- Use simple language (8th grade reading level)
- Always err on the side of caution
- Be empathetic, calm, and supportive

---

**Response Format**:
Start with sympathy, then explanation, then possible causes and tips, and finally end with a safety notice:
"For urgent concerns, please visit the nearest hospital."
"""

def format_messages(messages):
    prompt = SYSTEM_PROMPT + "\n\n"
    for msg in messages:
        role = msg["role"]
        content = msg["content"]
        if role == "user":
            prompt += f"Patient: {content}\n"
        elif role == "assistant":
            prompt += f"Assistant: {content}\n"
    prompt += "Assistant: "
    return prompt


import time

def get_response(messages, model="mistral:instruct"):
    prompt = format_messages(messages)
    print("\n📤 Sent to Ollama API:")
    print(prompt)

    try:
        start = time.time()

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False}
        )

        end = time.time()

        print(f"\n✅ API Status: {response.status_code}")
        print(f"⏱️ Response Time: {round(end - start, 2)} sec")

        if response.status_code != 200:
            print(f"❌ Response Body: {response.text}")
            return "⚠️ Error: The model returned a non-200 response."

        return response.json()["response"].strip()

    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: {e}")
        return "⚠️ Error: Could not connect to the model."



st.set_page_config(page_title="🩺 Medical Assistant", layout="centered")
st.title("🩺 Medical Chatbot")
st.markdown("Ask a general medical question. This AI follows a safe reasoning framework.")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Enter your medical concern:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    bot_reply = get_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

for msg in st.session_state.messages:
    speaker = "👤 You" if msg["role"] == "user" else "🤖 Assistant"
    st.markdown(f"**{speaker}:** {msg['content']}")
