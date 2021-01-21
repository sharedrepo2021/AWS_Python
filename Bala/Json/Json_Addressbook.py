import json as js
import pandas as pd
from tkinter import *
from tkinter import filedialog

class Addressbook:

    def __init__(self):
        self.fname = ''
        self.data = {}
        self.addr = {}
        self.jsfile = ''
        self.phone = ''
        self.dfaddr = ''
        self.addfnd = False
        self.window = Tk()

        self.addrbook = {
            "first_name": '',
            "last_name": '',
            "street_address": '',
            "city": '',
            "zip_code": '',
            "phone_no": ''
        }

    def disphead(self):
        print('\n=============================================')
        print('|    Select Your Option                        |')
        print('===============================================\n')

    def browsefile(self):
        self.fname = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("json files",
                                                          "*.json*"),
                                                         ("All files",
                                                          "*.*")))

    def getfilename(self):
        # Set window title
        self.window.title('File Explorer')

        # Set window size
        self.window.geometry("500x500")

        # Set window background color
        self.window.config(background="white")


        # Create a File Explorer label
        label_file_explorer = Label(self.window,
                                    text="File Explorer using Tkinter",
                                    width=100, height=4,
                                    fg="blue")

        button_explore = Button(self.window,
                                text="Browse Files",
                                command=self.browsefile())

        print(self.fname)

        # button_exit = Button(self.window,
        #                      text="Exit",
        #                      command=self.window.destroy)

        # Grid method is chosen for placing
        # the widgets at respective positions
        # in a table like structure by
        # specifying rows and columns
        label_file_explorer.grid(column=1, row=1)

        button_explore.grid(column=1, row=2)

        # button_exit.grid(column=1, row=3)

        # Let the window wait for any events
        self.window.mainloop()


    def getvalue(self):
        self.phone = input('Enter Phone  Number   : ')

    def getvalues(self):
        self.addrbook['first_name'] = input('Enter First  Name     : ')
        self.addrbook['last_name'] = input('Enter Last   Name     : ')
        self.addrbook['street_address'] = input('Enter Street Address  : ')
        self.addrbook['city'] = input('Enter City   Name     : ')
        self.addrbook['zip_code'] = input('Enter Zip    Code     : ')
        self.addrbook['phone_no'] = input('Enter Phone  Number   : ')
        self.phone = self.addrbook['phone_no']

    def modvalues(self):
        self.addrbook['first_name'] = input('Enter First  Name     : ')
        self.addrbook['last_name'] = input('Enter Last   Name     : ')
        self.addrbook['street_address'] = input('Enter Street Address  : ')
        self.addrbook['city'] = input('Enter City   Name     : ')
        self.addrbook['zip_code'] = input('Enter Zip    Code     : ')

    def readaddress(self):
        with open('address_book.json', 'r') as self.jsfile:
            self.data = js.load(self.jsfile)

    def viewaddress(self):
        print(js.dumps(self.data, indent=2))

    def addiaddress(self):
        self.data["Addressbook"].append(self.addrbook)
        with open('address_book.json', 'w') as self.jsfile:
            js.dump(self.data, self.jsfile, indent=2)

    def srchaddress(self):
        self.dfaddr = pd.read_json('address_book.json')
        df_dict = self.dfaddr.to_dict()
        for i in range(len(df_dict["Addressbook"])):
            self.addrbook = df_dict["Addressbook"][i]
            if self.addrbook["phone_no"] == self.phone:
                print("The Address is: ")
                print(js.dumps(self.addrbook, indent=2))
                self.addfnd = True
                break
            else:
                self.addfnd = False

        if self.addfnd:
            pass
        else:
            print('Phone Number not found in the Addressbook!')

    def deleaddress(self):
        for self.addr in self.data["Addressbook"]:
            if self.addr['phone_no'] == self.phone:
                print("Address is successfully deleted!")
                self.data["Addressbook"].remove(self.addr)
                self.addfnd = True
                break
            else:
                self.addfnd = False

        if self.addfnd:
            with open('address_book.json', 'w') as self.jsfile:
                js.dump(self.data, self.jsfile, indent=2)
        else:
            print('Phone Number not found in the Addressbook!')

    def modiaddress(self):
        for self.addr in self.data["Addressbook"]:
            if self.addr['phone_no'] == self.phone:
                print("Address is successfully modified!")
                self.addr['first_name'] = self.addrbook['first_name']
                self.addr['last_name'] = self.addrbook['last_name']
                self.addr['street_address'] = self.addrbook['street_address']
                self.addr['city'] = self.addrbook['city']
                self.addr['zip_code'] = self.addrbook['zip_code']
                self.addr['phone_no'] = self.phone
                self.addfnd = True
                break
            else:
                self.addfnd = False

        if self.addfnd:
            with open('address_book.json', 'w') as self.jsfile:
                js.dump(self.data, self.jsfile, indent=2)
        else:
            print('Phone Number not found in the Addressbook!')

    def deleaddbook(self):
        with open('address_book.json', 'w') as self.jsfile:
            self.jsfile.write("")
        print('Entire Address Book is Cleared !!! ')


if __name__ == '__main__':

    address_option = {
        1: 'Open the json file',
        2: 'View the Address Book',
        3: 'Add a New Address to the Address Book',
        4: 'Search an Existing Address using Phone Number',
        5: 'Delete an Existing Address using Phone Number',
        6: 'Modify an Existing Address using Phone Number',
        7: 'Delete the Entire Address Book',
        0: 'Exit'
    }

    addbook = Addressbook()

    while True:
        addbook.disphead()
        print(js.dumps(address_option, indent=2))
        opt = input("Select Option: ")

        if opt == '1':
            try:
                addbook.getfilename()
            except Exception as e:
                continue

        if opt == '2':
            try:
                addbook.readaddress()
                addbook.viewaddress()
            except js.decoder.JSONDecodeError as e:
                print("File doesn't have any contents!!!!")
                break
        elif opt == '3':
            try:
                addbook.getvalues()
                addbook.readaddress()
                addbook.addiaddress()
            except KeyError as e:
                print("File doesn't have any contents!!!!")
                break
        elif opt == '4':
            try:
                addbook.getvalue()
                addbook.srchaddress()
            except ValueError as e:
                print("File doesn't have any contents!!!!")
                break
        elif opt == '5':
            try:
                addbook.getvalue()
                addbook.readaddress()
                addbook.deleaddress()
            except js.decoder.JSONDecodeError as e:
                print("File doesn't have any contents!!!!")
                break
        elif opt == '6':
            try:
                addbook.getvalue()
                addbook.modvalues()
                addbook.readaddress()
                addbook.modiaddress()
            except js.decoder.JSONDecodeError as e:
                print("File doesn't have any contents!!!!")
                break
        elif opt == '7':
            addbook.deleaddbook()
        elif opt == '0':
            break
        else:
            print('An Invalid Option is Given. Please give correct option')
