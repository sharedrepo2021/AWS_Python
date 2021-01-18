import json
import pandas as pd


class Items:
    def __init__(self):
        self.a = None

    def get_inputs(self):
        self.a = input("Enter a letter: ")


class Vendor:
    def __init__(self):
        self.vendor_dict = {
            "Name": '',
            "Address": '',
            "Phone": ''}

    def get_inputs(self):
        self.vendor_dict["Name"] = input("Enter Vendor name : ")
        self.vendor_dict["Address"] = input("Enter Vendor address: ")
        self.vendor_dict["Phone"] = input("Enter Vendor phone number: ")

    def print_confirmation(self):
        print("Vendor name {} added".format(self.vendor_dict["Name"]))


class Customer:
    pass


class Employee:
    pass


option_dict = {
    1: 'Exit',
    2: 'Vendor menu',
    3: 'Employee menu',
    4: 'Item menu',
    5: 'Customer menu'
}

vendor_option_dict = {
    1: 'Exit',
    2: 'Display all vendors',
    3: 'Enter Vendor details',
    4: 'Delete all Vendor information',
    5: 'Search for a vendor'
}

print(json.dumps(option_dict, indent=4))

if __name__ == '__main__':
    while True:
        i = int(input("Select a main menu option : "))
        if i == 1:
            break
        if i == 2:
            while True:
                print(json.dumps(vendor_option_dict, indent=4))
                j = int(input("Select a vendor menu option : "))
                if j == 1:
                    print("Welcome back to main menu.....")
                    break
                elif j == 2:
                    with open(r"E:\Study\Python\Data\Whole_seller.jsonl") as f:
                        print(f.read())
                elif j == 3:
                    v = Vendor()
                    v.get_inputs()
                    v.print_confirmation()
                    with open(r"E:\Study\Python\Data\Whole_seller.jsonl", 'a') as f:
                        json.dump(v.vendor_dict, f)
                        f.write("\n")
                elif j == 4:
                    with open(r"E:\Study\Python\Data\Whole_seller.jsonl", 'w') as f:
                        f.write("")
                elif j == 5:
                    vname = input("Enter the name of the Vendor :      ")
                    df = pd.read_json(path_or_buf=r"E:\Study\Python\Data\Whole_seller.jsonl", lines=True)
                    df = df.loc[df['Name'] == vname]
                    if df.empty:
                        print('Vendor not found!')
                    else:
                        print("Match found :")
                        print(df)




