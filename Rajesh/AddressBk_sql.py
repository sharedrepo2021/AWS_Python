import pandas as pd
from tabulate import tabulate
import pyodbc

class DatabaseConn:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=DESKTOP-26UUTJF\SQLEXPRESS;'
                                   'Database=master;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

class AddressBook(DatabaseConn):
    def __init__(self):
        self.book_dict = {
            "FName": '',
            "LName": '',
            "email": '',
            "phone": '',
            "address": ''}

        self.choice = None
        self.srchkey = None
        self.srchkey1 = None
        self.srchkey2 = None
        self.srchfld = None
        self.srchfld1 = None
        self.srchfld2 = None
        self.sql1 = None
        self.mytable=None
        self.mytable_schema = None
        self.mytable_name = None
        self.mytable_bkp= 'person.address_bkp_db'
        self.tableexist = None

    def getinput(self):
        self.book_dict = dict()
        self.book_dict['FName'] = input(" Enter the First Name   : ")
        self.book_dict['LName'] = input(" Enter the Last Name    : ")
        self.book_dict['email'] = input(" Enter the Email addr   : ")
        self.book_dict['phone'] = input(" Enter the Phone Number : ")
        self.book_dict['addr'] = input(" Enter the Address      : ")

    def addcontact(self):

        placeholders = ', '.join(['?'] * len(self.book_dict))
        columns = ', '.join(self.book_dict.keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )  " % (self.mytable, columns, placeholders)
        value = tuple(self.book_dict.values())
        self.cursor.execute(sql, value)
        sql = 'COMMIT'
        self.cursor.execute(sql)

    def restorecontact(self):

        sql = "INSERT INTO {0} SELECT * from {1} where Fname = '{2}' and Lname = '{3}' " \
        .format(self.mytable, self.mytable_bkp, self.srchkey1, self.srchkey2)
        self.cursor.execute(sql)
        sql = 'COMMIT'
        self.cursor.execute(sql)

    def selectall(self):

        sql = "SELECT * FROM %s " % (self.mytable)
        self.sql1 = pd.read_sql_query(sql, self.conn)

    def tablestatus(self):

        sql = "SELECT * from information_schema.tables where table_schema = '{0}' and table_name ='{1}'" \
            .format(self.mytable_schema, self.mytable_name)
        self.cursor.execute(sql)
        self.tableexist = self.cursor.fetchone()

    def recoverbook(self):

        sql = "INSERT INTO {0} SELECT * from {1} " \
            .format(self.mytable, self.mytable_bkp)
        self.cursor.execute(sql)
        sql = 'COMMIT'
        self.cursor.execute(sql)

    def createnewbook(self):

        sql = "CREATE TABLE {0} (Fname varchar(50), Lname varchar(50), email varchar(100) \
        ,phone varchar(10), addr varchar(100))".format(self.mytable)
        self.cursor.execute(sql)
        sql = 'COMMIT'
        self.cursor.execute(sql)

    def deletebook(self):

        sql = "TRUNCATE TABLE {0} ".format(self.mytable)
        self.cursor.execute(sql)
        sql = 'COMMIT'
        self.cursor.execute(sql)

    def bookoptions(self):
        print("\n")
        print("   ====================================================================")
        print("   |:::::|                    MY ADDRESS BOOK                    |::::|")
        print("   ====================================================================")
        print("   |  M  |  1  | Add a Contact   |:::::|   :   |::::::::::::::::::::::|")
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
        print("   |  K  |  7  | Show Contacts   |:::::|   :   |::::::::::::::::::::::|")
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
        sql = "SELECT * FROM {0} where {1} = '{2}' ".format(self.mytable, self.srchfld, self.srchkey )
        self.sql1 = pd.read_sql_query(sql, self.conn)
        if self.sql1.empty:
            print("\n CONTACT NOT FOUND IN ADDRESS BOOK !!")
        else:
            print(tabulate(addr.sql1, headers="keys", tablefmt='grid'))

    def updatecontact(self):

        self.book_dict['FName'] = self.srchkey1
        self.book_dict['LName'] = self.srchkey2
        sql = "SELECT * FROM %s where %s = '%s' and %s = '%s' " \
              % (self.mytable, self.srchfld1, self.srchkey1, self.srchfld2, self.srchkey2)
        self.sql1 = pd.read_sql_query(sql, self.conn)
        if not self.sql1.empty:
            if not self.mytable == 'person.address_bkp_db':
                self.book_dict['email'] = input(" Enter the New Email addr   : ")
                self.book_dict['phone'] = input(" Enter the New Phone Number : ")
                self.book_dict['address'] = input(" Enter the New Address      : ")
            sql = "UPDATE {0} SET email = '{1}' , phone = '{2}' , addr = '{3}'  where Fname = '{4}' and Lname = '{5}' "  \
                .format(self.mytable, self.book_dict['email'], self.book_dict['phone'], self.book_dict['address'], \
                 self.srchkey1, self.srchkey2)
            self.cursor.execute(sql)
            sql = 'COMMIT'
            self.cursor.execute(sql)
            print("\n CONTACT UPDATED TO ADDRESS BOOK!!")
        else:
            print("\n NO RECORD FOUND")


    def deletecontact(self):

        self.book_dict['FName'] = self.srchkey1
        self.book_dict['LName'] = self.srchkey2
        sql = "SELECT * FROM %s where %s = '%s' and %s = '%s' " \
              % (self.mytable, self.srchfld1, self.srchkey1, self.srchfld2, self.srchkey2)
        self.sql1 = pd.read_sql_query(sql, self.conn)
        if not self.sql1.empty:
            sql = "DELETE from {0} where Fname = '{1}' and Lname = '{2}' " \
                .format(self.mytable, self.srchkey1, self.srchkey2)
            self.cursor.execute(sql)
            sql = 'COMMIT'
            self.cursor.execute(sql)
            print("\n CONTACT DELETED FROM ADDRESS BOOK!!")
        else:
            print("\n NO RECORD FOUND")

    def searchbylfname(self):

        sql = "SELECT * FROM {0} where {1} = '{2}' and {3} = '{4}' " \
             .format(self.mytable, self.srchfld1, self.srchkey1, self.srchfld2, self.srchkey2 )
        self.sql1 = pd.read_sql_query(sql, self.conn)
        if self.sql1.empty:
            print("\n CONTACT NOT FOUND IN ADDRESS BOOK !!")
        else:
            print(tabulate(addr.sql1, headers="keys", tablefmt='grid'))


if __name__ == '__main__':

    addr = AddressBook()

    schema = 'person'
    ctable = 'address_db'
    btable = 'address_bkp_db'
    curr_table = 'person.address_db'
    bkp_table = 'person.address_bkp_db'
    addr.srchfld1 = 'FName'
    addr.srchfld2 = 'LName'

    addr.connect()

    addr.mytable_schema = schema
    addr.mytable_name = btable

    addr.tablestatus()

    if addr.tableexist:
        pass
    else:
        addr.mytable = bkp_table
        addr.createnewbook()
        print("BACKUP TABLE CREATED!")

    addr.mytable_name = ctable
    addr.tablestatus()
    if addr.tableexist:
        pass
    else:
        addr.mytable = curr_table
        addr.createnewbook()
        print("ADDRESS BOOK CREATED!")

    addr.bookoptions()

    while addr.choice != 0:
        addr.mytable = curr_table
        if addr.choice == 1:
            addr.getinput()
            addr.addcontact()
            addr.mytable = bkp_table
            addr.addcontact()
        elif addr.choice == 2:
            addr.srchkey1 = input("\n Enter the first Name : ")
            addr.srchkey2 = input(" Enter the Last Name  : ")
            addr.updatecontact()
            addr.mytable = bkp_table
            addr.updatecontact()
        elif addr.choice == 3:
                addr.srchkey1 = input("\n Enter the first Name : ")
                addr.srchkey2 = input(" Enter the Last Name  : ")
                addr.deletecontact()
        elif addr.choice == 4:
            addr.srchkey1 = input("\n Enter the first Name : ")
            addr.srchkey2 = input(" Enter the Last Name  : ")
            addr.searchbylfname()
            if addr.sql1.empty:
                addr.restorecontact()
                print("\n CONTACT INFORMATION RESTORED!")
        elif addr.choice == 5:
            addr.deletebook()
            print("\n ALL CONTACTS ERASED !!")
        elif addr.choice == 6:
            addr.recoverbook()
            print("\n ADDRESS BOOK RESTORED!")
        elif addr.choice == 7:
            addr.selectall()
            tot_rows = len(addr.sql1.index)
            print(tabulate(addr.sql1, headers="keys", tablefmt='grid'))
            print("\n TOTAL CONTACTS IN BOOK : " + str(tot_rows))
        elif addr.choice == 8:
            addr.srchfld = addr.srchfld1
            addr.searchcontact()
        elif addr.choice == 9:
            addr.srchfld = addr.srchfld2
            addr.searchcontact()
        elif addr.choice == 10:
            addr.srchfld = 'phone'
            addr.searchcontact()
        addr.bookoptions()
