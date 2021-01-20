import json
import pandas as pd
import os.path

class Addressbook:

    def __init__(self):
        self.entrydic = {"Name": "",
                         "Address": "",
                         "Phone": ""}
        self.f =""
    def getinputs(self):
        self.entrydic["Name"] = input("Enter name :")
        self.entrydic["Address"] = input("Enter Address ")
        self.entrydic["Phone"] = input("Enter phone number :")
    def printconfirm(self):
        print("name {} added".format(self.entrydic["Name"]))

    def createaddreesbook(self):
        if not os.path.exists("addressbook.json"):
          f = open("addressbook.json", "w+")
          print("addressbook created")

    if __name__ == '__main__':
        print("WELCOME TO ADDRESS BOOK")

        option_dict = {
            1: 'Show Address Book ',
            2: 'New Entry',
            3: 'Delete an Entry',
            4: 'Delete address book',
            5: 'Search for an Entry',
            6: 'Update an Entry',
            7: 'Exit'
        }

        print(json.dumps(option_dict, indent=4))
        option_dict1 = {
            1: 'address',
            2: 'phone',
            3: 'Exit'
        }
objadd=Addressbook()
objadd.createaddreesbook()
while True:
    choice = int(input("Select an option : "))
    if choice == 1:

        with open(r"addressbook.json") as f:
             if  os.stat("addressbook.json").st_size == 0:
                 print("Address book is empty")
             else:
                 print(f.read())
    elif choice == 2:
        objadd = Addressbook()
        objadd.getinputs()
        objadd.printconfirm()
        with open(r"addressbook.json", 'a') as f:
            json.dump(objadd.entrydic, f)
            f.write("\n")
    elif choice == 3:
        objadd = Addressbook()
        name = input("Enter name :")
        df = pd.read_json(r"addressbook.json", lines=True)
        if df.empty:
            print("Name not found ")
        else:
            dfrow = df[df['Name'].isin([name])]
            if dfrow.empty:
                print("Name not found")
            else:
                print("{}Entry deleted!".format(dfrow.shape[0]))
                dfrow = df[~df['Name'].isin([name])]
                dictsamp = dfrow.to_dict('records')
                with open(r"addressbook.json", 'w') as f:
                    for line in dictsamp:
                        f.write(json.dumps(line))
                        f.write("\n")
    elif choice == 4:
        with open(r"addressbook.json", "w") as f:
            print(f.write(""))
            print("Adrress book deleted")
    elif choice == 5:
        df = pd.read_json(r"addressbook.json", lines=True)
        name = input("Enter name :")
        if df.empty:
            print("Name not found")
        else:
            dfrow = df[df['Name'].isin([name])]
            if dfrow.empty:
                print("Name not found")
            else:
                dictnew = dfrow
                print(dictnew)
    elif choice == 6:

        df = pd.read_json(r"addressbook.json", lines=True)
        name = input("Enter  name :")
        address = input("Enter address:")
        if df.empty:
            print("Name not found")
        else:
            dfrow = df[df['Name'].isin([name]) & df['Address'].isin([address])]
            if dfrow.empty:
                print("Details not found")
            else:
                print("what do u want to update?")
                print("1: Phone no")
                print("2: Address")
                print("3: Both")
                opt = int(input("Select an option : "))
                index = df.index
                nameind = index[df['Name'] == name]
                lstind = nameind.tolist()
                intval = lstind[0]
                if opt == 1:
                    phone = input("Enter new phone no : ")
                    df.loc[intval, 'Phone'] = phone
                    dictsamp = df.to_dict('records')
                    with open(r"addressbook.json", 'w') as f:
                        for line in dictsamp:
                            f.write(json.dumps(line))
                            f.write("\n")
                            print("phone number updated")
                elif opt == 2:
                    address = input("Enter your new address: ")

                    df.loc[intval, 'Address'] = address
                    dictsamp = df.to_dict('records')
                    with open(r"addressbook.json", 'w') as f:
                        for line in dictsamp:
                            f.write(json.dumps(line))
                            f.write("\n")
                            print("Address updated")

                elif opt ==3 :
                    phone = input("Enter new phone no : ")
                    address = input("Enter your new address: ")
                    df.loc[intval, 'Address'] = address
                    df.loc[intval, 'Phone'] = phone
                    dictsamp = df.to_dict('records')
                    with open(r"addressbook.json", 'w') as f:
                        for line in dictsamp:
                            f.write(json.dumps(line))
                            f.write("\n")
                            print("phone number and address updated")
                else:
                     print("select a valid option")
    elif choice == 7:
     break
    else:
     print("Enter valid option ")


