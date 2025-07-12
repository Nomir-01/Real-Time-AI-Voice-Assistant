# Handles recording audio dynamically and transcribing it using Whisper ASR

import whisper
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile
from config import SAMPLE_RATE, SILENCE_THRESHOLD, SILENCE_DURATION, LANGUAGE, WHISPER_MODEL

# Load Whisper model once globally to avoid repeated loading
whisper_model = whisper.load_model(WHISPER_MODEL)

def record_and_transcribe_dynamic(
    threshold=SILENCE_THRESHOLD, silence_duration=SILENCE_DURATION, samplerate=SAMPLE_RATE
):
    """
    Records user speech from mic until silence is detected.
    Then saves to WAV file and transcribes to Urdu using Whisper.
    """
    print("\nSpeak now... (auto-stops after silence)")

    chunk_duration = 0.5  # Seconds per chunk
    chunk_samples = int(samplerate * chunk_duration)
    silence_chunks = int(silence_duration / chunk_duration)

    recording = []
    silent_count = 0

    stream = sd.InputStream(samplerate=samplerate, channels=1, dtype='int16')
    stream.start()

    try:
        while True:
            chunk, _ = stream.read(chunk_samples)
            audio_chunk = chunk.flatten()
            recording.append(audio_chunk)

            volume = np.linalg.norm(audio_chunk)
            silent_count = silent_count + 1 if volume < threshold else 0

            if silent_count >= silence_chunks:
                break
    finally:
        stream.stop()
        stream.close()

    full_audio = np.concatenate(recording)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        scipy.io.wavfile.write(f.name, samplerate, full_audio)
        filename = f.name

    result = whisper_model.transcribe(filename, language=LANGUAGE)
    transcribed_text = result["text"]
    print(f"Urdu Script: {transcribed_text}")
    return transcribed_text
