import streamlit as st
import requests
import time

st.set_page_config(page_title="Chatty", layout="centered")
st.title("🧠 Chatty - LLM Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input field
user_input = st.text_input("You:", key="input")

# Send button
if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Measure response time
    start = time.time()
    try:
        response = requests.post(
            "http://backend:8000/chat",
            json={"user_input": user_input}
        )
        response.raise_for_status()
        data = response.json()
        bot_reply = data.get("bot_reply", "❌ No response")
        token_usage = data.get("token_usage", "N/A")

    except Exception as e:
        bot_reply = f"❌ Error: {e}"
        token_usage = "N/A"

    end = time.time()

    st.session_state.messages.append({"role": "bot", "content": bot_reply})
    st.markdown(f"🧮 **Token Usage:** {token_usage}")
    st.markdown(f"⏱️ **Response Time:** {round(end - start, 2)}s")

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"👤 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **Bot:** {msg['content']}")
