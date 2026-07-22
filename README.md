# Real-Time AI Voice Assistant

A local voice assistant designed for spoken Urdu and Roman Urdu conversations. It records speech, transcribes Urdu audio with Whisper, converts text to Roman Urdu, generates a response with an Ollama-hosted language model, and reads the reply aloud.

## Features

- Silence-aware microphone recording
- Urdu speech recognition with Whisper
- Urdu-to-Roman-Urdu conversion
- Local response generation through Ollama
- Text-to-speech playback
- Configurable greetings and runtime settings
- Optional timestamped conversation logs

## Processing flow

```text
Microphone → Whisper transcription → Roman Urdu conversion
           → Ollama response → text-to-speech → speaker
```

## Requirements

- Python 3.8 or newer
- A microphone and audio output device
- [Ollama](https://ollama.com/) installed and running locally
- An Ollama model matching `OLLAMA_MODEL` in `config.py`

## Setup

```bash
git clone https://github.com/Nomir-01/Real-Time-AI-Voice-Assistant.git
cd Real-Time-AI-Voice-Assistant
python -m venv .venv
python -m pip install -r requirements.txt
ollama pull mistral
python main.py
```

The default configuration uses the Whisper `small` model and Ollama's `mistral` model. Initial model downloads require internet access; inference is local afterward.

## Configuration

Runtime settings are defined in `config.py`:

- recording sample rate and silence detection
- Whisper model and language
- Ollama model
- chat logging toggle and log directory

Startup greetings can be edited in `greetings_list.py`.

## Project structure

```text
main.py             Application loop
recorder.py         Audio capture and Whisper transcription
romanizer.py        Urdu-to-Roman-Urdu conversion
chatbot.py          Local LLM response generation
speaker.py          Text-to-speech output
logger.py           Timestamped conversation logging
config.py           Runtime configuration
greetings_list.py   Startup greeting messages
```

## Privacy

Speech processing and response generation run locally. When logging is enabled, conversations are written to the local `chats/` directory; disable logging in `config.py` when transcripts should not be retained.

## Troubleshooting

- Confirm Ollama is running and the configured model is installed.
- Verify the operating system can access the selected microphone.
- Adjust `SILENCE_THRESHOLD` if recording stops too early or does not stop.
- Audio packages may require platform-specific system drivers or build tools.
