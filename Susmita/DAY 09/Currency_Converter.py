from currency_converter import CurrencyConverter
from tkinter import *


root = Tk()
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
    root.configure(background='yellow')
    root.geometry("400x175")
    headlabel = Label(root, text='welcome to Currency Convertor',
                      fg='black', bg="red")

    # Create a "Amount :" label
    label1 = Label(root, text="Amount:",
                   fg='black', bg='dark green')

    # Create a "From Currency :" label
    # label2 = Label(root, text="From Currency",
    #                fg='black', bg='dark green')

    # Create a "To Currency: " label
    # label3 = Label(root, text="To Currency :",
    #                fg='black', bg='dark green')

    # Create a "Converted Amount :" label
    label4 = Label(root, text="Converted Amount :",
                   fg='black', bg='dark green')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 1, column = 0)
    # label2.grid(row = 2, column = 0)
    # label3.grid(row = 3, column = 0)
    label4.grid(row = 5, column = 0)

    # Create a text entry box
    # for filling or typing the information.
    Amount1_field = Entry(root)
    Amount2_field = Entry(root)

    # ipadx keyword argument set width of entry space.
    Amount1_field.grid(row=1, column=1, ipadx="25")
    Amount2_field.grid(row=5, column=1, ipadx="25")
    CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

    # create a drop down menu using OptionMenu function
    # which takes window name, variable and choices as
    # an argument. use * befor the name of the list,
    # to unpack the values
    FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list)
    ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list)

    FromCurrency_option.grid(row=2, column=1, ipadx=10)
    ToCurrency_option.grid(row=3, column=1, ipadx=10)

    # Create a Convert Button and attached
    # with RealTimeCurrencyExchangeRate function
    button1 = Button(root, text="Convert", bg="red", fg="black",
                     command=RealTimeCurrencyConversion)

    button1.grid(row=4, column=1)

    # Create a Clear Button and attached
    # with delete function
    button2 = Button(root, text="Clear", bg="red",
                     fg="black", command=clear_all)
    button2.grid(row=6, column=1)
    root.mainloop()
    p = Currency()
    p.get_input()
    p.convert()