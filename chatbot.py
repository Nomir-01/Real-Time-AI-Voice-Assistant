# Sends user input (Roman Urdu) to Ollama AI model to generate AI response
# Uses streaming to collect full reply text

import requests
import json
from config import OLLAMA_MODEL

def generate_ai_reply(user_input):
    """
    Prompts Ollama model to reply politely in Roman Urdu to the user's input.
    Returns AI-generated reply as string.
    On failure, returns a polite error message.
    """
    prompt = (
        f"You are a friendly AI assistant that speaks Roman Urdu. "
        f"User said: '{user_input}'. Respond politely in Roman Urdu only."
    )
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": True},
            stream=True
        )
        reply = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                reply += data.get("response", "")
        print(f"AI: {reply.strip()}")
        return reply.strip()
    except Exception:
        return "Sorry, AI service is not available right now."
