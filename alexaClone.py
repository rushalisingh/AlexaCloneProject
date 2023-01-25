import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' ,voices[0].id)
engine.say('Hi ! I am Alex')
engine.say('What can I do for you ?')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command ():
    try :
        with sr.Microphone() as source :
            print('listening ....')
            voice = listener.listen(source)
            command =listener.recognize_google(voice)
            command = command.lower()
            command =command.replace('alexa', ' ')
            print(command)
    except :
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play' , ' ')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command :
            time = datetime.datetime.now().strftime('%I:%M:%S %p')
            print(time)
            talk ('Current time is '+time)
    elif 'tell me about' in command:
            person = command.replace('tell me about', ' ')
            info =wikipedia.summary(person ,1)
            print(info)
            talk(info)
    elif 'joke' in command :
        talk(pyjokes.get_joke())
    else :
        talk('Please say the command again')


while True:
        run_alexa()
