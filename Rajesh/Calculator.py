class Calculator:

    def __init__(self, number1, number2, result, chc, div0):
        self.a = number1
        self.b = number2
        self.result = result
        self.choice = chc
        self.d = div0

    def add(self):
        self.result = self.a + self.b
        return self.result

    def sub(self):
        self.result = self.a - self.b
        return self.result

    def mul(self):
        self.result = self.a * self.b
        return self.result

    def div(self):
        self.d = "Cannot Divide By 0"
        if self.b == 0:
            self.result = self.d
        else:
            self.result = self.a / self.b
            self.d = 0
        return self.result

    def getinput(self):
        self.a = int(input("Enter 1st Number : "))
        self.b = int(input("Enter 2nd Number : "))

    def optiondisplay(self):
        print("\n")
        print("Select Options : 1 . Addition")
        print("               : 2 . Subtraction")
        print("               : 3 . Multiplication")
        print("               : 4 . Division")
        print("               : 5 . Exit")
        print("               : 6 . Change Input")
        self.choice = int(input("Choice : "))
        print("\n\n")


if __name__ == "__main__":

    a = 0
    b = 0
    r = 0
    choice = 0
    d = 0
    calc1 = Calculator(a, b, r, choice, d)
    prev1 = Calculator(a, b, r, choice, d)
    calc1.optiondisplay()

    while calc1.choice > 6:
        print("Invalid choice")
        calc1.optiondisplay()

    if calc1.choice != 6:
        calc1.getinput()
    else:
        prev1.choice = calc1.choice

    while calc1.choice != 5:
        if calc1.choice == 1:
            print("\n")
            print("      " + str(calc1.a) + " +")
            print("      " + str(calc1.b))
            print("---------")
            print("      " + str(calc1.add()))
            prev1.choice = calc1.choice
            calc1.optiondisplay()
        elif calc1.choice == 2:
            print("\n")
            print("      " + str(calc1.a) + " -")
            print("      " + str(calc1.b))
            print("---------")
            print("      " + str(calc1.sub()))
            prev1.choice = calc1.choice
            calc1.optiondisplay()
        elif calc1.choice == 3:
            print("\n")
            print("      " + str(calc1.a) + " *")
            print("      " + str(calc1.b))
            print("---------")
            print("      " + str(calc1.mul()))
            prev1.choice = calc1.choice
            calc1.optiondisplay()
        elif calc1.choice == 4:
            print("\n")
            print("      " + str(calc1.a) + " /")
            print("      " + str(calc1.b))
            print("---------")
            print("      " + str(calc1.div()))
            prev1.choice = calc1.choice
            if calc1.d == 0:
                calc1.optiondisplay()
            else:
                print("\n")
                calc1.getinput()
        elif calc1.choice == 5:
            exit()
        elif calc1.choice == 6:
            calc1.getinput()
            if prev1.choice >= 6:
                calc1.optiondisplay()
            else:
                calc1.choice = prev1.choice
        else:
            print("Invalid choice")
            prev1.choice = calc1.choice
            calc1.optiondisplay()
