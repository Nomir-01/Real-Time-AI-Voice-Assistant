# Configuration constants to control app behavior.
# Change values here to adjust settings without touching main code.

"""
Configuration settings for AI Voice Bot.

- SAMPLE_RATE: Audio sample rate for recording and playback (Hz).
- SILENCE_THRESHOLD: Sensitivity for silence detection (lower = more sensitive).
- SILENCE_DURATION: Duration in seconds of continuous silence to auto-stop recording.
- WHISPER_MODEL: Whisper ASR model to use for speech-to-text.
- OLLAMA_MODEL: Ollama model name used for AI generation.
- LANGUAGE: Language code for Whisper transcription.
- LOGGING_ENABLED: Toggle chat logging on/off.
- CHAT_LOG_DIR: Directory path where chat logs are saved.
"""

SAMPLE_RATE = 16000           # Audio sample rate (Hz)
SILENCE_THRESHOLD = 500       # Silence threshold (lower is more sensitive)
SILENCE_DURATION = 1.5        # Duration of silence before stopping (seconds)
WHISPER_MODEL = "small"       # Whisper model to use (e.g., tiny, base, small)
OLLAMA_MODEL = "mistral"      # Ollama AI model to generate Roman Urdu responses
LANGUAGE = "ur"               # Whisper language code (e.g., 'ur' for Urdu)
LOGGING_ENABLED = True        # Toggle logging on/off
CHAT_LOG_DIR = "chats"        # Folder to save chat logs
