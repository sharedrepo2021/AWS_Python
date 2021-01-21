# This programs cretes basic calculator using Python Class (OOP)
import json


class Calculator():

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resu = 0

    def getonenum(self):
        self.num1 = int(input('Enter the Number: '))

    def gettwonum(self):
        self.num1 = int(input('Enter the First  Number: '))
        self.num2 = int(input('Enter the Second Number: '))

    def addfunc(self):
        self.resu = self.num1 + self.num2
        print('The Addition value of two given number       : ',  self.resu)

    def subfunc(self):
        self.resu = self.num1 - self.num2
        print('The Subtraction value of two given number    : ',  self.resu)

    def mulfunc(self):
        self.resu = self.num1 * self.num2
        print('The Multiplication value of two given number : ',  self.resu)

    def divfunc(self):
        if self.num2 == 0:
            print('The Division Operation cannot be performed. Divide-By-Zero Error')
        else:
            self.resu = self.num1 / self.num2
            print('The Division value of two given number       : ',  self.resu)

    def perfunc(self):
        if self.num2 == 0:
            print('The Percentage Operation cannot be performed. Divide-By-Zero Error')
        else:
            self.resu = (self.num1 / self.num2) * 100
            print('The Percent of x is y                        : ',  self.resu)

    def sqrfunc(self):
        self.resu = self.num1 ** 2
        print('The Square value of two given number         : ',  self.resu)

    def rotfunc(self):
        self.resu = self.num1 ** 0.5
        print('The Square root value of two given number    : ',  self.resu)

    def powfunc(self):
        self.resu = self.num1 ** self.num2
        print('The x to the power of y                      : ',  self.resu)

    def obyfunc(self):
        if self.num1 == 0:
            print('The 1/X Operation cannot be performed. Divide-By-Zero Error')
        else:
            self.resu = 1 / self.num1
            print('The 1 b y x                                  : ',  self.resu)

if __name__ == '__main__':

    dict_option = {
        1: 'Addition         [+]       ',
        2: 'Subtraction      [-]       ',
        3: 'Multiplication   [*]       ',
        4: 'Division         [/]       ',
        5: 'Percentage       [x is y]  ',
        6: 'Square           [x^2]     ',
        7: 'Square Root      [Vx]      ',
        8: 'To the Power     [x^y]     ',
        9: '1 by x           [1/x]     ',
        0: 'Exit'
    }

    calc = Calculator()

    while True:
        print(json.dumps(dict_option, indent=5))
        opt = int(input("Select Option: "))

        if opt == 1:
            calc.gettwonum()
            calc.addfunc()
        elif opt == 2:
            calc.gettwonum()
            calc.subfunc()
        elif opt == 3:
            calc.gettwonum()
            calc.mulfunc()
        elif opt == 4:
            calc.gettwonum()
            calc.divfunc()
        elif opt == 5:
            calc.gettwonum()
            calc.perfunc()
        elif opt == 6:
            calc.getonenum()
            calc.sqrfunc()
        elif opt == 7:
            calc.getonenum()
            calc.rotfunc()
        elif opt == 8:
            calc.gettwonum()
            calc.mulfunc()
        elif opt == 9:
            calc.getonenum()
            calc.obyfunc()
        elif opt == 0:
            break
        else:
            print('An Invalid Option is Given. Please give correct option')
