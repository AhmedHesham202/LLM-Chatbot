from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)

# Define FastAPI app
app = FastAPI()

# Request schema
class Message(BaseModel):
    user_input: str

@app.post("/chat")
async def chat_with_bot(message: Message):
    logging.info(f"Received user input: {message.user_input}")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.user_input}
        ],
        "model": "llama3-8b-8192"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload
            )
            response.raise_for_status()
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
            token_usage = data.get("usage", {}).get("total_tokens", "N/A")

        logging.info(f"Bot reply: {reply}")
        return {
            "user_input": message.user_input,
            "bot_reply": reply,
            "token_usage": token_usage
        }

    except Exception as e:
        logging.error(f"❌ Error: {e}")
        return {
            "error": "Something went wrong.",
            "details": str(e)
        }
