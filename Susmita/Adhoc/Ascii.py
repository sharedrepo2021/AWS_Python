class Ascii:
    def __init__(self):
        self.a = None

    def get_inputs(self):
        self.a = input("Enter a letter: ")

    def asc(self):
        print("The Ascii of letter {} is {}".format(self.a, int(ord(self.a))))

    def upper(self):
        print("The Upper of letter  {} is  {}".format(self.a, self.a.upper()))


c1 = Ascii()

c1.get_inputs()
c1.asc()
c1.upper()



