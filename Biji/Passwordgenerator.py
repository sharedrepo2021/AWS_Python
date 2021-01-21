import random
import string
import json


class Passwordgenerator:

    def createrandompwd(self):
        passwordlength = int(input("Password Length:"))
        passwordcharacters = string.ascii_letters+ string.punctuation + string.digits
        password = []
        for x in range(passwordlength):
            (password.append(random.choice(passwordcharacters)))
        password = "".join(password)
        print(password)
    def createrandompwdletters(self):
        passwordlength = int(input("Password Length:"))
        passwordcharacters = string.ascii_letters
        password = []
        for x in range(passwordlength):
            (password.append(random.choice(passwordcharacters)))
        password = "".join(password)
        print(password)

    def createrandompwddigits(self):
        passwordlength = int(input("Password Length:"))
        passwordcharacters = string.digits
        password = []
        for x in range(passwordlength):
            (password.append(random.choice(passwordcharacters)))
        password = "".join(password)
        print(password)

    def createrandompwdothercharacters(self):
        passwordlength = int(input("Password Length:"))
        passwordcharacters =string.punctuation
        password = []
        for x in range(passwordlength):
            (password.append(random.choice(passwordcharacters)))
        password = "".join(password)
        print(password)

    def createrandompwdexcludecharacters(self):
        passwordlength = int(input("Password Length:"))
        passwordcharacters = string.punctuation + string.digits
        password = []
        for x in range(passwordlength):
            (password.append(random.choice(passwordcharacters)))
        password = "".join(password)
        print(password)

if __name__ == "__main__":
    print(" Password Generator")

option_dict = {
    1: 'Letters ',
    2: 'Digits',
    3: 'Othercharacters',
    4: 'Exclude characters',
    5: 'including all',
    6: 'Exit'
}
print(json.dumps(option_dict, indent=4))

objpwd = Passwordgenerator()

while True:
    choice = int(input("Select an option : "))
    if choice == 1:
        objpwd.createrandompwdletters()
    elif choice == 2:
        objpwd.createrandompwddigits()
    elif choice == 3:
        objpwd.createrandompwdothercharacters()
    elif choice == 4:
        objpwd.createrandompwdexcludecharacters()
    elif choice == 5:
        objpwd.createrandompwd()
    elif choice == 6:
        break
    else:
        print("Enter valid option ")
