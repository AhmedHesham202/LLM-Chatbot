# 🤖 IT Visionary Chatbot (FastAPI + Streamlit)

An interactive, containerized chatbot  
It uses a FastAPI backend to connect with the Groq LLaMA model and a Streamlit frontend to display chat interactions, token usage, and response time.

---

## 🚀 Features

- FastAPI backend with Groq API integration
- Streamlit frontend for the chat interface
- LLM-powered responses (LLaMA 3 via Groq)
- API key management using `.env`
- Fully containerized with Docker Compose
- Displays token usage & latency

---

## 🧰 Tech Stack

- Python 3.10
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [Docker & Docker Compose](https://docs.docker.com/)
- [Groq API](https://console.groq.com/)

---

## 🔧 Setup Instructions

### 1. Clone the Repo

git clone https://github.com/AhmedHesham202/LLM-Chatbot.git

cd LLM-Chatbot

### 2. Add Your API Key

Rename .env.example to .env:

mv .env.example .env

Then edit it and replace with your real key:

GROQ_API_KEY=your_real_api_key_here

### 3. Run the App with Docker
Make sure Docker & Docker Compose are installed.

docker-compose up --build

Open browser at: http://localhost:8000 for Backend
Open browser at: http://localhost:8501 for Frontend

### Features in Action

- Live chat with memory

- Token usage shown after each response

- Execution time measured for performance

- Logs saved to chatbot.log in backend

### Contributing

Contributions, forks, or issues are welcome.
Feel free to open a pull request or suggest features.

### Author
### Ahmed Hesham
Developed for the IT Visionary Assessment 2025
