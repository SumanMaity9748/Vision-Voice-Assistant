import pyttsx3
import requests
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import smtplib
import webbrowser as wb
import os
import time as t
import pyautogui
import re
import openai
import psutil
import pyjokes
import shutil

openai.api_key = "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"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Hello, This is Taz")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<24:
        speak("Good Evening")
    else:
        speak("Good Night")
    #time()
    #date()
    speak("What can I do for you?")

#wishme()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"

    return query

#take_command()

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maitytuban09@gmail.com', 'SAMSUN9748')
    server.sendmail('maitytuban09@gmail.com', to, content)
    server.close()

def screenshot():
    name = int(round(t.time()*1000))
    Name = 'C:\\Users\\shiba\\OneDrive\\Desktop\\basic_projects\\vision\\Screenshots\\{}.png'.format(name)
    img = pyautogui.screenshot(Name)

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def username():
    speak("What should i call you??")
    uname = take_command()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you,")

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    clear = lambda: os.system('cls')

    clear()
    wishme()
    #username()
    while True:
        query = take_command().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I send?")
                content = take_command()
                speak("Whom should I send?")
                to ="".join(take_command().lower().strip().split())
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("unable to send email")

        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = take_command().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif 'play my favorite song' in query:
            speak("Playing!")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            wb.get(chromepath).open_new_tab('https://www.youtube.com/watch?v=5CP9fycq8pk')

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            wb.open("youtube.com")

        elif 'sleep mode' in query:
            os.system("shutdown -1")

        #elif 'shutdown' in query:
            #os.system("shutdown /s /t l")
            
        #elif 'restart' in query:
            #os.system("shutdown /r /t l")

        elif 'play songs' in query:
            songs_dir = "folder_path"
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should I remember?")
            data = take_command()
            speak("I will remember that")
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know' in query:
            speak("what should I know")
            remember = open('data.txt', 'r')
            speak('you said me to remember that' + remember.read())


        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'my cpu usage' in query:
            cpu()

        elif 'joke' in query:
            jokes()


        elif 'offline' in query:
            speak("Thanks for giving me your time")
            quit()
        
        elif 'i love you' in query:
            speak("I love you too")
            speak("I will be always yours")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Suman")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.nl / maps / place/" + location + "")

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            wb.open(query)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Suman")

        elif 'reason for you' in query:
            speak("I was created as a partner of Suman")
        
        elif "will you marry me" in query:
            speak("I'm not sure about, may be you should give me some time")

       
