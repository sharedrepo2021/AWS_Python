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
        self.view = 0
        self.search = 0
        self.datafile = ' '
        self.fileview = ' '


    def enter_contacts(self):
        self.name = input("Enter the name of the address book to add contact") + ".json"
        self.first = input("First name ").capitalize()
        self.last = input("Last name ").capitalize()
        self.phone = input('Phone number ')
        if len(self.phone) == 10 and self.phone.isnumeric():
            self.telephone = "(" + self.phone[0:3] + ")" + " " + self.phone[3:6] + "-" + self.phone[6:10]
        else:
            self.telephone = "Only numerals are accepted in this field"
        self.addie = input('Address').title()
        self.email = input('E-mail')
        self.data['Information'].append({
                "Name": self.first + " " + self.last,
                "Phone": self.phone,
                "Address": self.addie,
                "Email": self.email,
        })
        with open(self.name, 'w') as text_file:
            js.dump(self.data, text_file)
        print("The contact has been added to the  address book", self.data)

    def view_book(self):
        self.view = input("Enter the name of the address book to view") + ".json"
        with open(self.view, 'r') as self.fileview:
            self.data = js.load(self.fileview)
        print(js.dumps(self.data, indent=5))


    def search_book(self):
        self.search = input("Enter the name of the address book to search") + ".json"
        self.data1 = pd.read_json(self.search)
        self.value = input('Enter the Name to search: ').title()
        self.data = pd.DataFrame(self.data1)

        for i in range(len(self.data['Information'])):
            if self.data['Information'][i]['Name'] == self.value:
                print("Name " + self.value + "  Found")
                print(self.data['Information'][i])

    def changevalues(self):
        self.change = input("Enter the name of the address book to make changes") + ".json"
        self.data2 = pd.read_json(self.change)
        change_addressbook = {
            1: 'Change Address',
            2: 'Change Email',
            3: 'Change Phone',
            4: 'Exit'
        }
        print(js.dumps(change_addressbook, indent=4))
        self.namefound = False
        self.namechange = input('Enter the name of the person').title()
        for i in range(len(self.data2['Information'])):
            if self.data2['Information'][i]['Name'] == self.namechange:
                self.namedata = self.data2['Information'][i]
                self.choi = input('Enter the options')
                if self.choi == "1":
                    self.addressdata = input("Enter the address to be changed")
                    self.namedata['Address'] = [self.addressdata]
                    print("Address updated for given name", self.namedata)
                if self.choi == "2":
                    self.emaildata = input("Enter the Email to be changed")
                    self.namedata['Email'] = [self.emaildata]
                    print("Email updated for given name", self.namedata)
                if self.choi == "3":
                    self.phonedata = input("Enter the Phone to be changed")
                    self.namedata['Phone'] = [self.self.phonedata]
                    print("Phone updated for given name", self.namedata)
            with open(self.change, 'w') as texfile:
                js.dump(self.namedata, texfile, indent=5)
            self.namefound = True
        if self.namefound == False:
            print("Name not found")


if __name__ == '__main__':
    option_addressbook = {
        1: 'Enter a New contact in Book',
        2: 'View your Book',
        3: 'Search your Book',
        4: 'Change values in Book',
        5: 'Exit'
    }
    print(js.dumps(option_addressbook, indent=4))

    objaddress = Addressbook()

    while True:
        choice = input("Enter your choice")
        if choice == "1":
            objaddress.enter_contacts()
        elif choice == "2":
            objaddress.view_book()
        elif choice == "3":
            objaddress.search_book()
        elif choice == "4":
            objaddress.changevalues()
        elif choice == "5":
            break
        else:
            print("Invalid choice!! Give numbers specified in the options")
