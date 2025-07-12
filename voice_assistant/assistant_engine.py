# voice_assistant/assistant_engine.py
# Asisten AI menggunakan Mycroft atau Google Assistant SDK

from voice_assistant.wake_word import wait_for_wake
from voice_assistant.stt import recognize_speech
from voice_assistant.tts import speak
from core.logger import log


def start_assistant():
    log("AI", "Voice Assistant Siap.")

    while True:
        wait_for_wake()
        log("AI", "Wake word detected. Listening...")

        command = recognize_speech()
        log("AI", f"Command: {command}")

        # Eksekusi perintah dasar
        if "music" in command:
            speak("Playing music.")
        elif "weather" in command:
            speak("Today is sunny.")
        elif "record" in command:
            speak("Saving video.")
        else:
            speak("Sorry, I don't understand.")
