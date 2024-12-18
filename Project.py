from tkinter import *
import datetime
import pyttsx3
import bcrypt
import os

Engine = pyttsx3.init('sapi5')
voices = Engine.getProperty('voices')
Engine.setProperty('voice', voices[1].id)

user_dict = {}

def load_existing_users():
    if os.path.exists('user_data.txt'):
        with open('user_data.txt', 'r') as file:
            for line in file:
                stored_name, stored_hashed_password = line.strip().split(':')
                user_dict[stored_name] = stored_hashed_password

def wishU():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say_smth('Good morning')
    elif 12 <= hour < 18:
        say_smth('Good afternoon')
    else:
        say_smth('Good evening')

def say_smth(Audio):
    Engine.say(Audio)
    Engine.runAndWait()

def say_name():
    Audio=wishU()
    name = Name_entry.get()
    say_smth(Audio)
    Engine.say(f'Welcome, {name}!')
    Engine.runAndWait()

def toggle_password():
    if Pass_entry.cget('show') == '':
        Pass_entry.config(show='*')
        toggle_button.config(text='Show Password')
    else:
        Pass_entry.config(show='')
        toggle_button.config(text='Hide Password')

def hash_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())

def save_data():
    name = Name_entry.get()
    password = Pass_entry.get().encode('utf-8')

    if name in user_dict:
        data_label.config(text="Username already taken.")
    else:
        hashed_password = hash_password(password)
        hashed_name = bcrypt.hashpw(name.encode('utf-8'), bcrypt.gensalt())
        user_dict[name] = hashed_password.decode()

        with open('user_data.txt', 'a') as file:
            file.write(f'{name}:{hashed_password.decode()}\n')
        say_name()
        data_label.config(text="Account created successfully.")

def is_username_taken(username):
    return username in user_dict

load_existing_users()

window = Tk()
window.geometry('700x500')
window.title('Account Config')

label_1 = Label(window, text='Account login', font=('Ink free', 40, 'bold'))
label_1.pack(side='top', fill='x', pady=10)

account_frame = Frame(window)
account_frame.pack(expand=True)

account_frame_2 = Frame(window)
account_frame_2.pack(expand=True)

label_2 = Label(account_frame, text='Account name:', font=('Ink free', 20, 'bold'))
label_2.pack(side='left', padx=5)

label_3 = Label(account_frame_2, text='Account password:', font=('Ink free', 17, 'bold'))
label_3.pack(side='left', padx=5)

Name_entry = Entry(account_frame, font=('Arial', 20))
Name_entry.pack(side='left', padx=5)

Pass_entry = Entry(account_frame_2, font=('Arial', 20), show='*')
Pass_entry.pack(side='left', padx=5)

toggle_button = Button(account_frame_2, text='Show Password', font=('Arial', 12), command=toggle_password)
toggle_button.pack(side='left', padx=10)

submit_button = Button(window, text="Submit", font=('Arial', 16), command=save_data)
submit_button.pack(pady=20)

data_label = Label(window, text="", font=('Arial', 14), justify='left')
data_label.pack(pady=20)

window.mainloop()
