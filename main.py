# Entry point to run AI voice chat bot

import random
from greetings_list import GREETINGS
from recorder import record_and_transcribe_dynamic
from romanizer import convert_to_roman_urdu
from chatbot import generate_ai_reply
from speaker import speak, init_speaker
from logger import log_chat, start_new_log, close_log, log_heading, log_greeting
from config import LOGGING_ENABLED

def get_random_greeting():
    """
    Picks a random greeting from the greetings list.
    """
    return random.choice(GREETINGS)

def run_chat():
    """
    Runs the main voice chat loop:
    - Greets user
    - Records input dynamically
    - Converts to Roman Urdu
    - Sends to AI and speaks response
    - Logs entire conversation
    - Stops if user says 'khatam' or 'ختم'
    """
    if LOGGING_ENABLED:
        start_new_log()
        log_heading()

    engine = init_speaker()
    print("AI Voice Bot Started — Say 'khatam' or 'ختم' to exit.\n")

    # Say greeting only (not sent to AI)
    greeting = get_random_greeting()
    print(f"Bot Greeting: {greeting}")
    speak(engine, greeting)
    log_greeting(greeting)

    while True:
        urdu_text = record_and_transcribe_dynamic()
        if "ختم" in urdu_text or "khatam" in urdu_text.lower():
            print("Exiting. Shukriya!")
            speak(engine, "Shukriya! Allah Hafiz!")
            break

        roman_text = convert_to_roman_urdu(urdu_text)
        if not roman_text:
            continue

        ai_response = generate_ai_reply(roman_text)
        log_chat(urdu_text, roman_text, ai_response)
        speak(engine, ai_response)

    close_log()

if __name__ == "__main__":
    run_chat()
