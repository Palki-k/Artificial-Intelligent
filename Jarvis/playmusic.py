import pywhatkit as pw
import speech_recognition as sr


# Function to play music on YouTube
def play_music_on_yt(Song_name):
    pw.playonyt(Song_name)

# Function to get voice command
def listen_for_song():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for song name...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusting for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        song_name = recognizer.recognize_google(audio)
        print(f"Song recognized: {song_name}")
        return song_name
    except sr.UnknownValueError:
        print("Sorry, I did not understand the song name.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

# Main loop to continuously listen and play music
while True:
    song_name = listen_for_song()
    if song_name:
        play_music_on_yt(song_name)
