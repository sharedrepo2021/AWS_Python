import tkinter as tk
from tkinter import *
import string
import random

window = tk.Tk()
window.title('My Window')
window.geometry('100x100')

l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()




def say_hi():
    print("hi there, everyone!")

def print_selection():

    if (var1.get() == 1) & (var2.get() == 0):



        passwordlength = int(input("Password Length:"))
        passwordcharacters = string.ascii_letters
        password = []
        for x in range(passwordlength):
            (password.append(random.choice(passwordcharacters)))
        password = "".join(password)
        print(password)

    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='Please select one')
    else:
        l.config(text='I love both')



var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text='letters', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='digits', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
b1 = tk.Button(window)
b1["text"] = "Generate Random Password\n(click me)"
b1["command"] =print_selection()
b1.pack()
#quit = tk.Button(text="QUIT", fg="red",
                 #command=master.destroy)
#quit.pack(side="bottom")



window.mainloop()