from tkinter import *
from PIL import Image, ImageTk
import threading

Rebirth_upgrade=0
Rebirths = 1
Count = 0
Upgrade = 1

def Rebirthing():
    global Rebirths, Upgrade, Count, Rebirth_upgrade
    Count=0
    Upgrade=1
    Rebirths+=1
    Rebirth_upgrade+=1
    Rebirth_count.config(text=f'Rebirths: {Rebirths-1}')
    Rebirth_counting.config(text=f'Resets upgrades and clicks for \n upgrades and clicks \n costs {Rebirths*1000}')
    Rebirth_counting.config(state=DISABLED)
    Upgrader.config(text=f'Upgrade \n Makes clicks worth +1 \n Costs {Upgrade * 10} clicks')
    Counter.config(text=f'Count:{Count}')
    update_upgrade_button()
    check_upgrade_availability()

def Upgrading():
    global Count, Upgrade
    Count -= Upgrade * 10
    Upgrade += 1
    Counter.config(text=f'Count: {Count}')
    update_upgrade_button()
    check_upgrade_availability()

def Counting():
    global Count, Upgrade, Rebirths, Rebirth_upgrade
    Count += Upgrade + Rebirth_upgrade
    Counter.config(text=f'Count: {Count}')
    check_upgrade_availability()

def check_upgrade_availability():
    if Count >= Upgrade * 10:
        Upgrader.config(state=ACTIVE)
    else:
        Upgrader.config(state=DISABLED)
    if Count >= Rebirths*1000:
        Rebirth_counting.config(state=ACTIVE)
    else:
        Rebirth_counting.config(state=DISABLED)
def update_upgrade_button():
    Upgrader.config(text=f'Upgrade \n Makes clicks worth +1 \n Costs {Upgrade * 10} clicks')

window = Tk()

img = Image.open('C:\\Users\\sakib\\Desktop\\Python\\Cursor.jpg')
image = ImageTk.PhotoImage(img)

Rebirth_count = Label(window, text=f'Rebirths: {Rebirths-1}', font=('Ink Free', 24, 'bold'))
Rebirth_count.pack(expand=True)

Counter = Label(window, text=f'Count: {Count}', font=('Ink Free', 24, 'bold'))
Counter.pack()

Clicker = Button(window, image=image, font=('Ink Free', 50, 'bold'), command=Counting)
Clicker.pack(expand=True)

Upgrader = Button(window, font=('Ink Free', 24, 'bold'), command=Upgrading)
Upgrader.pack(expand=True)

Rebirth_counting=Button(window,text=f'Resets upgrades and clicks for \n upgrades and clicks \n costs {Rebirths*1000}',font=('Ink free',24,'bold'))
Rebirth_counting.config(command=Rebirthing)
Rebirth_counting.pack(expand=True)
update_upgrade_button()
check_upgrade_availability()

window.mainloop()
