import secrets
import string
import tkinter as tk


class PassGen:
    def __init__(self):
        self.length = None
        self.schars = '!@#$%&'
        self.psword = None

    def onlyalpha(self):
        try:
            self.length = int(entry_pwd_length.get())
            if self.length > 5:
                self.psword = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) \
                           for _ in range(self.length))
                label_pwd_result["text"] = self.psword
            else:
                label_pwd_result["text"] = 'Length should be > 5'
        except:
            label_pwd_result["text"] = 'Not a Valid Entry'

    def alphanum(self):
        try:
            self.length = int(entry_pwd_length.get())
            if self.length > 5:
                self.psword = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) \
                              for _ in range(self.length))
                label_pwd_result["text"] = self.psword
            else:
                label_pwd_result["text"] = 'Length should be > 5'
        except:
            label_pwd_result["text"] = 'Not a Valid Entry'

    def mixedpass(self):
        try:
            self.length = int(entry_pwd_length.get())
            if self.length > 5:
                self.psword = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + \
                                             self.schars) for _ in range(self.length))
                label_pwd_result["text"] = self.psword
            else:
                label_pwd_result["text"] = 'Length should be > 5'
        except:
            label_pwd_result["text"] = 'Not a Valid Entry'


if __name__ == '__main__':

    pg = PassGen()
    window = tk.Tk()
    window.title("Password Generator")
    frame_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    frame_form.pack()

    label_pwd_length = tk.Label(master=frame_form, text="Password Length: ")
    entry_pwd_length = tk.Entry(master=frame_form, width=20)
    label_pwd_length.grid(row=0, column=1, sticky="e")
    entry_pwd_length.grid(row=0, column=2)

    frame_buttons = tk.Frame()
    frame_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    btn_Alpha = tk.Button(master=frame_buttons, text="Only Alpha", command=pg.onlyalpha)
    btn_Alpha.pack(side=tk.RIGHT, padx=10, ipadx=10)
    btn_Alphanum = tk.Button(master=frame_buttons, text="Alphanumeric", command=pg.alphanum)
    btn_Alphanum.pack(side=tk.RIGHT, padx=10, ipadx=10)
    btn_mixed = tk.Button(master=frame_buttons, text="SpecialChar", command=pg.mixedpass)
    btn_mixed.pack(side=tk.RIGHT, ipadx=10)

    frame_result = tk.Frame(relief=tk.FLAT, borderwidth=2)
    label_pwd_result = tk.Label(master=frame_result, text='')
    label_pwd_result.grid(row=0, column=0, sticky="e")
    frame_result.pack()

    window.mainloop()
