import pyautogui, time
from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("500x200")
window.minsize(500,200)
window.maxsize(500,200)
window.title("Smiling Spam Bot")
icon = PhotoImage(file="giorno_arrow_scene.png")
window.iconphoto(True,icon)

def spam_update():
    spam_value = entryA.get()
    f = open("spam-record.txt", "w")
    f.write(str(spam_value))
    f.close()
    spam_number = entryB.get()
    spam_number_value = spam_number.strip('')
    global spam_frequency
    spam_frequency = int(spam_number_value)

menuA = ttk.Frame(window)
menuB = ttk.Frame(window)
menu_submit = ttk.Frame(window)

menuA.place(x=0, y=0, relwidth=1, relheight=0.4)
menuB.place(x=0, rely=0.4, relwidth=1, relheight=0.4)
menu_submit.place(x=0, rely=0.8, relwidth=1, relheight=0.2)


labelA = Label(menuA, text="Enter Spam Line:")
labelA.pack(side=LEFT)
entryA = Entry(menuA)
entryA.pack(side=RIGHT, expand=True)
entryA.config(width=45)

labelB = Label(menuB, text="Spam Occurance:")
labelB.pack(side=LEFT)
entryB = Entry(menuB)
entryB.pack(side=RIGHT, expand=True)
entryB.config(width=45)

def spam_info():
    time.sleep(0.1)
    f = open("spam-record.txt", "r")
    for each_line in f:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")
        

def spam_control():
    a = 0
    time.sleep(5)
    while a < spam_frequency:
        spam_info()
        a += 1

def spam_start():
    spam_update()
    spam_control()

submit = Button(menu_submit, text = "RUN SPAM!!!", command = spam_start)
submit.pack()

window.mainloop()