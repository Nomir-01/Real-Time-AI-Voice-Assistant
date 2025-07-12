# Handles chat logging (optional) saving Urdu, Roman Urdu and AI replies with timestamps

import os
from datetime import datetime
from config import LOGGING_ENABLED, CHAT_LOG_DIR

log_file = None

def start_new_log():
    """
    Opens a new log file with timestamped filename in the chat logs directory.
    """
    global log_file
    if not LOGGING_ENABLED:
        return
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    os.makedirs(CHAT_LOG_DIR, exist_ok=True)
    log_file = open(os.path.join(CHAT_LOG_DIR, filename), "w", encoding="utf-8")

def log_heading():
    """
    Writes the heading at the start of a log file.
    """
    if log_file:
        log_file.write("=== AI Voice Chat Log ===\n")
        log_file.write("Timestamped entries of user and AI conversation.\n")
        log_file.write("-" * 60 + "\n\n")
        log_file.flush()

def log_greeting(greeting):
    """
    Logs the initial greeting message from the bot.
    """
    if log_file:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_file.write(f"{timestamp} AI Greeting: {greeting}\n")
        log_file.write("-" * 60 + "\n")
        log_file.flush()

def log_chat(urdu_text, roman_text, ai_reply):
    """
    Logs a single turn of chat: User's input (Roman + Urdu) and AI reply.
    """
    if not LOGGING_ENABLED or log_file is None:
        return

    now = datetime.now()
    log_file.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] User (Roman Urdu): {roman_text}\n")
    log_file.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] User (Urdu): {urdu_text}\n")
    log_file.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] AI Reply: {ai_reply}\n")
    log_file.write("-" * 60 + "\n")
    log_file.flush()

def close_log():
    """
    Closes the log file at the end of the session.
    """
    global log_file
    if log_file:
        log_file.close()
