import json as js
import pandas as pd


class Addressbook:

    def __init__(self):

        self.first = 0
        self.last = 0
        self.phone = 0
        self.telephone = 0
        self.addie = 0
        self.email = 0
        self.data = {}
        self.data['Information'] = []
        self.namedata = {}
        self.view = 0
        self.search = 0
        self.datafile = ' '
        self.fileview = ' '
        self.datadict = 0
        self.datalist = []

    def enter_contacts(self):

        self.first = input("First name ").capitalize()
        self.last = input("Last name ").capitalize()
        self.phone = input('Phone number')
        self.addie = input('Address').title()
        self.email = input('E-mail')
        self.data['Information'].append({
                "Name": self.first + " " + self.last,
                "Phone": self.phone,
                "Address": self.addie,
                "Email": self.email,
        })

        with open('address.json', 'w') as text_file:
            text_file.write("")

        with open('address.json', 'a') as text_file:
            js.dump(self.data, text_file, indent=4)
        print("The contact has been added to the  address book")

    def view_book(self):
        with open('address.json', 'r') as self.fileview:
            print(self.fileview.read())



    def search_book(self):
        self.data1 = pd.read_json('address.json')
        self.value = input('Enter the Name to search::::: ').title()
        self.data = pd.DataFrame(self.data1)

        for i in range(len(self.data['Information'])):
            if self.data['Information'][i]['Name'] == self.value:
                print("Name " + self.value + "  Found")
                print(js.dumps(self.data['Information'][i], indent=4))

    def changevalues(self):
        self.data2 = pd.read_json('address.json')
        self.namechange = input('Enter the name of the person:').title()
        change_addressbook = {
            1: 'Change Address',
            2: 'Change Email',
            3: 'Change Phone'
        }
        self.namefound = False
        for i in range(len(self.data2['Information'])):
            if self.data2['Information'][i]['Name'] == self.namechange:
                print(js.dumps(change_addressbook, indent=4))
                self.namefound = True
                self.namedata = self.data2['Information'][i]
                self.choi = input("Enter the options::::")
                if self.choi == "1":
                    self.addressdata = input("Enter the address to be changed:::")
                    self.namedata['Address'] = self.addressdata
                    print("Address updated for given name:::::", self.namedata)
                elif self.choi == "2":
                    self.emaildata = input("Enter the Email to be changed:::")
                    self.namedata['Email'] = self.emaildata
                    print("Email updated for given name:::", self.namedata)
                elif self.choi == "3":
                    self.phonedata = input("Enter the Phone to be changed:::")
                    self.namedata['Phone'] = self.phonedata
                    print("Phone updated for given name:::::", self.namedata)
                else:
                    print('Invalid Choice')
                self.data2['Information'][i] = self.namedata


        if self.namefound:
            df_dict = self.data2.to_dict(orient='list')
            with open(r"address.json", 'w') as f:
                js.dump(df_dict, f, indent=4)

    def deleteaddressbook(self):
        with open('address.json', 'w') as text_file:
            text_file.write("")

    def deletebasedname(self):
        self.data3 = pd.read_json('address.json')
        self.namechange1 = input('Enter the name of the person to delete:').title()
        self.namefound1 = False
        for i in range(len(self.data3['Information'])):
            if self.data3['Information'][i]['Name'] == self.namechange1:
                self.namefound1 = True
                self.dropdata = self.data3.drop(self.data3.index[i])

        if self.namefound1:
            df_dict1 = self.dropdata.to_dict(orient='list')
            with open(r"address.json", 'w') as f:
                js.dump(df_dict1, f, indent=4)
        else:
            print("Name not found")


if __name__ == '__main__':


    option_addressbook = {
        1: 'Enter a New contact in Book',
        2: 'View your Book',
        3: 'Search your Book',
        4: 'Change values in Book',
        5: 'Delete Entire AddressBook',
        6: 'Delete Based on Name',
        7: 'Exit'
    }

    objaddress = Addressbook()

    while True:
        print("***************************************")
        print("*************ADDRESS BOOK**************")
        print("***************************************")
        print(js.dumps(option_addressbook, indent=4))
        choice = input("Enter your choice: ")
        if choice == "1":
            objaddress.enter_contacts()
        elif choice == "2":
            objaddress.view_book()
        elif choice == "3":
            objaddress.search_book()
        elif choice == "4":
            objaddress.changevalues()
        elif choice == "5":
            objaddress.deleteaddressbook()
        elif choice == "6":
            objaddress.deletebasedname()
        elif choice == "7":
            break
        else:
            print("Invalid choice!! Give numbers specified in the options")
