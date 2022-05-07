import os
import pyttsx3
import speech_recognition as sr
#import pyAudio
import datetime
#import flask
import pywhatkit
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')                                      #pyttsx3 is python text to speech convertor
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)                            #can change the voice ids

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)                        #to wish date and time to me.
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good evening!')
    speak('Hallo sir, I am Rio. How may i help you?')
def takeCommand():                                                  #to take the speech from user.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        if 'rio' in query:
            query = query.replace('rio', '')
        print(f'User said: {query}\n')
    except Exception as e:
        print(e)
        print('Say that again please...')
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        #to make everything in lower case

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        #browser open works by Rio

        elif 'open youtube' in query:
            speak('youtube is opening')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('google is opening')
            webbrowser.open('google.com')

        elif 'play music' in query:
            speak('use your headphone for best experience, sir')
            webbrowser.open('spotify.com')

        elif 'facebook' in query:
            speak('facebook is opening')
            webbrowser.open('facebook.com')

        elif 'instagram' in query:
            speak('instagram is opening')
            webbrowser.open('instagram.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print('strTime')
            speak(f'Sir, the time is {strTime}')

        elif 'open gmail' in query:
            speak('gmail is opening')
            webbrowser.open('mail.google.com')

        elif 'open whatsapp' in query:
            speak('whatsapp is opening')
            webbrowser.open('web.whatsapp.com')

        # application open by Rio

        elif 'open word' in query:
            speak('microsoft word is opening')
            pathWord = 'C:\\Users\\SHETAAN\\Desktop\\word 2016'
            os.startfile(pathWord)

        elif 'open excel' in query:
            speak('microsoft excel is opening')
            pathExcel = 'C:\\Users\\SHETAAN\\Desktop\\excel 2016'
            os.startfile(pathExcel)

        elif 'open powerpoint' in query:
            speak('microsoft powerpoint is opening')
            pathPower = 'C:\\Users\\SHETAAN\\Desktop\\powerPoint 2016'
            os.startfile(pathPower)

        elif 'open chrome' in query:
            speak('google chrome is opening')
            pathChrome = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome'
            os.startfile(pathChrome)

        elif 'open premiere pro' in query:
            speak('adobe premiere pro is opening')
            pathPremiere = 'C:\\Program Files\\Adobe\\Adobe Premiere Pro 2022\\Adobe Premiere Pro'
            os.startfile(pathPremiere)

        #play any specific song on yt

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'search' in query:
            page = query.replace('search', '')
            speak('searching ' + page)
            webbrowser.open(page)

        #question asked to Rio

        elif 'love you' in query:
            speak('I also love you sir, as my brother. My sir, Rohit made me, so i love him only, not others')

        elif 'f***' in query:
            speak('you are a bad person i think, do not use the abussing words. Go and jurkoff your own.')

        elif 'i look' in query:
            speak('you are looking very handsome, today. Girls are going to be mad when they look at you sir.')

        elif 'you looking' in query:
            speak('I am looking at the ladies face, she is very pritty sir.')

        elif 'are you doing' in query:
            speak('nothing sir, tell me what can i do for you?')

        elif 'sex' in query:
            speak('I know sex is mandetory for reproduction, but I am a machine, i can not do it with you. you are a bad person i think, do not use the abussing words')

        elif 'who are you' in query:
            speak('I am Rio. I am an A.I. I made by my master Rohit. Tell me how can i help you?')

        elif 'is your name' in query:
            speak('My name is Rio. I am an A.I. voice assistant')

        elif 'rohit' in query:
            speak('He is a good Boy, but some time he is very rude. he is my teacher and master, He made me.')

        elif 'arpita' in query:
            speak('yes, she is a good girl, the funny thing is, the name of ex girl friend of, my sir, is same to same')

        elif 'what kind of boy' in query:
            speak('No, he is not overall a good boy. no one is overall good, except my sir, rohit')

        elif 'what kind of girl' in query:
            speak('No, she is not overall a good girl. no one is overall good, except my sir, rohit')









