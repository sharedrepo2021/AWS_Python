import json


class Calculator:
    def __init_(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.countadd = 0
        self.addlist = []
        self.addlistlen = 0


    def oneinput(self):
        self.c = int(input('Enter the Number: '))

    def twoinput(self):
        self.a = int(input('Enter the First  Number: '))
        self.b = int(input('Enter the Second Number: '))

    def nnuminput(self):
        self.countadd = int(input('Enter the count of Numbers to be added: '))
        self.addlist = []
        if self.countadd in (0, 1):
            print("Need minimum 2 numbers")
        else:
            for i in range(int(self.countadd)):
                self.addlist.append(int(input('Enter the number you want to add : ')))

    def add(self):
        self.total1 = 0
        self.addlistlen = int(len(self.addlist))
        for k in range(self.addlistlen):
            self.total1 += self.addlist[k]
        return self.total1

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return "You cant have denominator zero! Give valid denominator! "
        else:
            return self.a / self.b

    def percent(self):
        if self.b == 0:
            return "You cant have denominator zero! Give valid denominator "
        else:
            return (self.a / self.b) * 100

    def sqrfunc(self):
        return self.c ** 2

    def sqrroot(self):
        return self.c ** 0.5




option_calc = {

    1: 'Add',
    2: 'Subtract',
    3: 'Multiple',
    4: 'Divide',
    5: 'Pertentage',
    6: 'Square',
    7: 'Square root',
    8: 'Exit'

}
print(json.dumps(option_calc, indent=4))

objcal = Calculator()

while True:

    i = int(input("Select an option : "))
    if i == 1:
        objcal.nnuminput()
        print("Result for ADD : ", objcal.add())
    elif i == 2:
        objcal.twoinput()
        print("Result for SUB: ", objcal.sub())
    elif i == 3:
        objcal.twoinput()
        print("Result for MUL: ", objcal.mul())
    elif i == 4:
        objcal.twoinput()
        print("Result for DIV: ", objcal.div())
    elif i == 5:
        objcal.twoinput()
        print("Result PERCENT:", str(objcal.percent()) + "%")
    elif i == 6:
        objcal.oneinput()
        print("Result SQUARE :", objcal.sqrfunc())
    elif i == 7:
        objcal.oneinput()
        print("Result SQUAREROOT:", objcal.sqrroot())
    elif i == 8:
        break
    else:
        print("Invalid choice!! Give numbers specified in the options")