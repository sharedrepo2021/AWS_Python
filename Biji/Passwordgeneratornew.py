import string
import tkinter as tk
import random


class Generatepassword:
    def __init__(self):
        self.length = None
        self.pwd = None

    def print_selection(self):

        try:
            self.length = int( txtpwdlength.get())

            if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):

                self.pwd = []
                passwordcharacters = string.ascii_letters
                for x in range(self.length):
                    (self.pwd.append(random.choice(passwordcharacters)))
                self.pwd = "".join(self.pwd)
                lblpwdresult["text"] = self.pwd
            elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0):

                self.pwd = []
                passwordcharacters = string.digits
                for x in range(self.length):
                    (self.pwd.append(random.choice(passwordcharacters)))
                self.pwd = "".join(self.pwd)
                lblpwdresult["text"] = self.pwd
            elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):
                self.length = int( txtpwdlength.get())
                self.pwd = []
                passwordcharacters = string.punctuation
                for x in range(self.length):
                    (self.pwd.append(random.choice(passwordcharacters)))
                self.pwd = "".join(self.pwd)
                lblpwdresult["text"] = self.pwd
            elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0):
                self.pwd = []
                passwordcharacters = string.ascii_letters + string.digits
                for x in range(self.length):
                    (self.pwd.append(random.choice(passwordcharacters)))
                self.pwd = "".join(self.pwd)
                lblpwdresult["text"] = self.pwd
            elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1):
                self.pwd = []
                passwordcharacters = string.punctuation + string.ascii_letters
                for x in range(self.length):
                    (self.pwd.append(random.choice(passwordcharacters)))
                self.pwd = "".join(self.pwd)
                lblpwdresult["text"] = self.pwd
            elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 1):
                self.pwd = []
                passwordcharacters = string.punctuation + string.digits
                for x in range(self.length):
                    (self.pwd.append(random.choice(passwordcharacters)))
                self.pwd = "".join(self.pwd)
                lblpwdresult["text"] = self.pwd
            elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0):
                lblpwdresult["text"] = "Please select one"
            else:
                self.length = int( txtpwdlength.get())
                self.pwd = []
                passwordcharacters = string.ascii_letters + string.digits + string.punctuation
                for x in range(self.length):
                    (self.pwd.append(random.choice(passwordcharacters)))
                self.pwd = "".join(self.pwd)
                lblpwdresult["text"] = self.pwd
        except:
          lblpwdresult["text"] = "Pls.Enter length as in Integer only"


if __name__ == '__main__':
    objpg = Generatepassword()
    window = tk.Tk()
    window.title("Password Generator")
    frameform = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frameform.pack()
    lblpwdlength = tk.Label(master=frameform, text="Password Length: ")
    txtpwdlength = tk.Entry(master=frameform, width=20)
    lblpwdlength.grid(row=0, column=1, sticky="e")
    txtpwdlength.grid(row=0, column=2)
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    c1 = tk.Checkbutton(window, text='letters', variable=var1, onvalue=1, offvalue=0)
    c1.pack()
    c2 = tk.Checkbutton(window, text='digits', variable=var2, onvalue=1, offvalue=0)
    c2.pack()
    c3 = tk.Checkbutton(window, text='Other characters', variable=var3, onvalue=1, offvalue=0)
    c3.pack()
    btn_pwd = tk.Button(window, text="Generate Password", command=objpg.print_selection)
    btn_pwd.pack()    
    frameresult = tk.Frame(relief=tk.FLAT, borderwidth=2)
    lblpwdresult = tk.Label(master=frameresult, text='')
    lblpwdresult.grid(row=0, column=0, sticky="e")
    frameresult.pack()
    window.mainloop()
