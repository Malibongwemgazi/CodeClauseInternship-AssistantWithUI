import speech_recognition as sr
import tkinter as tk
from gtts import gTTS
import os

# Create a GUI with a microphone button
root = tk.Tk()
root.title("Voice Assistant")

def record_voice():
    # Record user's voice
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.record(source)
    try:
        # Process the voice command
        command = r.recognize_google(audio, language="en-US")
        print("You said:", command)
        # Respond with relevant information, solutions, or feedback
        response = "You said " + command
        tts = gTTS(text=response, lang="en")
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand")

mic_button = tk.Button(root, text="Record", command=record_voice)
mic_button.pack()

root.mainloop()
