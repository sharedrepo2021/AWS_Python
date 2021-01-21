import json as js
import pandas as pd


class Addressbook:

    def __init__(self):
        self.data = {}
        self.addr = {}
        self.jsfile = ''
        self.phone = ''
        self.dfaddr = ''
        self.addfnd = False

        self.addrbook = {
            "first_name": '',
            "last_name": '',
            "street_address": '',
            "city": '',
            "zip_code": '',
            "phone_no": ''
        }

    def disphead(self):
        print('\n============================')
        print('|    Select Your Option    |')
        print('============================\n')

    def getvalue(self):
        self.phone = input('Enter Phone  Number   : ')

    def getvalues(self):
        self.addrbook['first_name'] = input('Enter First  Name     : ')
        self.addrbook['last_name'] = input('Enter Last   Name     : ')
        self.addrbook['street_address'] = input('Enter Street Address  : ')
        self.addrbook['city'] = input('Enter City   Name     : ')
        self.addrbook['zip_code'] = input('Enter Zip    Code     : ')
        self.addrbook['phone_no'] = input('Enter Phone  Number   : ')

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
                print("Below the Address related with Phone Number!")
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
                print("Address related with Phone Number is successfully deleted!")
                print(js.dumps(self.addr, indent=2))
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
                print("Address related with Phone Number is successfully modified!")
                print(js.dumps(self.addr, indent=2))
                self.addr['first_name'] = self.addrbook['first_name']
                self.addr['last_name'] = self.addrbook['last_name']
                self.addr['street_address'] = self.addrbook['street_address']
                self.addr['city'] = self.addrbook['city']
                self.addr['zip_code'] = self.addrbook['zip_code']
                self.addr['phone_no'] = self.addrbook['phone_no']
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
        1: 'View the Address Book',
        2: 'Add a New Address to the Address Book',
        3: 'Search an Existing Address using Phone Number',
        4: 'Delete an Existing Address using Phone Number',
        5: 'Modify an Existing Address using Phone Number',
        6: 'Delete the Entire Address Book',
        0: 'Exit'
    }

    addbook = Addressbook()

    while True:
        addbook.disphead()
        print(js.dumps(address_option, indent=2))
        opt = input("Select Option: ")

        if opt == '1':
            addbook.readaddress()
            addbook.viewaddress()
        elif opt == '2':
            addbook.getvalues()
            addbook.addiaddress()
            addbook.readaddress()
        elif opt == '3':
            addbook.getvalue()
            addbook.srchaddress()
        elif opt == '4':
            addbook.getvalue()
            addbook.readaddress()
            addbook.deleaddress()
        elif opt == '5':
            addbook.getvalue()
            addbook.getvalues()
            addbook.readaddress()
            addbook.modiaddress()
        elif opt == '6':
            addbook.deleaddbook()
            break
        elif opt == '0':
            break
        else:
            print('An Invalid Option is Given. Please give correct option')
