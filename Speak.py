import pyttsx3
import datetime
Motor = pyttsx3.init('sapi5')
voices = Motor.getProperty('voices')
Motor.setProperty('voice',voices[1].id)
def say_smth(Audio):
    Motor.say(Audio)
    Motor.runAndWait()
def wishU():
    hour=int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say_smth('Good morning')
    elif 12 <= hour <18:
        say_smth('Good afternoon')
    else:
        say_smth('Good evening')
    say_smth('I am Sayeem')
A = wishU()
say_smth(A)