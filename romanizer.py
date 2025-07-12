# Sends Urdu text to Ollama API to convert it into Roman Urdu script
# Handles streaming response to build output dynamically

import requests
import json
from config import OLLAMA_MODEL

def convert_to_roman_urdu(urdu_text):
    """
    Uses Ollama local API to convert Urdu script to Roman Urdu.
    Sends a prompt instructing the model to transliterate only.
    Returns Roman Urdu string or empty if error occurs.
    """
    prompt = f"Convert this Urdu sentence to Roman Urdu (Latin alphabet only): '{urdu_text}'"
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": True},
            stream=True
        )
        roman = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                roman += data.get("response", "")
        print(f"Roman Urdu: {roman.strip()}")
        return roman.strip()
    except Exception:
        print("Error: Ollama not running.")
        return ""
