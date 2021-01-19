import json
import math


class Calculator:
    def __init__(self):
        self.a = None
        self.b = None

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

    def sqr_root(self):
        return self.a ** 0.5

    def log(self):
        return math.log(self.a)

    def sin(self):
        return math.sin(self.a)

    def cos(self):
        return math.cos(self.a)

    def tan(self):
        return math.tan(self.a)

    def input_2(self):
        self.a = float(input("Enter the first number: "))
        self.b = float(input("Enter the second number: "))

    def input_1(self):
        self.a = float(input("Enter the number: "))


if __name__ == "__main__":

    operation_dict = {
        1: 'Exit',
        2: 'Addition',
        3: 'Multiplication',
        4: 'Division',
        5: 'Subtraction',
        6: 'Square root',
        7: 'log',
        8: 'sin',
        9: 'cos',
        10: 'tan'

    }
    print(json.dumps(operation_dict, indent=5))
try:
    obj_calc = Calculator()

    while True:
        i = int(input("Please select the operation: "))

        if i == 1:
            print("Thank you")
            break

        elif i == 2:
            obj_calc.input_2()
            print("Addition =", obj_calc.addition())
        elif i == 3:
            obj_calc.input_2()
            print("Multiplication =", obj_calc.multiplication())
        elif i == 4:
            obj_calc.input_2()
            print("Division=", obj_calc.division())
        elif i == 5:
            obj_calc.input_2()
            print("subtraction=", obj_calc.subtraction())
        elif i == 6:
            obj_calc.input_1()
            print('Square root =', obj_calc.sqr_root())
        elif i == 7:
            obj_calc.input_1()
            print("log =", obj_calc.log())
        elif i == 8:
            obj_calc.input_1()
            print("sin =", obj_calc.sin())
        elif i == 9:
            obj_calc.input_1()
            print("cos =", obj_calc.cos())
        elif i == 10:
            obj_calc.input_1()
            print("tan =", obj_calc.tan())

        else:
            print("Please select a valid operation")
except:
    print("Please enter a valid number")


