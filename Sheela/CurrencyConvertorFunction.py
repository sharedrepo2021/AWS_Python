import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class CurrencyConverter():
    def __init__(self,url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        self.initial_amount = amount

        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class CurrencyConverterUI(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        self.geometry("600x300")

        self.intro_label = Label(self, text='Welcome to Currency Convertor', fg='blue', relief=tk.RAISED,
                                 borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.intro_label.place(x=50, y=60)

        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER)
        self.converted_amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER)

        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("Choose From Currency")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("Choose To Currency")  # default value

        font = ("Courier", 12, "bold")

        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.currency_converter.currencies.keys()), font=font,
                                                   state='readonly', width=20, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.currencies.keys()), font=font,
                                                 state='readonly', width=20, justify=tk.CENTER)

        self.from_currency_dropdown.place(x=20, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=300, y=120)
        self.converted_amount_field.place(x=346, y=150)

        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=230, y=150)

        self.clearbutton = Button(self, text="Clear", fg="black", command=self.clearall)
        self.clearbutton.config(font=('Courier', 10, 'bold'))
        self.clearbutton.place(x=230, y=200)


    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field.insert(0, str(converted_amount))

       # self.converted_amount_field.config(text=str(converted_amount))

    def clearall(self):
        self.amount_field.delete(0, END)
        self.converted_amount_field.delete(0, END)


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    CurrencyConverterUI(converter)
    mainloop()