import webbrowser
import speech_recognition as sr
import os
import win32com.client
import openai
import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")
def takeCommand():
    r= sr.Recognizer()
    with (sr.Microphone() as source):
         r.pause_threshold=  0.6
         audio=r.listen(source)
    try:
            print("Recognizing.....")
            query=r.recognize_google(audio, language="en-in")
            print(f"User said:{query}")
            return query
    except Exception as e:
            return ("Some Error Occured Sorry From Jarvis")

speaker.Speak("hello I am your virtual assistant Jarvis ")
while 1:
    print("Listening....")
    query = takeCommand()
    # todo: add more sites
    sites = [["youtube","https://www.youtube.com"], ["wikipedia","https://www.wikipedia.com"],["Google","https://www.google.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
           speaker.Speak(f"Opening {site[0]} VARMA....")
           webbrowser.open(site[1])
    #todo: add a feature to play a specific song
    if "open music" in query:
        musicPath = "C:/Users/Chaitanya Varma/Downloads/tvari-hawaii-vacation-159069.mp3"
        os.startfile(musicPath)

    if "the time" in query:
        musicPath = "C:/Users/Chaitanya Varma/Downloads/tvari-hawaii-vacation-159069.mp3"
        strftime = datetime.datetime.now().strftime("%H:%M:%S")
        speaker.Speak(f"VARMA the time is {strftime}")
    #todo: add more applications
    if "open valorant" in query:
        gamepath = "C:/Users/Chaitanya Varma/Documents/MY JUNK/VALORANT.url"
        speaker.Speak(f"Varma opening Valorant enjoy the game...")
        os.startfile(gamepath)
    #todo: add more personel details of jarvis
    if "who created you" in query:
        speaker.Speak("i was created by Alluri Chaitanya Varma")
        print("ALLURI CHAITANYA VARMA")
    if "when is your birthday" in query:
        speaker.Speak("My Birthday is on 11th of feb 2024")
        print("11th feb 2024")
        ##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