# Text-to-speech module using pyttsx3 for offline voice synthesis

import pyttsx3

def init_speaker():
    """
    Initializes the pyttsx3 engine with preferred speech rate.
    Returns the engine instance.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    return engine

def speak(engine, text):
    """
    Speaks the given text aloud using the initialized engine.
    """
    engine.say(text)
    engine.runAndWait()
