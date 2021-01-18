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
        self.srchfld = None
        self.srchfld1 = None
        self.srchfld2 = None
        self.final_ou = None

    def getinput(self):
        self.book_dict = dict()
        self.book_dict['First_Name'] = input(" Enter the First Name   : ")
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

    def recoverbook(self):

        feeds = self.book_dict

        with open(self.addrfile, 'w') as f:
            f.write(json.dumps(feeds, indent=2))

    def createnewbook(self):

        feeds = []

        with open(self.addrfile, 'w') as f:
            f.write(json.dumps(feeds, indent=2))

    def bookoptions(self):
        print("\n")
        print("   ====================================================================")
        print("   |:::::|                    MY ADDRESS BOOK                    |::::|")
        print("   ====================================================================")
        print("   |  M  |  1  | Add a Contact   |:::::|       |::::::::::::::::::::::|")
        print("   |  A  |-----------------------------|   S   |                      |")
        print("   |  I  |  2  | Update Contact  |:::::|   E      By First Name  | 08 |")
        print("   |  N  |-----------------------------|   A   |                      |")
        print("   |  T  |  3  | Remove Contact  |:::::|   R   |::::::::::::::::::::::|")
        print("   |  A  |-----------------------------|   C   |                      |")
        print("   |  I  |  4  | Restore Contact |:::::|   H      By Last Name   | 09 |")
        print("   |  N  |-----------------------------|       |                      |")
        print("   |     |  5  | Delete Book     |:::::|   B   |::::::::::::::::::::::|")
        print("   |  B  |-----------------------------|   O   |                      |")
        print("   |  O  |  6  | Recover Book    |:::::|   O      By Phone Num   | 10 |")
        print("   |  O  |-----------------------------|   K   |                      |")
        print("   |  K  |  7  | Show Contacts   |:::::|       |::::::::::::::::::::::|")
        print("   |==================================================================|")
        print("   |::::::::::::::::::::::: Press ZERO to EXIT :::::::::::::::::::::::|")
        print("   ====================================================================")
        print("\n")

        while True:
            try:
                self.choice = int(input("Choice : "))
                break
            except:
                print("\n !!!INVALID CHOICE. PLEASE TRY AGAIN!!!\n")
        print("\n")

    def searchcontact(self):

        self.srchkey = input(" Enter the " + self.srchfld + " : ")
        if df.empty:
            self.final_ou = "\n ADDRESS BOOK IS EMPTY!!"
            self.fo = 0
        else:
            df_srchresult = df.loc[df[self.srchfld] == self.srchkey]
            if df_srchresult.empty:
                self.final_ou = "\n NO CONTACT IN BOOK " + self.srchfld + " AS " + self.srchkey
                self.fo = 0
            else:
                self.final_ou = df_srchresult.iloc[:, 0:5]
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

        newdf = df[(df[self.srchfld1] == self.srchkey1)]
        if newdf.empty:
            self.matchedf = newdf
            if self.f1 == 1:
                print("\n CONTACT " + self.srchkey1 + " NOT IN ADDRESS BOOK!")
        else:
            self.matchedf = (newdf.loc[newdf[self.srchfld2].isin([self.srchkey2])])
            if self.matchedf.empty:
                if self.f1 == 1:
                    print("\n CONTACT " + self.srchkey1 + " " + self.srchkey2 + " NOT IN ADDRESS BOOK!")
        return self.matchedf


if __name__ == '__main__':

    addr = AddressBook()

    mstr_file = r"myaddr_mstr_db.json"
    bkp_file = r"myaddr_bkp_db.json"
    addr.srchfld1 = 'First_Name'
    addr.srchfld2 = 'Last_Name'

    if not os.path.exists(mstr_file):
        addr.addrfile = mstr_file
        addr.createnewbook()

    if not os.path.exists(bkp_file):
        addr.addrfile = bkp_file
        addr.createnewbook()

    addr.bookoptions()

    while addr.choice != 0:
        df = pd.read_json(mstr_file)
        if addr.choice == 1:
            addr.getinput()
            addr.srchkey1 = addr.book_dict[addr.srchfld1]
            addr.srchkey2 = addr.book_dict[addr.srchfld2]
            if not df.empty:
                addr.searchbylfname()
            else:
                addr.matchedf = df
            if addr.matchedf.empty:
                addr.addrfile = mstr_file
                addr.addcontact()
                print("\n CONTACT ADDED TO ADDRESS BOOK!")
                addr.addrfile = bkp_file
                df = pd.read_json(bkp_file)
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
                print("\n CONTACT ALREADY EXIST!")
        elif addr.choice == 2:
            df = pd.read_json(mstr_file)
            if df.empty:
                print("\n ADDRESS BOOK IS EMPTY! ")
            else:
                addr.srchkey1 = input("\n Enter the first Name : ")
                addr.srchkey2 = input(" Enter the Last Name  : ")
                addr.f1 = 1
                addr.searchbylfname()
                if addr.matchedf.empty:
                    pass
                else:
                    addr.addrfile = mstr_file
                    addr.deletecontact()
                    addr.updatecontact()
                    print("\n CONTACT UPDATED TO ADDRESS BOOK!!")
                    addr.addrfile = bkp_file
                    df = pd.read_json(bkp_file)
                    addr.searchbylfname()
                    if addr.matchedf.empty:
                        addr.addcontact()
                    else:
                        addr.deletecontact()
                        addr.addcontact()
        elif addr.choice == 3:
            if df.empty:
                print("\n ADDRESS BOOK IS EMPTY! ")
            else:
                addr.srchkey1 = input("\n Enter the first Name : ")
                addr.srchkey2 = input(" Enter the Last Name  : ")
                addr.f1 = 1
                addr.searchbylfname()
                if addr.matchedf.empty:
                    pass
                else:
                    addr.addrfile = mstr_file
                    addr.deletecontact()
                    print("\n CONTACT REMOVED FROM BOOK!!")
        elif addr.choice == 4:
            addr.srchkey1 = input("\n Enter the first Name : ")
            addr.srchkey2 = input(" Enter the Last Name  : ")
            if df.empty:
                addr.matchedf = df
            else:
                addr.searchbylfname()
            if addr.matchedf.empty:
                df = pd.read_json(bkp_file)
                addr.f1 = 1
                if df.empty:
                    addr.matchedf = df
                else:
                    addr.searchbylfname()
                if addr.matchedf.empty:
                    print("\n CONTACT NOT IN ADDRESS BACKUP!")
                else:
                    addr.addrfile = mstr_file
                    addr.book_dict = addr.matchedf.to_dict(orient="records")[0]
                    addr.addcontact()
                    print("\n CONTACT INFORMATION RESTORED!")
            else:
                print("\n CONTACT ALREADY EXIST IN ADDRESS BOOK!")
        elif addr.choice == 5:
            addr.addrfile = mstr_file
            addr.createnewbook()
            print("\n ALL CONTACTS ERASED !!")
        elif addr.choice == 6:
            addr.addrfile = mstr_file
            df = pd.read_json(bkp_file)
            addr.book_dict = df.to_dict(orient="records")
            addr.recoverbook()
            print("\n ADDRESS BOOK RESTORED!")
        elif addr.choice == 7:
            tot_rows = len(df.index)
            print(tabulate(df, headers="keys", tablefmt='grid'))
            print("\n TOTAL CONTACTS IN BOOK : " + str(tot_rows))
        elif addr.choice == 8:
            addr.srchfld = addr.srchfld1
            addr.searchcontact()
            if addr.fo == 0:
                print(addr.final_ou)
            else:
                print(tabulate(addr.final_ou, headers="keys", tablefmt='grid'))
        elif addr.choice == 9:
            addr.srchfld = addr.srchfld2
            addr.searchcontact()
            if addr.fo == 0:
                print(addr.final_ou)
            else:
                print(tabulate(addr.final_ou, headers="keys", tablefmt='grid'))
        elif addr.choice == 10:
            addr.srchfld = 'phone'
            addr.searchcontact()
            if addr.fo == 0:
                print(addr.final_ou)
            else:
                print(tabulate(addr.final_ou, headers="keys", tablefmt='grid'))
        addr.bookoptions()
        addr.f1 = 0