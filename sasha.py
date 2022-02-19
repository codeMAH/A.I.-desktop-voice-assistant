import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour <17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Sasha in your assistance. How may I help you?")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio= r.listen(source)
    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Please say that again")
        return "None"
    return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('asifhasanmis@gmail.com', 'mah18mail')
    server.sendmail('asifhasanmis@gmail.com', to, content)
    server.close()
     

if __name__== "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir= 'D:\\Web Development\\proj1\\audio'
            songs= os.listdir(music_dir)
            speak("There are 7 songs in the directory, which one shall I play for you?")
            i= int(input())
            os.startfile(os.path.join(music_dir, songs[i]))
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open vs code' in query:
            codePath= "C:\\Users\\asifh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open pycharm' in query:
            pytPath= "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.1\\bin\\pycharm64.exe"
            os.startfile(pytPath)
        elif 'email to asif' in query:
            try:
                speak("What should I say?")
                content= takeCommand()
                to= "asifhasanmis@gmail.com"
                sendEmail(to, content)
                webbrowser.open("https://mail.google.com/mail/u/0/#all")
                speak("Email has been sent")      
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send this email")
        elif 'quit' in query:
            speak("Goodbye, see you soon!")
            break
            

