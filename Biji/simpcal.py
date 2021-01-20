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