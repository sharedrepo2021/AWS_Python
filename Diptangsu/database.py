import pyodbc
import json
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


class Database:

    def __init__(self):
        self.conn = None
        self.query = None
        self.value = None
        self.my_cursor = None

    def connect(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=DESKTOP-2OIFI6J\SQLEXPRESS;'
                                   'Database=Address Book;'
                                   'Trusted_Connection=yes;')
        self.my_cursor = self.conn.cursor()
        return self.my_cursor

    def create_table(self, schema_name, table_name):
        self.query = '''
         CREATE TABLE {}.{} ( SL_No INT IDENTITY(1,1),
              First_Name VARCHAR(50), 
              Last_Name VARCHAR(50), 
              Phone_Number VARCHAR(10),
              Address VARCHAR(200),
              Email_Address VARCHAR(50),
              City VARCHAR(20),
              DOB DATE)'''.format(schema_name, table_name)
        self.my_cursor.execute(self.query)

    def dataframe_read(self, schema_name, table_name):
        query = pd.read_sql_query('''SELECT * FROM {}.{}'''.format(schema_name, table_name), self.conn)
        df = pd.DataFrame(query)
        print(df)

    def add_row(self, input_dict):
        self.query = '''INSERT INTO addressbook VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(
            input_dict['First_Name'], input_dict['Last_Name'], input_dict['Phone_Number'],
            input_dict['Address'], input_dict['Email_Address'], input_dict['City'],
            input_dict['DOB'])

        self.my_cursor.execute(self.query)
        return self.query

    def delete_table(self):
        self.query = '''
                DROP TABLE dbo.addressbook'''
        self.my_cursor.execute(self.query)

    def delete_row(self, schema_name, table_name, field_name, field_value):
        try:
            self.query = '''
                    DELETE FROM {}.{} WHERE {} = '{}'
                    '''.format(schema_name, table_name, field_name, field_value)
            self.my_cursor.execute(self.query)
        except Exception as e:
            print('Unable to delete row. Error: ', e)

    def commit(self):
        self.conn.commit()

    def update_row(self, schema_name, table_name, column_name, column_value, field_name, field_value):
        self.query = '''
                    UPDATE {}.{} SET {} = '{}' WHERE {} = '{}'
                    '''.format(schema_name, table_name, column_name, column_value, field_name, field_value)

        self.my_cursor.execute(self.query)

    def contact_search(self):
        search_criteria = {
            1: 'first_name',
            2: 'last_name',
            3: 'phone_number',
            4: 'email',
            5: 'city',
            6: 'birthday'
        }
        print(json.dumps(search_criteria, indent=5))
        user_input = int(input('Please select the option you want to search: '))

        if user_input == 1:
            search_first_name = input('Please enter the first name of the user to be searched: ')
            self.query = '''
                SELECT * FROM dbo.addressbook WHERE First_Name = '{}' '''.format(search_first_name)
            self.my_cursor.execute(self.query).fetchall()
            query = pd.read_sql_query(self.query, self.conn)
            df = pd.DataFrame(query)
            print(df)
        elif user_input == 2:
            search_last_name = input('Please enter the last name of the user to be searched: ')
            self.query = '''
                SELECT * FROM dbo.addressbook WHERE Last_Name = '{}' '''.format(search_last_name)
            self.my_cursor.execute(self.query).fetchall()
            query = pd.read_sql_query(self.query, self.conn)
            df = pd.DataFrame(query)
            print(df)
        elif user_input == 3:
            search_phone_number = input('Please enter the phone number of the user to be searched: ')
            self.query = '''
                SELECT * FROM dbo.addressbook WHERE Phone_Number = '{}' '''.format(search_phone_number)
            self.my_cursor.execute(self.query).fetchall()
            query = pd.read_sql_query(self.query, self.conn)
            df = pd.DataFrame(query)
            print(df)
        elif user_input == 4:
            search_email = input('Please enter the email address of the user to be searched: ')
            self.query = '''
                SELECT * FROM dbo.addressbook WHERE Email_Address = '{}' '''.format(search_email)
            self.my_cursor.execute(self.query).fetchall()
            query = pd.read_sql_query(self.query, self.conn)
            df = pd.DataFrame(query)
            print(df)
        elif user_input == 5:
            search_city = input('Please enter the name of the city the user belongs to: ')
            self.query = '''
                SELECT * FROM dbo.addressbook WHERE City = '{}' '''.format(search_city)
            self.my_cursor.execute(self.query).fetchall()
            query = pd.read_sql_query(self.query, self.conn)
            df = pd.DataFrame(query)
            print(df)
        elif user_input == 6:
            search_city = input('Please enter the date of birth of the user to be searched(YYYY-MM-DD): ')
            self.query = '''
                SELECT * FROM dbo.addressbook WHERE DOB = '{}' '''.format(search_city)
            self.my_cursor.execute(self.query).fetchall()
            query = pd.read_sql_query(self.query, self.conn)
            df = pd.DataFrame(query)
            print(df)
        else:
            print('Please select an appropriate option')


