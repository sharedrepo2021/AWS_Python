from currency_converter import CurrencyConverter


class Currency:
    def __init__(self):
        self.curr1 = None
        self.curr2 = None
        self.amount = None

    def get_input(self):
        self.curr1 = input("Enter your currency code:: ")
        self.curr2 = input("Enter the currency code you want to convert:: ")
        self.amount = int(input("Enter the amount of money:: "))

    def convert(self):
        c = CurrencyConverter()
        print(c.convert(self.amount, self.curr1, self.curr2))


if __name__ == '__main__':
    p = Currency()
    p.get_input()
    p.convert()