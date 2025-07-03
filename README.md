# 🤖 IT Visionary Chatbot (FastAPI + Streamlit)

An interactive LLM-powered chatbot built for the IT Visionary Assessment.  
Powered by Groq API and containerized using Docker Compose.

---

## 🚀 Features

- FastAPI backend with Groq LLaMA model integration
- Streamlit frontend with chat UI, token usage, and response time
- Error logging and session-based chat history
- Fully dockerized and portable

---

## 📦 Project Structure

ITVisionaryChatbot/
├── backend/ # FastAPI service
├── frontend/ # Streamlit UI
├── docker-compose.yml
├── .env.example # Example of env vars
└── README.md


## 🔧 Setup Instructions

### 1. Clone the Repo


git clone https://github.com/YOUR_USERNAME/ITVisionaryChatbot.git
cd ITVisionaryChatbot

2. Add Your API Key
Rename .env.example to .env:

cp .env.example .env

Then edit it and replace with your real key:

GROQ_API_KEY=your_real_api_key_here

3. Run the App
docker-compose up --build

Open browser at: http://localhost:8501

8501

Contributing
Feel free to fork, clone, and suggest improvements!

