class Calculator:

    def __init__(self):
        self.a = 0
        self.b = 0
        self.result = None
        self.choice = None
        self.d = None

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
            self.result = round(self.a / self.b, 2)
            self.d = 0
        return self.result

    def getinput(self):
        while True:
            try:
                self.a = int(input("Enter 1st Number : "))
                self.b = int(input("Enter 2nd Number : "))
                break
            except:
                print("!!! Not a Valid Input !!!")

    def print_heading(self, heading):
        print('=' * (len(heading) + 2))
        print(heading)
        print('=' * (len(heading) + 2))


    def optiondisplay(self):
        print("   *****************************")
        print("   |   CALCULATOR VERSION.01   |")
        print("   *****************************")
        print("   |  1  |    Addition         |")
        print("   -----------------------------")
        print("   |  2  |    Subtraction      |")
        print("   -----------------------------")
        print("   |  3  |    Multiplication   |")
        print("   -----------------------------")
        print("   |  4  |    Division         |")
        print("   -----------------------------")
        print("   |  5  |    Exit             |")
        print("   -----------------------------")
        print("   |  6  |    Change Input     |")
        print("   -----------------------------")
        print("\n")
        while True:
            try:
                self.choice = int(input("Choice : "))
                break
            except:
                print("!!! Not a Valid Input !!!")
        print("\n")


if __name__ == "__main__":


    calc1 = Calculator()
    prev1 = Calculator()
    a = 10
    calc1.print_heading("Dipan {}".format(a))
    calc1.optiondisplay()

    # print_heading('Dipan')

    while calc1.choice > 6:
        print("   -----------------------------")
        print("   | Invalid choice            |")
        print("   -----------------------------")
        calc1.optiondisplay()

    if calc1.choice != 6 and calc1.choice !=5:
        calc1.getinput()
    else:
        prev1.choice = calc1.choice

    while calc1.choice != 5:
        if calc1.choice == 1:
            print("\n")
            print("   -----------------------------")
            length1 = len(str(calc1.a)) + len(str(calc1.b)) + len(str(calc1.add()))
            print("   | " + str(calc1.a) + " + " + str(calc1.b) + " = " + str(calc1.add()) + " " * (20 - length1) + "|")
            print("   -----------------------------")
            prev1.choice = calc1.choice
            calc1.optiondisplay()
        elif calc1.choice == 2:
            print("\n")
            print("   -----------------------------")
            length1 = len(str(calc1.a)) + len(str(calc1.b)) + len(str(calc1.sub()))
            print("   | " + str(calc1.a) + " - " + str(calc1.b) + " = " + str(calc1.sub()) + " " * (20 - length1) + "|")
            print("   -----------------------------")
            prev1.choice = calc1.choice
            calc1.optiondisplay()
        elif calc1.choice == 3:
            print("\n")
            print("   -----------------------------")
            length1 = len(str(calc1.a)) + len(str(calc1.b)) + len(str(calc1.mul()))
            print("   | " + str(calc1.a) + " * " + str(calc1.b) + " = " + str(calc1.mul()) + " " * (20 - length1) + "|")
            print("   -----------------------------")
            prev1.choice = calc1.choice
            calc1.optiondisplay()
        elif calc1.choice == 4:
            print("\n")
            print("   -----------------------------")
            length1 = len(str(calc1.a)) + len(str(calc1.b)) + len(str(calc1.div()))
            print("   | " + str(calc1.a) + " / " + str(calc1.b) + " = " + str(calc1.div()) + " " * (20 - length1) + "|")
            print("   -----------------------------")
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
            print("   -----------------------------")
            print("   | Invalid choice            |")
            print("   -----------------------------")
            prev1.choice = calc1.choice
            calc1.optiondisplay()