import random
import re


class Password:
    def __init__(self):
        self.number = None
        self.char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*~'

    def input_length(self):
        self.number = int(input("Enter the length of the password you want:: "))

    def output(self):
        _nu1 = 0
        for p in range(self.number):
            password = ''
            for c in range(self.number):
                password += random.choice(self.char)
            _nu1 = _nu1 + 1
            print('{}.{}'.format(_nu1, password))
            x = re.findall("[!@#$%^&*~]", password)
            y = re.findall("[0-9]", password)

            if x:
                if y:
                    print("Strong Password!")
                else:
                    print("Medium Password!")
            else:
                print("Weak Password!")


if __name__ == '__main__':
    pas = Password()
    pas.input_length()
    pas.output()

