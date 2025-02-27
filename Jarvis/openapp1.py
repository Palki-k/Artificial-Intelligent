import pyautogui
import subprocess
import time
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speaks(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and return it as text
def speak():
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            try:
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
                speaks("Sorry, I didn't understand that. Please try again.")
                return None
    except sr.WaitTimeoutError:
        print("No speech detected, try again!")
        speaks("No speech detected, please try again.")
        return None

# Function to open an application based on voice command
def open_app(command):
    try:
        print(f"Opening {command}")
        subprocess.run(command)  # Directly runs the command (e.g., "notepad", "calc")
    except Exception as e:
        print(f"Couldn't directly run {command}. Trying with pyautogui: {e}")
        pyautogui.press("win")
        time.sleep(0.5)
        pyautogui.write(command)
        time.sleep(0.5)
        pyautogui.press('enter')

# Main loop to continuously listen for voice commands
if __name__ == "__main__":
    while True:
        speaks("Please name the app you want to open.")
        command = speak()  # Get voice input
        
        if command is not None:  # Check if command is not None
            if "stop" in command.lower():  
                speaks("Stopping the application.")
                break  
            open_app(command)  