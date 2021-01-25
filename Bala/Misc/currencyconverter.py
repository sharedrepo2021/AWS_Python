import ccy
import tkinter as tk

from currency_converter import CurrencyConverter
from tkinter import *
from tkinter import ttk


class CurrConvert:

    def __init__(self):
        self.window = tk.Tk()
        self.listcurr = list(ccy.all())
        self.currconv = CurrencyConverter()

        self.given_value = 1.0
        self.convert_value = 1.0
        self.defamt0 = StringVar(self.window, value='0')
        self.defamt1 = StringVar(self.window, value='1')
        self.from_curr = ''
        self.to_curr = ''

    def buildUI(self):
        self.window.title = 'Currency Converter'
        self.window.geometry("750x250")
        self.window.config(background="grey")

        self.window.label = Label(self.window, text='Currency Convertor', fg='green', bg='grey',
                                  borderwidth=3)
        self.window.label.config(font=('Verdana', 15, 'bold', ))
        self.window.label.place(x=270, y=30)

        self.window.amt = Entry(self.window, bd=3, justify=tk.CENTER, textvariable=self.defamt1)
        self.window.convamt = Entry(self.window, bd=3, justify=tk.CENTER, textvariable=self.defamt0)

        self.window.frmcurr = StringVar(self.window)
        self.window.frmcurr.set('USD')
        self.window.tocurr = StringVar(self.window)
        self.window.tocurr.set('INR')


        font = ("Courier", 12, "bold")
        self.window.frmcurr_dropdown = ttk.Combobox(self.window, textvariable=self.window.frmcurr,
                                                    values=self.listcurr, font=font, state='readonly',
                                                    width=5, justify=tk.CENTER)
        self.window.tocurr_dropdown = ttk.Combobox(self.window, textvariable=self.window.tocurr,
                                                   values=self.listcurr, font=font, state='readonly',
                                                   width=5, justify=tk.CENTER)

        self.window.amt.place(x=100, y=90)
        self.window.frmcurr_dropdown.place(x=230, y=90)
        self.window.convamt.place(x=100, y=130)
        self.window.tocurr_dropdown.place(x=230, y=130)

        self.window.convbutton = Button(self.window, text="Convert", fg="black",
                                        command=self.conversion)
        self.window.convbutton.config(font=('Courier', 10, 'bold'))
        self.window.convbutton.place(x=310, y=110)

        self.window.mainloop()

    def conversion(self):
        self.window.convamt.delete(0, END)
        self.window.label = Label(self.window, text='                                     ',
                                  fg='red', bg='grey', borderwidth=3)
        self.window.label.config(font=('Verdana', 15, 'bold',))
        self.window.label.place(x=270, y=200)

        self.given_value = float(self.window.amt.get())
        self.from_curr = self.window.frmcurr.get()
        self.to_curr = self.window.tocurr.get()

        try:
            self.convert_value = self.currconv.convert(self.given_value, self.from_curr, self.to_curr)
        except Exception as exp:
            self.window.label = Label(self.window, text='No Currency Found', fg='red', bg='grey',
                                      borderwidth=3)
            self.window.label.config(font=('Verdana', 15, 'bold',))
            self.window.label.place(x=270, y=200)
            self.window.convamt.delete(0, END)

        self.window.convamt.insert(0, str(self.convert_value))

if __name__ == '__main__':
    currconv = CurrConvert()
    currconv.buildUI()
