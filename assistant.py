import speech_recognition as sr
import webbrowser
import pyttsx3
import time
from datetime import datetime
import os
import subprocess

engine = pyttsx3.init()
recognizer = sr.Recognizer()

assistant_activated = False

while True:
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("You said:", text)

        if "hp" in text:
            assistant_activated = True
            engine.say("Hello! How can I assist you today?")
            engine.runAndWait()
            # engine.stop()
            continue

        if assistant_activated:
            if "time" in text:
                current_time=datetime.now().strftime("%I:%M %p")
                engine.stop()
                time.sleep(0.3)

                # engine.say(f"The current time is {current_time}")
                engine.say("Checking time command...")
                engine.say(current_time)
                print("Checking time command...")
                print(f"The current time is {current_time}")
                engine.runAndWait()
            # elif "open" in text:
            #     apps= text.replace("open", "").strip()
            #     subprocess.Popen(apps)
            #     engine.say("Opening"+apps)
            elif "open" in text:
                app = text.replace("open", "").strip()
                engine.say(f"Opening {app}")
                engine.runAndWait()
                webbrowser.open(f"https://www.{app}.com")

            elif "shut down" in text:
                engine.say("Shutting down the assistant. Goodbye!")
                engine.runAndWait()
                assistant_activated = False

    except sr.UnknownValueError:
        engine.say("Sorry, I couldn't understand.")
        engine.runAndWait()