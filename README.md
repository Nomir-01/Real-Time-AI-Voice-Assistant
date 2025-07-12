# Real-Time AI Voice Assistant (Roman Urdu Assistant)

This is a simple voice-driven AI assistant that listens to spoken Urdu, transcribes it, converts it to Roman Urdu, generates intelligent replies using a local AI model (Ollama), and speaks the response out loud. All operations run locally for privacy and customization.

---

## Features

- Dynamic voice recording with auto-stop after silence
- Converts spoken Urdu to Roman Urdu using AI
- Generates replies using an LLM (e.g., Mistral via Ollama)
- Speaks the reply using text-to-speech
- Logs each interaction with timestamp
- Random greeting system at startup
- Easy configuration and customization
- Works offline after initial setup

---

## Requirements

- Python 3.8 or newer
- [Ollama](https://ollama.com/) installed and running locally
- Whisper model downloaded (e.g., `small`)
- Working microphone and speaker

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-voice-bot.git
cd ai-voice-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Ollama Model

Ensure Ollama is running and the desired model is available (e.g., `mistral`).

```bash
ollama run mistral
```

Check that the model name in `config.py` matches.

### 4. Run the Bot

```bash
python main.py
```

Speak your query in Urdu. The bot will process, respond in Roman Urdu, and speak the response.

Say `"khatam"` or `"ختم"` to exit.

---

## Configuration

All customizable settings are stored in `config.py`.

```python
SAMPLE_RATE = 16000             # Microphone sample rate
SILENCE_THRESHOLD = 500         # Volume threshold for detecting silence
SILENCE_DURATION = 1.5          # Seconds of silence before auto-stop
WHISPER_MODEL = "small"         # Whisper model name
OLLAMA_MODEL = "mistral"        # Ollama model name
LANGUAGE = "ur"                 # Whisper language code for Urdu
LOGGING_ENABLED = True          # Enable/disable chat logging
CHAT_LOG_DIR = "chats"          # Directory to save logs
```

To edit greeting messages, modify `greetings_list.py`.

---

## Project Structure

```
ai-voice-bot/
├── main.py                # Main runner file
├── chatbot.py             # Roman Urdu AI reply handler
├── recorder.py            # Audio recording and Whisper transcription
├── romanizer.py           # Urdu to Roman Urdu conversion via Ollama
├── speaker.py             # Text-to-speech handler
├── greetings_list.py      # Editable list of startup greetings
├── config.py              # App settings and constants
├── logger.py              # Chat logger with timestamps
├── requirements.txt       # Python dependency list
└── chats/                 # Folder containing timestamped logs
```

---

## Example Log (in `chats/`)

```
=== AI Voice Chat Log ===
Timestamped entries of user and AI conversation
------------------------------------------------------------

[2025-07-12 17:32:00] AI Greeting: Salam! Main aap ki madad ke liye yahan hoon.
------------------------------------------------------------
[2025-07-12 17:32:05] User (Roman Urdu): kia haal hai?
[2025-07-12 17:32:10] User (Urdu): کیا حال ہے؟
[2025-07-12 17:32:20] AI Reply: sab theek hai, shukriya.
------------------------------------------------------------
```

---

## Dependencies

Listed in `requirements.txt`:

```
numpy
sounddevice
scipy
whisper
requests
pyttsx3
```
