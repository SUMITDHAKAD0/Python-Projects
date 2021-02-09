
import speech_recognition as sr # Take voive from User
import pyttsx3 #Audio to Text
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def talk_command():
    try:
        with sr.Microphone() as source:
            print('Listining....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def imshme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk('good Morning sir!')
    elif hour>=12 and hour<18:
        talk('good afternoon sir!')
    else:
        talk('good evening sir!')
    talk('hello . I am Jarvis. How may I help you')

def run_alexa():
    imshme()
    command = talk_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song) # playonyt means play song on youtube

    elif 'find' in command :
        command = command.replace('find', '')
        print(command)
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info) 
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current Time is' + time)
        talk(time)

run_alexa()