class Calculator:
    def __init__(self):
        self.a = None
        self.b = None

    def get_inputs(self):
        self.a = int(input("Enter 1st number: "))
        self.b = int(input("Enter 2nd number: "))

    def sum(self):
        print("The sum of {} and {} is : {}".format(self.a, self.b, self.a + self.b))

    def subtract(self):
        print("The difference of {} and {} is : {}".format(self.a, self.b, self.a - self.b))

    def multiply(self):
        print("The product of {} and {} is : {}".format(self.a, self.b, self.a * self.b))

    def division(self):
        print("The division of {} and {} is : {}".format(self.a, self.b, self.a / self.b))

    def remainder(self):
        print("The remainder of {} and {} is : {}".format(self.a, self.b, self.a % self.b))


c1 = Calculator()

c1.get_inputs()
c1.sum()
c1.subtract()
c1.multiply()
c1.division()
c1.remainder()


