import pyttsx3
import datetime
import wikipedia
import sys

Motor = pyttsx3.init('sapi5')
voices = Motor.getProperty('voices')
Motor.setProperty('voice', voices[1].id)

def say_smth(Audio):
    Motor.say(Audio)
    Motor.runAndWait()

def wishU():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say_smth('Good morning')
    elif 12 <= hour < 18:
        say_smth('Good afternoon')
    else:
        say_smth('Good evening')
    say_smth('I am Saf')

def command():
    say_smth('What would you like to search?')
    a = input('>')
    return a.lower()

def stuff():
    wishU()
    while True:
        query = command()
        if 'exit' in query:
            say_smth('Goodbye!')
            sys.exit()
        else:
            say_smth('Searching Wikipedia...')
            try:
                result = wikipedia.summary(query, sentences=5)
                print('According to wikipedia')
                say_smth('According to Wikipedia')
                print(result)
                say_smth(result)
            except wikipedia.exceptions.DisambiguationError as e:
                say_smth('There are multiple results, please be more specific.')
            except wikipedia.exceptions.PageError:
                say_smth('I could not find a result for your query.')
            except Exception as e:
                say_smth('An error occurred. Please try again.')

if __name__ == "__main__":
    stuff()
