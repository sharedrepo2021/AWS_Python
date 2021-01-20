import pyodbc
import pandas as pd
import faker
import json as js
import random
from tabulate import tabulate
import re



class AddressbookTable:
    def __init__(self):
        self.cursor = None
        self.fake = faker.Faker()
        self.conn = None



    def sqlconnection(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=BALALENG50\SQLEXPRESS;'
                              'Database=ADDRESSBOOK;'
                              'Trusted_Connection=yes;')

        self.cursor = self.conn.cursor()
        print("CONNECTION ESTABLISHED")

    def createtable(self):
        createquery = '''
                        if not exists (select * from sys.sysobjects where name='PersonalInfo' and xtype='U')
                            CREATE TABLE ADDRESSBOOK.Address_Info.PersonalInfo(
                                PersonID int NOT NULL,
                                FirstName nvarchar(50) NOT NULL,
                                LastName nvarchar(50) NOT NULL,
                                Address nvarchar(100),
                                PhoneNum nvarchar(30) NOT NULL,
                                EmailID nvarchar(50) NOT NULL
                            );
                        '''
        self.cursor.execute(createquery)
        print("TABLE CREATED SUCCESSFULLY")

    def populatedata(self):
            uniqueid = random.randrange(1, 1000)
            firstname = self.fake.first_name().upper()
            lastname = self.fake.last_name().upper()
            address = self.fake.address().upper()
            phonenum = self.fake.phone_number()
            emailid = self.fake.email()
            populatequery = "INSERT INTO ADDRESSBOOK.Address_Info.PersonalInfo VALUES('{}', '{}', '{}', '{}', '{}', '{}')" \
                            "".format(uniqueid, firstname, lastname, address, phonenum, emailid)
            self.cursor.execute(populatequery)

    def viewaddress(self):
        viewquery = "SELECT * FROM ADDRESSBOOK.Address_Info.PersonalInfo ORDER BY PersonID"
        df1 = pd.read_sql_query(viewquery, self.conn)
        view = pd.DataFrame(df1)
        print(tabulate(view, headers='keys', tablefmt='psql'))

    def insertaddress(self):
        unival = random.randrange(1, 1000)
        ifirstname = input("Enter First Name: ").upper()
        while not re.match("^[A-Za-z]*$", ifirstname):
            print("Error! Make sure you only use letters in your name")
            ifirstname = input("Enter First Name: ").upper()
        ilastname = input("Enter Last Name:").upper()
        while not re.match("^[A-Za-z]*$", ilastname):
            print("Error! Make sure you only use letters in your name")
            ilastname = input("Enter Last Name: ").upper()
        iaddress = input("Enter Address:").upper()
        iphonenumber = input("Enter Phone Num :")
        iemailid = input("Enter Email ID :")
        while not re.match("^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$", iemailid):
            print("Invalid Email ID! Make sure you give proper email ID")
            iemailid = input("Enter Email ID :")
        insertquery = "INSERT INTO ADDRESSBOOK.Address_Info.PersonalInfo VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(unival, ifirstname, ilastname, iaddress, iphonenumber, iemailid)
        self.cursor.execute(insertquery)
        print("New Contact Added")

    def searchaddress(self):
        name = input("Enter First Name to Search:")
        searchquery = "SELECT * FROM ADDRESSBOOK.Address_Info.PersonalInfo WHERE FirstName = '{}';".format(name).upper()
        df2 = pd.read_sql_query(searchquery, self.conn)
        search = pd.DataFrame(df2)
        res = search.isin([name.upper()]).any().any()
        if res:
            print(tabulate(search, headers='keys', tablefmt='psql'))
        else:
            print("Name Doesnt Exist. Check the name")

    def updateaddress(self):
        name2 = input("Enter First Name of the contact to Update:").upper()
        searchquery2 = "SELECT * FROM ADDRESSBOOK.Address_Info.PersonalInfo WHERE FirstName = '{}';".format(
            name2).upper()
        df4 = pd.read_sql_query(searchquery2, self.conn)
        search = pd.DataFrame(df4)
        res2 = search.isin([name2.upper()]).any().any()
        if res2:
            change_addressbook = {
                1: 'Change Address',
                2: 'Change PhoneNumber',
                3: 'Change EmailID',
                4: 'Exit'
            }
            print(js.dumps(change_addressbook, indent=4))
            while True:
                choi = input('What do you want to update in address book :')
                if choi == "1":
                    address = input("Enter the address to update:").upper()
                    updateqry1 = "UPDATE ADDRESSBOOK.Address_Info.PersonalInfo SET [Address]='{}' WHERE FirstName = '{}';".format(
                        address, name2)
                    self.cursor.execute(updateqry1)
                    print("Address updated for the contact: {}".format(name2))
                elif choi == "2":
                    phonenum = input("Enter the PhoneNum to update:")
                    updateqry2 = "UPDATE ADDRESSBOOK.Address_Info.PersonalInfo SET [PhoneNum]='{}' WHERE FirstName = '{}';".format(
                        phonenum, name2)
                    self.cursor.execute(updateqry2)
                    print("PhoneNumber updated for the contact: {}".format(name2))
                elif choi == "3":
                    emailid = input("Enter the EmailID to update:")
                    updateqry3 = "UPDATE ADDRESSBOOK.Address_Info.PersonalInfo SET [EmailID]='{}' WHERE FirstName = '{}';".format(
                        emailid, name2)
                    self.cursor.execute(updateqry3)
                    print("EmailID updated for the contact: {}".format(name2))
                elif choi == "4":
                    break
                else:
                    print("Invalid choice!! Give numbers specified in the options")
        else:
            print("Name Doesnt Exist. Check the name")


    def deletebook(self):
        try:
            deletequery = "DROP TABLE ADDRESSBOOK.Address_Info.PersonalInfo"
            self.cursor.execute(deletequery)
            print('Address Book Deleted')
        except Exception as e:
            print(e)

    def deleteaddress(self):
        name1 = input("Enter First Name to delete:")
        searchquery1 = "SELECT * FROM ADDRESSBOOK.Address_Info.PersonalInfo WHERE FirstName = '{}';".format(name1).upper()
        df3 = pd.read_sql_query(searchquery1, self.conn)
        search = pd.DataFrame(df3)
        res1 = search.isin([name1.upper()]).any().any()
        if res1:
            deleteaddressquery = "DELETE FROM ADDRESSBOOK.Address_Info.PersonalInfo WHERE FirstName = '{}';".format(name1).upper()
            self.cursor.execute(deleteaddressquery)
            print(tabulate(search, headers='keys', tablefmt='psql'))
            print('Contact {} Deleted Successfully!!!'.format(name1))
        else:
            print("Name Doesnt Exist. Check the name")

    def commitdata(self):
        query = 'COMMIT'
        self.cursor.execute(query)




if __name__ == "__main__":


    option_addressbook = {
        1: 'Create Address Book Table',
        2: 'Populate data in AddressBook Table',
        3: 'View Address Book',
        4: 'Enter a New contact in Book',
        5: 'Search a Contact in Book by Name',
        6: 'Update Information in Book',
        7: 'Delete Entire AddressBook',
        8: 'Delete Based on Name',
        9: 'Exit'
    }

    address = AddressbookTable()
    address.sqlconnection()

    while True:
        print("*************ADDRESS BOOK******************")
        print(js.dumps(option_addressbook, indent=4))
        choice = input("Enter your choice::::")
        if choice == "1":
            try:
                address.createtable()
                address.commitdata()
            except Exception:
                print("TABLE ALREADY EXIST")
        elif choice == "2":
            try:
                for i in range(10):
                    address.populatedata()
                address.commitdata()
            except Exception:
                print("POPULATE DATA ERROR")
        elif choice == "3":
            try:
                address.viewaddress()
            except Exception :
                print("View AddressBook Error")
        elif choice == "4":
            try:
                address.insertaddress()
                address.commitdata()
            except Exception:
                print("New Contact Adding Error")
        elif choice == "5":
            try:
                address.searchaddress()
            except Exception:
                print("Search AddressBook Error")

        elif choice == "6":
            try:
                address.updateaddress()
                address.commitdata()
            except Exception:
                print("Update AddressBook Error")

        elif choice == "7":
            try:
                address.deletebook()
                address.commitdata()
            except Exception:
                print("Delete AddressBook Error")

        elif choice == "8":
            try:
                address.deleteaddress()
                address.commitdata()
            except Exception:
                print("Delete Contact Error")

        elif choice == "9":
            break
        else:
            print("Invalid choice!! Give numbers specified in the options")







