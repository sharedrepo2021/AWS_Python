import json
import os
import pandas as pd
from tabulate import tabulate


class AddressBook:
    def __init__(self):
        self.book_dict = {
            "First_Name": '',
            "Last_Name": '',
            "email": '',
            "phone": '',
            "address": ''}

        self.df = None
        self.fo = None
        self.f1 = None
        self.choice = None
        self.matchedf = None
        self.srchkey = None
        self.srchkey1 = None
        self.srchkey2 = None
        self.addrfile = None
        self.searchfield = None
        self.searchfield1 = None
        self.searchfield2 = None
        self.final_output = None

    def getinput(self):
        self.book_dict['First_Name'] = input("\n Enter the First Name  : ")
        self.book_dict['Last_Name'] = input(" Enter the Last Name    : ")
        self.book_dict['email'] = input(" Enter the Email addr   : ")
        self.book_dict['phone'] = input(" Enter the Phone Number : ")
        self.book_dict['address'] = input(" Enter the Address      : ")


    def addcontact(self):

        if os.stat(self.addrfile).st_size == 0:
            feeds = []
        else:
            with open(self.addrfile) as feedsjs:
                feeds = json.load(feedsjs)

        feeds.append(self.book_dict)

        with open(self.addrfile, 'w') as f:
            f.write(json.dumps(feeds, indent=2))

    def deletebook(self):

        feeds = []

        with open(self.addrfile, 'w') as f:
            f.write(json.dumps(feeds, indent=2))

    def recoverbook(self):

        feeds = self.book_dict

        with open(self.addrfile, 'w') as f:
            f.write(json.dumps(feeds, indent=2))

    def createbook(self):

        feeds = []

        with open(self.addrfile, 'w') as f:
            f.write(json.dumps(feeds, indent=2))


    def bookoptions(self):
        print("\n")
        print("   ==============================================================")
        print("   ||                     MY ADDRESS BOOK                      ||")
        print("   ==============================================================")
        print("   |  1  | Add a Contact   |:::::|   S   |::::::::::::::::::::::|")
        print("   ------------------------------|   E   |                      |")
        print("   |  2  | Update Contact  |:::::|   A      By First Name  | 8  |")
        print("   ------------------------------|   R   |                      |")
        print("   |  3  | Remove Contact  |:::::|   C   |::::::::::::::::::::::|")
        print("   ------------------------------|   H   |                      |")
        print("   |  4  | Restore Contact |:::::|          By Last Name   | 9  |")
        print("   ------------------------------|       |                      |")
        print("   |  5  | Delete Book     |:::::|   B   |::::::::::::::::::::::|")
        print("   ------------------------------|   O   |                      |")
        print("   |  6  | Recover Book    |:::::|   O      By Phone Num   | 10 |")
        print("   ------------------------------|   k   |                      |")
        print("   |  7  | Show Contacts   |:::::|       |::::::::::::::::::::::|")
        print("   |============================================================|")
        print("   |::::::::::::::::::::| To Exit Press Zero |::::::::::::::::::|")
        print("   ==============================================================")
        print("\n")

        while True:
            try:
                self.choice = int(input("Choice : "))
                break
            except:
                print("\n !!! Not a Valid Input !!!")
        print("\n")

    def searchcontact(self):

        self.srchkey = input(" Enter the " + self.searchfield + " : ")
        if df.empty:
            self.final_output = "\n Address Book is Empty!!"
            self.fo = 0
        else:
            df_srchresult = df.loc[df[self.searchfield] == self.srchkey]
            if df_srchresult.empty:
                self.final_output = "\n No contact in Book with " + self.searchfield + " as " + self.srchkey
                self.fo = 0
            else:
                self.final_output = df_srchresult.iloc[:, 0:5]
                self.fo = 1

    def updatecontact(self):

        self.book_dict['First_Name'] = self.srchkey1
        self.book_dict['Last_Name'] = self.srchkey2
        self.book_dict['email'] = input(" Enter the New Email addr   : ")
        self.book_dict['phone'] = input(" Enter the New Phone Number : ")
        self.book_dict['address'] = input(" Enter the New Address      : ")
        self.addcontact()

    def deletecontact(self):

        df_aftdel = df.drop(self.matchedf.index)
        df_aftdel_dict = df_aftdel.to_dict(orient="records")
        with open(self.addrfile, 'w') as f:
            f.write(json.dumps(df_aftdel_dict, indent=2))

    def searchbylfname(self):

        newdf = df[(df[self.searchfield1] == self.srchkey1)]
        if newdf.empty:
            self.matchedf = newdf
            if self.f1 == 1:
                print("\n Contact " + self.srchkey1 + " not in Address Book")
        else:
            self.matchedf = (newdf.loc[newdf[self.searchfield2].isin([self.srchkey2])])
            if self.matchedf.empty:
                if self.f1 == 1:
                    print("\n Contact " + self.srchkey1 + " " + self.srchkey2 + " not in Address Book")
        return self.matchedf


if __name__ == '__main__':

    addr = AddressBook()

    masteraddrfile = r"addr_dbx.json"
    backupaddrfile = r"addr_dbx_bkp.json"
    addr.searchfield1 = 'First_Name'
    addr.searchfield2 = 'Last_Name'


    if not os.path.exists(masteraddrfile):
        addr.addrfile = masteraddrfile
        addr.createbook()

    if not os.path.exists(backupaddrfile):
        addr.addrfile = backupaddrfile
        addr.createbook()

    addr.bookoptions()

    while addr.choice != 0:
        if addr.choice == 1:
            df = pd.read_json(masteraddrfile)
            addr.searchfield = addr.searchfield1
            addr.searchcontact()
            if addr.fo == 0:
                print(addr.final_output)
            else:
                print(tabulate(addr.final_output, headers="keys", tablefmt='grid'))
        elif addr.choice == 2:
            df = pd.read_json(masteraddrfile)
            addr.searchfield = addr.searchfield2
            addr.searchcontact()
            if addr.fo == 0:
                print(addr.final_output)
            else:
                print(tabulate(addr.final_output, headers="keys", tablefmt='grid'))
        elif addr.choice == 3:
            df = pd.read_json(masteraddrfile)
            addr.searchfield = 'phone'
            addr.searchcontact()
            if addr.fo == 0:
                print(addr.final_output)
            else:
                print(tabulate(addr.final_output, headers="keys", tablefmt='grid'))
        elif addr.choice == 4:
            addr.getinput()
            df = pd.read_json(masteraddrfile)
            addr.srchkey1 = addr.book_dict[addr.searchfield1]
            addr.srchkey2 = addr.book_dict[addr.searchfield2]
            if not df.empty:
                addr.searchbylfname()
            else:
                addr.matchedf = df
            if addr.matchedf.empty:
                addr.addrfile = masteraddrfile
                addr.addcontact()
                print("\n Contact successfully added to Address Book!")
                addr.addrfile = backupaddrfile
                df = pd.read_json(backupaddrfile)
                if not df.empty:
                    addr.searchbylfname()
                else:
                    addr.matchedf = df
                if addr.matchedf.empty:
                    addr.addcontact()
                else:
                    addr.deletecontact()
                    addr.addcontact()
            else:
                print("\n Contact already exist")
        elif addr.choice == 5:
            df = pd.read_json(masteraddrfile)
            if df.empty:
                print("\n Address book is Empty")
            else:
                addr.srchkey1 = input("\n Enter the first Name : ")
                addr.srchkey2 = input(" Enter the Last Name  : ")
                addr.f1 = 1
                addr.searchbylfname()
                if addr.matchedf.empty:
                    pass
                else:
                    addr.addrfile = masteraddrfile
                    addr.deletecontact()
                    addr.updatecontact()
                    print("\n Contact successfully updated to Address Book!")
                    addr.addrfile = backupaddrfile
                    df = pd.read_json(backupaddrfile)
                    addr.searchbylfname()
                    if addr.matchedf.empty:
                        addr.addcontact()
                    else:
                        addr.deletecontact()
                        addr.addcontact()
        elif addr.choice == 6:
            df = pd.read_json(masteraddrfile)
            if df.empty:
                print("\n Address book is Empty")
            else:
                addr.srchkey1 = input("\n Enter the first Name : ")
                addr.srchkey2 = input(" Enter the Last Name  : ")
                addr.f1 = 1
                addr.searchbylfname()
                if addr.matchedf.empty:
                    pass
                else:
                    addr.addrfile = masteraddrfile
                    addr.deletecontact()
                    print("\n Contact deleted successfully!")
        elif addr.choice == 7:
            df = pd.read_json(masteraddrfile)
            addr.srchkey1 = input("\n Enter the first Name : ")
            addr.srchkey2 = input(" Enter the Last Name  : ")
            if df.empty:
                addr.matchedf = df
            else:
                addr.searchbylfname()
            if addr.matchedf.empty:
                df = pd.read_json(backupaddrfile)
                addr.f1 = 1
                addr.searchbylfname()
                if addr.matchedf.empty:
                    print("\n Contact not in Address Backup")
                else:
                    addr.addrfile = masteraddrfile
                    addr.book_dict = addr.matchedf.to_dict(orient="records")[0]
                    addr.addcontact()
                    print("\n Contact information restored successfully!")
            else:
                print("\n Contact already present in Address Book!")
        elif addr.choice == 8:
            addr.addrfile = masteraddrfile
            addr.deletebook()
            print("\n All Contacts Erased !!")
        elif addr.choice == 9:
            addr.addrfile = masteraddrfile
            df = pd.read_json(backupaddrfile)
            addr.book_dict = df.to_dict(orient="records")
            addr.recoverbook()
            print("\n Address Book Restored!")
        elif addr.choice == 10:
            df_all = pd.read_json(masteraddrfile)
            tot_rows = len(df_all.index)
            print(tabulate(df_all, headers="keys", tablefmt='grid'))
            print("\n Total number of contacts in the book : " + str(tot_rows))
        addr.bookoptions()
        addr.f1 = 0
