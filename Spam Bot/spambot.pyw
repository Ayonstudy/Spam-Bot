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
    spam_value = entryB.get()
    f = open("spam-record.txt", "w")
    f.write(str(spam_value))
    f.close()
    spam_number = entryC.get()
    spam_number_value = spam_number.strip('')
    global spam_frequency
    spam_frequency = int(spam_number_value)


ping_active = 0
def ping_update():
    global ping_active
    ping_active = ping_value.get()

menuA = ttk.Frame(window)
menuB = ttk.Frame(window)
menuC = ttk.Frame(window)
menu_submit = ttk.Frame(window)

menuA.place(x=0, y= 0, relwidth=1, relheight=0.25)
menuB.place(x=0, rely=0.25, relwidth=1, relheight=0.25)
menuC.place(x=0, rely=0.50, relwidth=1, relheight=0.25)
menu_submit.place(x=0, rely=0.75, relwidth=1, relheight=0.25)

ping_value = IntVar()
labelA = Label(menuA, text="ping")
labelA.pack(side=LEFT)
checkboxA = Checkbutton(menuA,text='@',command=ping_update,variable=ping_value,onvalue=1,offvalue=0)
checkboxA.pack(side=LEFT)

labelB = Label(menuB, text="Enter Spam Line:")
labelB.pack(side=LEFT)
entryB = Entry(menuB)
entryB.pack(side=RIGHT, expand=True)
entryB.config(width=45)

labelC = Label(menuC, text="Spam Occurance:")
labelC.pack(side=LEFT)
entryC = Entry(menuC)
entryC.pack(side=RIGHT, expand=True)
entryC.config(width=45)




def spam_info():
    time.sleep(0.1)
    f = open("spam-record.txt", "r")
    for each_line in f:
        pyautogui.typewrite(each_line)
        if ping_active == 1:
            pyautogui.press("enter")
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
