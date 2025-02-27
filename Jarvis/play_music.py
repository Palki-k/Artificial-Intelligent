import pywhatkit as pw
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to play music on YouTube
def play_music_on_yt(Song_name):
    pw.playonyt(Song_name)

# Function to get voice command
def listen_for_song():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        speak("Listening for song name or say 'stop' to exit.")
        recognizer.adjust_for_ambient_noise(source)  
        print("Listening for song name or say 'stop' to exit.")  
        audio = recognizer.listen(source)

    try:
        speak("Recognizing the song...")
        song_name = recognizer.recognize_google(audio).lower()  
        print(f"Recognized command: {song_name}")  
        speak(f"Song recognized as {song_name}")
        return song_name
    except sr.UnknownValueError:
        speak("Sorry, I did not understand the song name.")
        return None
    except sr.RequestError as e:
        speak(f"Could not request results; {e}")
        return None

# Main loop to continuously listen and play music
while True:
    song_name = listen_for_song()
    
    if song_name:
        if "stop" in song_name:  # Check if "stop" is in the recognized text
            speak("Stopping the program.")
            print("Stopping the program.")  # Debugging message
            break  # Exit the loop if the stop command is given
        else:
            play_music_on_yt(song_name)
