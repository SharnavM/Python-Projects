import win32com.client as wc
import speech_recognition as sr
import requests
import webbrowser
from time import localtime, strftime, sleep
from bs4 import BeautifulSoup
import keyboard
import subprocess as sp
import pyautogui as pg
import os

speaker = wc.Dispatch("Sapi.Spvoice")
firefox_path = "D:/Mozilla Firefox_Extended/firefox.exe %s"

def speak(string):
    speaker.Speak(string)

def  getTemperature():
    url = f"https://www.google.com/search?q=weather+in+pune"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    update = soup.find("div", class_="BNeawe").text
    print(f"Temperature in Pune now is {update}")
    speak(f"Temperature in Pooney now is {update}")

def getWeather():
    url = f"https://www.google.com/search?q=weather+in+pune"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    update = soup.find("span",{"id":"wob_dc"}).text
    print(f"weather in Pune now is {update}")
    speak(f"weather in Pooney now is {update}")


def openURL(url):
    if url.lower()=="youtube":
        speak("opening youtube")
        webbrowser.get(firefox_path).open("youtube.com")
    elif url == "whatsapp":
        speak("opening whatsapp web")
        webbrowser.get(firefox_path).open("web.whatsapp.com")
    elif url == "gmail":
        speak("opening G mail")
        webbrowser.get(firefox_path).open("mail.google.com/mail/u/0/#inbox")
    elif url == "github":
        speak("opening git hub")
        webbrowser.get(firefox_path).open("github.com")
    else:
        url = url.replace("dot",".").replace(" ","")
        speak("Opening URL")
        webbrowser.get(firefox_path).open(f"{url}")
        

def searchGoogle(query):
    webbrowser.get(firefox_path).open(f"google.com/search?q={query}", new=2)

def searchYT(query):
    speak(f"Searching youtube for {query}")
    query = query.replace(" ","+")
    webbrowser.get(firefox_path).open(f"www.youtube.com/results?search_query={query}", new=2)

def recognise():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Speak Command:- ",end="")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            data = r.recognize_google(audio)
            print(data)

            if "open url" in data.lower():
                query = data.lower().replace("open url", "").strip()
                openURL(query.lower())

            if "what time is it" in data.lower():
                print(strftime("Its %I:%M %p", localtime()))
                speak(strftime("%M minutes past %I %p", localtime()))

            if "temperature right now" in data.lower():
                getTemperature()

            if "weather right now" in data.lower():
                pass

            if "google for" in data.lower():
                query = data.lower().replace("search","").replace("google for","").strip()
                searchGoogle(query.lower())

            if "youtube for" in data.lower():
                query = data.lower().replace("search","").replace("youtube for","").strip()
                searchYT(query.lower())

            if "shutdown system" in data.lower():
                speak("Initiating System Shutdown Sequence. Goodbye")
                os.system("shutdown /s /t 00")
                
        except Exception as e:
            print(e)
            speak("An Exception occured while processing the command")
            pass

    

try:
    requests.get("https://www.google.com", timeout = 3)
except (requests.ConnectionError, requests.Timeout)  as exception:
    speak("I am offline. Try Again with net Connection")
else:
    speak("I have indeed been uploaded and Ready")

speak("Press F 12 and Speak your Command")

while True:
  
    if(keyboard.read_key()=="f12"):
        recognise()
