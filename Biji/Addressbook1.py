import json
import pyodbc
import pandas as pd
import re

class Addressbook:

    def __init__(self):
        self.name=""
        self.phone=""
        self.sqltab='person.details'
    def connect(self):
        self.con = pyodbc.connect('Driver={SQL Server};'
                                 'Server=BIJI-PC\SQLEXPRESS;'
                                 'Database=employee;'
                                 'Trusted_Connection=yes;')
        self.cursor = self.con.cursor()
    def showaddressbook(self):
        query="select * from person.details"
        #sqltab= pd.read_sql_query(query,self.con)
        #print(sqltab)
        self.cursor.execute(query)
        var=self.cursor.fetchall()
        if not var:
            print("Address book is empty")
        else:
         for row in self.cursor.execute(query):
             print("Name:", row[0],"Address:",row[1], "Phone:", row[2])

    def searchanentry(self):
        self.name = input("Enter name :")
        query = "select * from person.details where name='{}'".format(self.name)
        self.cursor.execute(query)
        var = self.cursor.fetchall()
        if not var:
            print("details not found")

        else:
            for i in range(len(var)):
                print(var[i])
    def insertdata(self):
        name = input("Enter name :")
        address = input("Enter Address ")
        phone = input("Enter phone number :")
        query = "INSERT INTO person.details(name,address,phone) VALUES ('{}','{}','{}')".format(name,address, phone)
        objadd.cursor.execute(query)

    def printconfirm(self):
        print("name {} added".format(self.name))
    def deleteanetry(self):
        self.name = input("Enter name :")
        query = "select * from person.details where name='{}'".format(self.name)
        self.cursor.execute(query)
        var = self.cursor.fetchall()
        if not var:
            print("details not found")
        else:
            query="delete from person.details where name='{}'".format(self.name)
            self.cursor.execute(query)
            print("entry ddeleted")
    def updateanetry(self):
        self.name = input("Enter name :")
        query = "select * from person.details where name='{}'".format(self.name)
        self.cursor.execute(query)
        var = self.cursor.fetchall()
        if not var:
            print("details not found")
        else:
            print("what do u want to update?")
            print("1: Phone no")
            print("2: Address")
            print("3: Both")
            opt = int(input("Select an option : "))
            if opt ==1:
              phone = input("Enter phone:")
              query = "update person.details set phone='{}'".format(phone)+ "where  name = '{}'".format(self.name)
              self.cursor.execute(query)
              print("phone number updated")
            elif opt ==2:
              address=input("Enter address:")
              query = "update person.details set address='{}'".format(address) + "where  name = '{}'".format(self.name)
              self.cursor.execute(query)
              print("Address updated")
            elif opt ==3:
              phone = input("Enter phone:")
              address=input("Enter address:")
              query = "update person.details set phone='{}', address='{}'".format(phone,address) + "where  name = '{}'".format(self.name)
              self.cursor.execute(query)
              print("phone number&address updated")
            else:
                print("select a valid option")
    def deleteaddressbook(self):
        query = "delete from person.details"
        self.cursor.execute(query)
        print("Adressbook deleted")
    def comitresults(self):
        query = 'COMMIT'
        self.cursor.execute(query)
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
while True:
    choice = int(input("Select an option : "))
    if choice == 1:
        objadd.connect()
        objadd.showaddressbook()
    elif choice == 2:
        objadd.connect()
        objadd.insertdata()
        objadd.printconfirm()
        objadd.comitresults()
    elif choice == 3:
        objadd.connect()
        objadd.deleteanetry()
        objadd.comitresults()
    elif choice == 4:
        objadd.connect()
        objadd.deleteaddressbook()
        objadd.comitresults()
    elif choice == 5:
        objadd.connect()
        objadd.searchanentry()
    elif choice == 6:
        objadd.connect()
        objadd.updateanetry()
        objadd.comitresults()
    elif choice == 7:
        break
    else:
      print("Enter valid option ")


