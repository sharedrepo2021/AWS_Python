from SQL_DB import DBase
from Send_Email import Email
import pandas as pd
import json
import datetime


def print_formatted(df):
    from tabulate import tabulate
    print(tabulate(df, headers='keys', tablefmt='psql'))


class Library:
    def __init__(self):
        self.email = Email()
        self.db = DBase()
        self.db.connect()
        self.book_path = r"C:\Users\dipan\Desktop\Book.csv"

    def create_database(self):
        _query = '''
            IF NOT EXISTS ( SELECT  *
                    FROM    sys.schemas
                    WHERE   name = N'LIBRARY' )
            EXEC('CREATE SCHEMA [LIBRARY]');
            '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
            IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='ITEMS' AND XTYPE='U')
            CREATE TABLE LIBRARY.ITEMS(
                BOOK_ID INT NOT NULL IDENTITY(1,1),
                AUTHOR_NAME VARCHAR(255) NOT NULL,
                BOOK_TITLE VARCHAR(255) NOT NULL            
                )
            '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
            IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='EMPLOYEES' AND XTYPE='U')
            CREATE TABLE LIBRARY.EMPLOYEES(
                EMPLOYEE_ID INT NOT NULL IDENTITY(1,1),
                NAME VARCHAR(255) NOT NULL,
                ADDRESS VARCHAR(255) NOT NULL,
                PHONE_NUMBER VARCHAR(25)            
                )
            '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
            IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='EVENTS' AND XTYPE='U')
            CREATE TABLE LIBRARY.EVENTS(
                ACTIVITY_ID INT NOT NULL IDENTITY(1,1),
                DESCRIPTION VARCHAR(255) NOT NULL,
                EVENT_DATE DATE NOT NULL,
                AGE INT NOT NULL,
                MAX_OCCUPANCY INT NOT NULL,
                CURRENT_OCCUPANCY INT     
                )
            '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
           IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='USERS' AND XTYPE='U')
           CREATE TABLE LIBRARY.USERS(
               USER_ID INT NOT NULL IDENTITY(1,1),
               NAME VARCHAR(255) NOT NULL,
               ADDRESS VARCHAR(255) NOT NULL,
               PHONE_NUMBER VARCHAR(25),
               LIBRARY_ID INT NOT NULL           
               )
           '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
            IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='TRANSACTIONS' AND XTYPE='U')
            CREATE TABLE LIBRARY.TRANSACTIONS(
                BOOK_ID INT NOT NULL IDENTITY(1,1),
                TRANSACTION_DATE DATE NOT NULL,
                BOOK_TITLE VARCHAR(255) NOT NULL,
                LIBRARY_ID INT NOT NULL          
                )
            '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
            IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='CHECK_OUT' AND XTYPE='U')
            CREATE TABLE LIBRARY.CHECK_OUT(
                BOOK_ID INT NOT NULL,
                USER_ID INT NOT NULL,
                CHECK_OUT_IND BIT           
                )
            '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
            IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='EVENT_REGISTRATION' AND XTYPE='U')
            CREATE TABLE LIBRARY.EVENT_REGISTRATION(
                ACTIVITY_ID INT NOT NULL,
                USER_ID INT NOT NULL,
                KIDS_COUNT INT           
                )
            '''
        self.db.execute_sql_and_commit(_query)

    def populate_items(self):
        book_df = pd.read_csv(self.book_path)
        print(book_df)

        _query = "DELETE FROM LIBRARY.ITEMS"
        self.db.execute_sql_and_commit(_query)

        for index, row in book_df.iterrows():
            _query = "INSERT INTO LIBRARY.ITEMS (AUTHOR_NAME, BOOK_TITLE) VALUES('{}', '{}')". \
                format(row.Author, row.Title)
            self.db.execute_sql_and_commit(_query)

    def delete_items(self, book_title):
        _query = "DELETE FROM LIBRARY.ITEMS WHERE BOOK_TITLE = '{}' ".format(book_title)
        self.db.execute_sql_and_commit(_query)

    def show_items(self):
        _query = "SELECT * FROM LIBRARY.ITEMS ORDER BY BOOK_ID DESC"
        result_df = self.db.execute_sql(_query)
        print_formatted(result_df)

    def search_items_author_name(self, author_name):
        _query = "SELECT * FROM LIBRARY.ITEMS WHERE AUTHOR_NAME = '{}';".format(author_name)
        print_formatted(self.db.execute_sql(_query))

    def search_items_book_title(self, book_title):
        _query = "SELECT * FROM LIBRARY.ITEMS WHERE BOOK_TITLE = '{}';".format(book_title)
        print_formatted(self.db.execute_sql(_query))

    def add_items(self):
        _name = input("Enter Author name: ")
        _title = input("Enter Book Title")
        _query = "INSERT INTO LIBRARY.ITEMS VALUES('{}', '{}')" \
            .format(_name, _title)
        self.db.execute_sql_and_commit(_query)

    def add_employee(self):
        _name = input("Enter name: ")
        _address = input("Enter address: ")
        _phone = input("Enter phone number: ")
        _query = "INSERT INTO LIBRARY.EMPLOYEES VALUES('{}', '{}', '{}')" \
            .format(_name, _address, _phone)
        self.db.execute_sql_and_commit(_query)

    def delete_employee(self, employee_id):
        _query = "DELETE FROM LIBRARY.EMPLOYEES WHERE EMPLOYEE_ID = {} ".format(employee_id)
        self.db.execute_sql_and_commit(_query)

    def show_employee(self):
        _query = "SELECT * FROM LIBRARY.EMPLOYEES"
        result_df = self.db.execute_sql(_query)
        print_formatted(result_df)

    def add_user(self):
        _name = input("Enter name: ")
        _address = input("Enter address: ")
        _phone = input("Enter phone number: ")
        _library_id = datetime.datetime.now().strftime('%Y%m%d%H')
        _query = "INSERT INTO LIBRARY.USERS VALUES('{}', '{}', '{}', {})" \
            .format(_name, _address, _phone, _library_id)
        self.db.execute_sql_and_commit(_query)

    def delete_user(self, library_id):
        _query = "DELETE FROM LIBRARY.USERS WHERE LIBRARY_ID = {} ".format(library_id)
        self.db.execute_sql_and_commit(_query)

    def show_user(self):
        _query = "SELECT * FROM LIBRARY.USERS"
        result_df = self.db.execute_sql(_query)
        print_formatted(result_df)


if __name__ == '__main__':
    lib = Library()
    lib.create_database()
    # lib.populate_items()
    # book_title = input("Enter the title of the book you want to delete:: ")
    # lib.delete_items(book_title)
    # lib.show_items()
    # author_name = input("Enter the name of author you want to search:: ")
    # lib.search_items_author_name(author_name)
    # lib.search_items_book_title(book_title)
    # lib.add_employee()

    while True:
        print('\n')
        print("Select an Option::")
        search_option_dict = {
            0: 'Exit',
            1: 'Add Employee',
            2: 'Show Employee',
            3: 'Delete Employee',
            4: 'Load Book Details',
            5: 'Add new book/cd',
            6: 'Delete book/cd',
            7: 'View book/cd',
            8: 'Search book by author name',
            9: 'Search book by book title',
            10: 'Add User',
            11: 'Show User',
            12: 'Delete User'
        }
        print(json.dumps(search_option_dict, indent=4))

        option = int(input("Select Option: "))
        if option == 0:
            break
        elif option == 1:
            lib.add_employee()
        elif option == 2:
            lib.show_employee()
        elif option == 3:
            employee_id = input("Enter Employee ID: ")
            lib.delete_employee(employee_id)
        elif option == 4:
            lib.populate_items()
        elif option == 5:
            lib.add_items()
        elif option == 6:
            book_title = input("Enter the title of the book you want to delete:: ")
            lib.delete_items(book_title)
        elif option == 7:
            lib.show_items()
        elif option == 8:
            author_name = input("Enter the name of author you want to search:: ")
            lib.search_items_author_name(author_name)
        elif option == 9:
            book_title = input("Enter the title of the book you want to search:: ")
            lib.search_items_book_title(book_title)
        elif option == 10:
            lib.add_user()
        elif option == 11:
            lib.show_user()
        elif option == 12:
            library_id = input("Enter Library ID: ")
            lib.delete_user(library_id)
        else:
            print('Invalid option')