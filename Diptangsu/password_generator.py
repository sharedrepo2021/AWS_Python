from tkinter import *
import pyperclip
import random


class PasswordGenerator:

    def __init__(self):
        self.root = Tk()
        self.pass_str = StringVar()
        self.pass_len = IntVar()

    def pass_generator(self):
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't',
                      'u',
                      'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O',
                      'P',
                      'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      '0',
                      '!',
                      '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', '/']

        password = ''
        for i in range(self.pass_len.get()):
            password = password + random.choice(characters)
        self.pass_str.set(password)

    def copy_clipboard(self):
        random_password = self.pass_str.get()
        pyperclip.copy(random_password)

    def main(self):
        self.root.geometry("400x500")
        self.root.title("Password Generator")
        self.pass_len.set(0)

        Label(self.root, text='Enter password length').pack(pady=3)
        Entry(self.root, textvariable=self.pass_len).pack(pady=3)
        Button(self.root, text='Generate password', command=self.pass_generator).pack()
        Entry(self.root, textvariable=self.pass_str).pack(pady=3)
        Button(self.root, text='Copy to clipboard', command=self.copy_clipboard).pack()
        self.root.mainloop()


if __name__ == "__main__":
    pass_gen = PasswordGenerator()
    pass_gen.main()
