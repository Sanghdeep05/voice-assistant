"""import subprocess
import webbrowser

import speech_recognition as sr
import pyttsx3
import datetime

# Initialize speech recognition engine
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Greeting response
greeting = "Hello there! How can I help you today?"

# Loop to listen for commands
while True:
    try:
        # Listen for audio input from the microphone
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        # Convert audio to text
        command = recognizer.recognize_google(audio)

        # Process commands
        if "hello" in command.lower():
            engine.say(greeting)
            engine.runAndWait()
        elif 'chrome' in command:
            a='opening chrome..'
            engine.say(a)
            engine.runAndWait()
            program="C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
            subprocess.Popen([program])

        elif "time" in command.lower():
            current_time = datetime.datetime.now()
            time_string = current_time.strftime("%H:%M:%S")
            engine.say(f"The current time is {time_string}")
            engine.runAndWait()
        elif "date" in command.lower():
            current_date = datetime.datetime.now()
            date_string = current_date.strftime("%Y-%m-%d")
            engine.say(f"The current date is {date_string}")
            engine.runAndWait()
        elif "search" in command.lower():
            # Extract search query from the command
            query = command.split("search for")[-1]
            # Search the web using webbrowser and inform user
            webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
            engine.say(f"Searching for {query} on the web.")
            engine.runAndWait()
        else:
            engine.say("I'm sorry, I don't understand that command.")
            engine.runAndWait()

    except sr.UnknownValueError:
        engine.say("I couldn't understand your command. Please try again.")
        engine.runAndWait()
    except sr.RequestError as e:
        engine.say("There was an error. Please try again later.")
        engine.runAndWait()
        print(f"Could not request results from Google Speech Recognition service; {e}")"""
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import os

# Initialize speech recognition engine
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Greeting response
greeting = "Hello there! How can I help you today?"

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to open Chrome
def open_chrome():
    speak("Opening Chrome")
    os.system('start chrome')

# Function to get current time
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

# Function to get current date
def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"The current date is {current_date}")

# Function to search the web
def search_web(query):
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    speak(f"Searching for {query} on the web.")

# Loop to listen for commands
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        print("Recognizing...")
        command = recognizer.recognize_google(audio)

        if "hello" in command.lower():
            speak(greeting)
        elif 'chrome' in command.lower():
            open_chrome()
        elif "time" in command.lower():
            get_time()
        elif "date" in command.lower():
            get_date()
        elif "search" in command.lower():
            query = command.split("search for")[-1]
            search_web(query)
        else:
            speak("I'm sorry, I don't understand that command.")

    except sr.UnknownValueError:
        speak("I couldn't understand your command. Please try again.")
    except sr.RequestError as e:
        speak("There was an error. Please try again later.")
        print(f"Could not request results from Google Speech Recognition service; {e}")


