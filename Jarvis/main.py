import speech_recognition as sr 
import pyttsx3 
import subprocess

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def processcommand(command):
    print(f"Command received: {command}")
    
    if "open" in command.lower():
        try:
            # Run 'open_app.py'
            subprocess.run(['python', 'openapp1.py'])  
        except Exception as e:
            speak(f"Error in running the open_app.py file: {e}")
    
    elif "tell" in command.lower():
        try:
            # Run 'texttospeech.py'
            subprocess.run(['python', 'texttospeech.py'])  
        except Exception as e:
            speak(f"Error in running the texttospeech.py file: {e}")
    
    elif "play" in command.lower():
        try:
            # Run 'play_music.py'
            subprocess.run(['python', 'play_music.py'])  
        except Exception as e:
            speak(f"Error in running the play_music.py file: {e}")
    
    else:
        speak("Command not recognized")

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    r = sr.Recognizer()

    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)  # Limit duration

                word = r.recognize_google(audio)
                
                if word.lower() == "jarvis":
                    speak("ahaa")
                    with sr.Microphone() as source:
                        print("Jarvis Activate...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processcommand(command)
        except sr.WaitTimeoutError:
            print("Listening timed out...")
        except sr.UnknownValueError:
            print("Could not understand the audio...")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")
