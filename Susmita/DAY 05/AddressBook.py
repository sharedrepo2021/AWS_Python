import json
import pandas as pd


class Entry:
    def __init__(self):
        self.entry_dict = {
            "Name": '',
            "Address": '',
            "Phone": ''}

    def get_inputs(self):
        self.entry_dict["Name"] = input("Enter name : ")
        self.entry_dict["Address"] = input("Enter address: ")
        self.entry_dict["Phone"] = input("Enter phone number: ")

    def print_confirmation(self):
        print("{} name added".format(self.entry_dict["Name"]))


if __name__ == '__main__':
    print("WELCOME TO ADDRESSBOOK")

    address_option_dict = {
        1: 'Exit',
        2: 'Display all entries',
        3: 'Add a new entry',
        4: 'Delete an entry',
        5: 'Search for an entry',
        6: 'Update an entry',
        7: 'Delete address book',
    }

    print(json.dumps(address_option_dict, indent=4))

    while True:
        i = int(input("Select a main menu option : "))

        if i == 1:
            break

        elif i == 2:
            with open(r"AddressBook.json") as f:
                print(f.read())

        elif i == 3:
            v = Entry()
            v.get_inputs()
            v.print_confirmation()
            with open(r"AddressBook.json", 'a') as f:
                json.dump(v.entry_dict, f)
                f.write("\n")

        elif i == 4:
            ename = input("Enter the name : ")
            df = pd.read_json(r"AddressBook.json", lines=True)
            df_row = df[df['Name'].isin([ename])]
            if df_row.empty:
                print('Entry not found!')
            else:
                print("{} entries deleted !".format(df_row.shape[0]))
                df_row = df[~df['Name'].isin([ename])]
                df_dict = df_row.to_dict(orient='records')
                with open(r"AddressBook.json", 'w') as f:
                    for line in df_dict:
                        f.write(json.dumps(line))
                        f.write("\n")

        elif i == 5:
            ename = input("Enter the name : ")
            df = pd.read_json(r"AddressBook.json", lines=True)
            df_row = df[df['Name'].isin([ename])]
            if df_row.empty:
                print('Address not found!')
            else:
                print("Match found :")
                print(df_row)

        elif i == 6:
            ename = input("Enter the name : ")
            df = pd.read_json(r"AddressBook.json", lines=True)
            df_row = df[df['Name'].isin([ename])]
            if df_row.empty:
                print('Address not found!')
            else:
                print("Match found :")
                print(df_row)

        elif i == 7:
            with open(r"AddressBook.json", 'w') as f:
                f.write("")
