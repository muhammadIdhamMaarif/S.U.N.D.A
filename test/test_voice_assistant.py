# test/test_voice_assistant.py
from voice_assistant.tts import speak
from core.logger import log

def simulate_voice_assistant():
    print("Simulasi Voice Assistant (ketik perintah):")
    while True:
        command = input("Kamu: ").lower()
        log("AI", f"Command received: {command}")

        if "musik" in command or "music" in command:
            speak("Memutar musik.")
        elif "cuaca" in command or "weather" in command:
            speak("Hari ini cerah dan hangat.")
        elif "rekam" in command or "record" in command:
            speak("Merekam video sekarang.")
        elif "keluar" in command or "exit" in command:
            speak("Sampai jumpa!")
            break
        else:
            speak("Maaf, saya tidak mengerti.")

if __name__ == "__main__":
    simulate_voice_assistant()
