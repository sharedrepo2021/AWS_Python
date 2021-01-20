import pyodbc
import json as js
import pandas as pd
import faker

from tabulate import tabulate


class Addressbook:

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.sqlquery = ''

    def display_header(self):
        print('\n================================================')
        print('|            Select Your Option                |')
        print('================================================\n')

    def establish_connection(self):
        try:
            self.conn = pyodbc.connect('Driver={SQL Server};' 
                                       'Server=BALALENR7\SQLEXPRESS;' 
                                       'Database=AddressBook2021;'
                                       'Trusted_Connection=yes;')

            self.cursor = self.conn.cursor()
        except Exception:
            print('CONNECTION Failed !!!')

    def commit_statement(self):
        try:
            self.cursor.execute('COMMIT')
        except Exception:
            print('COMMIT Failed !!!')

    def curd_addrbook(self, curdquery):
        try:
            self.sqlquery = curdquery
            self.cursor.execute(self.sqlquery)
        except Exception:
            print('Activity Failed !!!')

    def select_addrbook(self, query):
        try:
            self.sqlquery = query
            df = pd.read_sql_query(self.sqlquery, self.conn)
            return df
        except Exception:
            print('SELECT Failed !!!')


if __name__ == '__main__':

    fake = faker.Faker()
    addbook = Addressbook()
    addbook.establish_connection()
    add_df = pd.DataFrame()

    addr_opt = {
        1: 'Create Address Book Table',
        2: 'View the Address Book',
        3: 'Insert Bluk Data',
        4: 'Add a New Address to the Address Book',
        5: 'Search an Existing Address using Address ID',
        6: 'Delete an Existing Address using Address ID',
        7: 'Modify an Existing Address using Address ID',
        8: 'Delete the Entire Address Book',
        0: 'Exit'
    }
    add_headers = ['INDEX', 'Address_ID', 'First_Name', 'Last_Name', 'Address',
                   'City', 'State', 'Country', 'Zip_Code', 'Phone_Number']

    while True:
        addbook.display_header()
        print(js.dumps(addr_opt, indent=2))
        opt = input("Select Option: ")

        if opt == '1':
            try:
                createquery = '''
                            if not exists (select * from sys.sysobjects where name='AddressBook' and xtype='U')
                                CREATE TABLE AddressBook2021.AddrBook.AddressBook
                                (
                                     Address_ID int NOT NULL PRIMARY KEY
                                    ,First_Name nvarchar(50) NOT NULL
                                    ,Last_Name nvarchar(50) NOT NULL
                                    ,Address nvarchar(100) NOT NULL
                                    ,City nvarchar(30) NOT NULL
                                    ,State nvarchar(30) NOT NULL
                                    ,Country nvarchar(30) NOT NULL
                                    ,Zip_Code nvarchar(10) NOT NULL
                                    ,Phone_Number nvarchar(30) NOT NULL
                                );
                               '''
                addbook.curd_addrbook(createquery)
                addbook.commit_statement()
                print('Table Created Successfully')
            except Exception as e:
                print('Exception: ', e)
                break
        elif opt == '2':
            try:
                selallqry = "SELECT * FROM [AddressBook2021].[Addrbook].[AddressBook] " \
                            "ORDER BY [Address_ID] ASC"
                add_df = addbook.select_addrbook(selallqry)
                if add_df.size == 0:
                    print('No Rows Found!!!')
                else:
                    print(tabulate(add_df, add_headers, tablefmt="fancy_grid"))
            except KeyError as e:
                print('Exception: ', e)
                break
        elif opt == '3':
            try:
                rows = int(input('Enter how many rows to populate: '))
                for i in range(rows):
                    aaid = fake.random_int(10000, 99999)
                    afname = fake.first_name().capitalize()
                    alname = fake.last_name().capitalize()
                    aaddr = fake.address()
                    acity = fake.city().capitalize()
                    astate = fake.state().capitalize()
                    acountry = 'USA'
                    azip = fake.postcode()
                    aphone = fake.phone_number()

                    insertbquery = "INSERT INTO [AddressBook2021].[Addrbook].[AddressBook] " \
                                    "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')" \
                                   "".format(aaid, afname, alname, aaddr, acity, astate, acountry, azip, aphone)

                    addbook.curd_addrbook(insertbquery)
                addbook.commit_statement()
            except Exception as e:
                print('Exception: ', e)
                break
        elif opt == '4':
            try:
                aaid = fake.random_int(10000, 99999)
                afname = input('Enter First Name     : ').capitalize()
                alname = input('Enter Last Name      : ').capitalize()
                aaddr = input('Enter Address        : ')
                acity = input('Enter City Name      : ')
                astate = input('Enter State Name     : ').capitalize()
                acountry = 'USA'
                azip = input('Enter Zip Code       : ')
                aphone = input('Enter Phone Number   : ')

                insertqry = "INSERT INTO [AddressBook2021].[Addrbook].[AddressBook] " \
                       "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(aaid, afname, alname,
                                                                                              aaddr, acity, astate,
                                                                                              acountry, azip, aphone)
                addbook.curd_addrbook(insertqry)
                addbook.commit_statement()
            except Exception as e:
                print('Exception: ', e)
                break
        elif opt == '5':
            try:
                aaid = int(input('Enter Address_ID: '))
                selectqry = "SELECT * FROM [AddressBook2021].[Addrbook].[AddressBook] " \
                            "WHERE Address_ID = '{}';".format(aaid)
                add_df = addbook.select_addrbook(selectqry)
                if add_df.size == 0:
                    print('Address-ID: {} Not Found!!!'.format(aaid))
                else:
                    print(tabulate(add_df, add_headers, tablefmt="fancy_grid"))
            except Exception as e:
                print('Exception: ', e)
                break
        elif opt == '6':
            try:
                aaid = int(input('Enter Address_ID: '))
                selectqry = "SELECT * FROM [AddressBook2021].[Addrbook].[AddressBook] " \
                            "WHERE Address_ID = '{}';".format(aaid)
                add_df = addbook.select_addrbook(selectqry)
                if add_df.size == 0:
                    print('Address-ID: {} Not Found!!!'.format(aaid))
                else:
                    deleteqry = "DELETE FROM [AddressBook2021].[Addrbook].[AddressBook] " \
                                "WHERE Address_ID = '{}';".format(aaid)
                    addbook.curd_addrbook(deleteqry)
                    addbook.commit_statement()
                    print('Address-ID: {} Deleted Successfully!!!'.format(aaid))
            except Exception as e:
                print('Exception: ', e)
                break
        elif opt == '7':
            try:
                aaid = int(input('Enter Address_ID where Address needs to be modified: '))
                selectqry = "SELECT * FROM [AddressBook2021].[Addrbook].[AddressBook] " \
                            "WHERE Address_ID = '{}';".format(aaid)
                add_df = addbook.select_addrbook(selectqry)
                if add_df.size == 0:
                    print('Address-ID: {} Not Found!!!'.format(aaid))
                else:
                    afname = input('Enter First Name     : ').capitalize()
                    alname = input('Enter Last Name      : ').capitalize()
                    aaddr = input('Enter Address        : ')
                    acity = input('Enter City Name      : ')
                    astate = input('Enter State Name     : ').capitalize()
                    acountry = 'USA'
                    azip = input('Enter Zip Code       : ')
                    aphone = input('Enter Phone Number   : ')

                    updateqry = "UPDATE [AddressBook2021].[Addrbook].[AddressBook] " \
                                "SET [First_Name]='{}', [Last_Name]='{}', [Address]='{}', " \
                                "[City]='{}', [State]='{}', [Country]='{}', [Zip_Code]='{}', [Phone_Number]='{}' " \
                                "WHERE Address_ID = '{}'" \
                        .format(afname, alname, aaddr, acity, astate, acountry, azip, aphone, aaid)
                    addbook.curd_addrbook(updateqry)
                    addbook.commit_statement()
                    print('Address-ID: {} Updated Successfully!!!'.format(aaid))
            except Exception as e:
                print('Exception: ', e)
                break
        elif opt == '8':
            dropquery = ''' DROP TABLE AddrBook.AddressBook; '''
            addbook.curd_addrbook(dropquery)
            addbook.commit_statement()
            print('Address Book Table Deleted Successfully!!!')
        elif opt == '0':
            break
        else:
            print('An Invalid Option is Given. Please give correct option')
