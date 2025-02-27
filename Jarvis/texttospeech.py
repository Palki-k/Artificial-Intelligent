import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak ("I am a voice-controlled assistant designed to respond to your commands. ")
    speak ("I listen for the wake word, which is 'Jarvis.' Once I hear it, ")
    speak ("I wait for a command like 'open,' 'tell,' or 'play.' ")
    speak ("Based on your command, I can open specific applications, ")
    speak ("describe my own functions, or play music. I use speech recognition to understand ")
    speak ("your commands and convert them to text, and text-to-speech to respond verbally.")
    
