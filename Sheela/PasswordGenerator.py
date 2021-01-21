import random
import string

class PasswordGen :
    def __init__(self):
        self.passlist = []

    def autopasswordgen(self,numpass,passlength):

        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        for p in range(numpass):
            digit1 = random.choice(string.ascii_uppercase)
            digit2 = random.choice(string.ascii_lowercase)
            digit3 = random.choice(string.digits)
            digit4 = random.choice(string.punctuation)
            password = ""
            password = digit1 + digit2 + digit3 + digit4
            for b in range(passlength - 4):
                password = password + random.choice(chars)
                print("password2",password)
            self.passlist.append(password)
        return self.passlist



if __name__ == '__main__':
    print("AUTOMATIC PASSWORD GENERATOR")
    while True:
        number = int(input("Enter Number of Passwords to be generated :"))
        if number == 0:
            print("Its cant be 0. Enter at least 1")
        else:
            while True:
                length = int(input("Enter the length(min8) of the password to be generated"))
                if length < 8:
                    print("Its cant be less than 8. Enter a number 8 or more than 8")
                else:
                    passwordgen = PasswordGen()
                    passwordlist = passwordgen.autopasswordgen(number, length)
                    print(str(number) + "  Passwords Generated :")
                    for i in range(len(passwordlist)):
                        print(passwordlist[i])
                    break
            break
