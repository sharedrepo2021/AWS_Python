import json
import math


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def sub(self):
        print(self.num1 - self.num2)

    def mul(self):
        print(self.num1 * self.num2)

    def div(self):
        print(self.num1 / self.num2)

    def getinp(self, num1, num2):
        self.num1 = int(input("Enter first number:"))
        self.num2 = int(input("Enter second number:"))
    def squarein(self,num1):
        print(math.sqrt(num1))
    def power(self, num1,num2):
        print(math.pow(self.num1,self.num2))
    def remainder(self, num1,num2):
        print(math.remainder(self.num1,self.num2))

print("  Calculator  ")
option_dict = {
    1: 'Addition',
    2: 'Substraction',
    3: 'Multiplication',
    4: 'Division',
    5:'square root',
    6:'Power',
    7:'Remainder'
}
print(json.dumps(option_dict, indent=4))

if __name__ == "__main__":

 while True:

    choice = int(input("Select an option : "))

    #    x = int(input("Enter first number:"))
    #    y = int(input("Enter second number:"))
    x = 0
    y = 0

    objcal = Calculator(x, y)
#    objcal.getinp(x, y)

    if choice == 1:
        objcal.getinp(x, y)
        objcal.add()
    elif choice == 2:
        objcal.getinp(x, y)
        objcal.sub()
    elif choice == 3:
        objcal.getinp(x, y)
        objcal.mul()
    elif choice == 4:
        objcal.getinp(x, y)
        if y == 0:
            print("no number can divide by 0")
        else:
            objcal.div()
    elif choice == 5:
        x = int(input("Enter  number:"))
        objcal.squarein(x)
    elif choice == 6:
        objcal.getinp(x,y)
        objcal.power(x,y)
    elif choice == 7:
        objcal.getinp(x,y)
        objcal.remainder(x,y)
    else:
        print("Enter a valid option")
