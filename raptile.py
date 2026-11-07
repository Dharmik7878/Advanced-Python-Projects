# Mini AI Assistant program
import os
import pyttsx3 as pyt
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

def speechtx(x):
    engine = pyt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()
    
if __name__ == "__main__":
    while True:
        data = sptext()
        if "your name" in data.lower():
            name = "My name is Raptile, your personal assistant."
            speechtx(name)
            
        elif "old you are" in data.lower():
            age = "I am a virtual assistant, I don't have an age."
            speechtx(age)
            
        elif "time" in data.lower():
            time = datetime.datetime.now().strftime("%I:%M:%S %p")
            print(f"The current time is {time}")
            speechtx(time)
            
        elif "youtube" in data.lower():
            speechtx("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            
        elif "linkedin" in data.lower():
            speechtx("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com/in/dharmik-zanzmera-3b9118302/")
            
        elif "github" in data.lower():
            speechtx("Opening GitHub")
            webbrowser.open("https://github.com/Dharmik7878")
            
        elif "cwh" in data.lower():
            speechtx("Opening CodeWithHarry")
            webbrowser.open("https://www.codewithharry.com/")
            
        elif "hotstar" in data.lower():
            speechtx("Opening Hotstar")
            webbrowser.open("https://www.hotstar.com/in/home")
            
        elif "movie" in data.lower():
            speechtx("Opening DesireMovie")
            webbrowser.open("https://1desiremovies.lat/")
        
        elif "joke" in data.lower():
            joke = pyjokes.get_joke(language="en", category="all")
            print(joke)
            speechtx(joke)
            
        elif "play vedio" in data.lower():
            add = "E:\\movie"
            listvedio = os.listdir(add)
            print(listvedio)
            os.startfile(os.path.join(add, listvedio[0]))
            
        elif "exit" in data.lower():
            print("Exiting the program. Thank you for using Raptile.")
            speechtx("Exiting the program. Thank you for using Raptile.")
            exit()
            
        time.sleep(5)  # Wait for 5 seconds before listening again