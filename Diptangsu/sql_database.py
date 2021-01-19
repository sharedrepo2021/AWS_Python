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
        self.input_dict = {}

    def connect(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=DESKTOP-2OIFI6J\SQLEXPRESS;'
                                   'Database=Address Book;'
                                   'Trusted_Connection=yes;')
        self.my_cursor = self.conn.cursor()
        return self.my_cursor

    def create_table(self):
        self.query = '''
         CREATE TABLE dbo.addressbook ( SL_No INT IDENTITY(1,1),
              First_Name VARCHAR(50), 
              Last_Name VARCHAR(50), 
              Phone_Number VARCHAR(10),
              Address VARCHAR(200),
              Email_Address VARCHAR(50),
              City VARCHAR(20),
              DOB DATE)'''
        self.my_cursor.execute(self.query)

    def get_user_input(self):
        try:

            self.input_dict['First_Name'] = input('Enter first name: ')
            self.input_dict['Last_Name'] = input('Enter last name: ')
            self.input_dict['Phone_Number'] = int(input('Enter phone number: '))
            self.input_dict['Address'] = input('Enter complete address: ')
            self.input_dict['Email_Address'] = input('Enter complete email address: ')
            self.input_dict['City'] = input('Enter the name of the city: ')
            self.input_dict['DOB'] = input('Enter birthdate in YYYY-MM-DD format: ')

        except Exception as e:
            print('Please provide appropriate input', e)

    def dataframe_read(self):
        query = pd.read_sql_query('''SELECT * FROM dbo.addressbook''', self.conn)
        df = pd.DataFrame(query)
        print(df)

    def add_contact(self):
        self.query = '''INSERT INTO addressbook VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(
            self.input_dict['First_Name'], self.input_dict['Last_Name'], self.input_dict['Phone_Number'],
            self.input_dict['Address'], self.input_dict['Email_Address'], self.input_dict['City'],
            self.input_dict['DOB'])

        self.my_cursor.execute(self.query)
        return self.query

    def delete_table(self):
        self.query = '''
                DROP TABLE dbo.addressbook'''
        self.my_cursor.execute(self.query)

    def delete_records(self):
        try:
            user_input = input('Enter the Sl.No of the contact you wish to delete: ')
            self.query = '''
                    DELETE FROM addressbook WHERE SL_NO = '{}'
                    '''.format(user_input)
            self.my_cursor.execute(self.query)
        except Exception as e:
            print('Please select one from the given Sl.No', e)

    def commit(self):
        self.conn.commit()

    def update_contact(self):
        user_sl_input = input('Please enter the Sl No. of the contact you wish to modify: ')

        option_dict = {
            1: 'First_Name',
            2: 'Last_Name',
            3: 'Phone_Number',
            4: 'Address',
            5: 'Email Address',
            6: 'City',
            7: 'DOB'
        }
        print(json.dumps(option_dict, indent=5))

        user_input = int(input('Please select the option you want to update: '))

        if user_input == 1:
            mod_first_name = input('Enter new first name: ')
            self.query = '''
                            UPDATE dbo.addressbook SET First_Name = '{}' WHERE SL_NO = '{}'
                            '''.format(mod_first_name, user_sl_input)
        elif user_input == 2:
            mod_last_name = input('Enter new last name: ')
            self.query = '''
                            UPDATE dbo.addressbook SET Last_Name = '{}' WHERE SL_NO = '{}'
                            '''.format(mod_last_name, user_sl_input)
        elif user_input == 3:
            mod_phone_number = input('Enter new first phone number: ')
            self.query = '''
                            UPDATE dbo.addressbook SET Phone_Number = '{}' WHERE SL_NO = '{}'
                            '''.format(mod_phone_number, user_sl_input)
        elif user_input == 4:
            mod_address = input('Enter new address: ')
            self.query = '''
                            UPDATE dbo.addressbook SET Address = '{}' WHERE SL_NO = '{}'
                            '''.format(mod_address, user_sl_input)
        elif user_input == 5:
            mod_email_address = input('Enter new email address: ')
            self.query = '''
                            UPDATE dbo.addressbook SET Email_Address = '{}' WHERE SL_NO = '{}'
                            '''.format(mod_email_address, user_sl_input)
        elif user_input == 6:
            mod_city = input('Enter the new name of the city: ')
            self.query = '''
                            UPDATE dbo.addressbook SET City = '{}' WHERE SL_NO = '{}'
                            '''.format(mod_city, user_sl_input)
        elif user_input == 7:
            mod_dob = input('Enter new birthdate in YYYY-MM-DD format: ')
            self.query = '''
                            UPDATE dbo.addressbook SET DOB = '{}' WHERE SL_NO = '{}'
                            '''.format(mod_dob, user_sl_input)
        else:
            print('Please select a proper input')

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


if __name__ == "__main__":

    choices_dict = {
        1: 'Exit',
        2: 'Display address book',
        3: 'Add contact',
        4: 'Search contact',
        5: 'Delete contact',
        6: 'Update contact'

    }
    print(json.dumps(choices_dict, indent=5))

    db = Database()
    try:
        while True:
            choice = int(input('Please enter your choice: '))
            db.connect()

            if choice == 1:
                break
            elif choice == 2:
                db.dataframe_read()
            elif choice == 3:
                db.get_user_input()
                db.add_contact()
                db.commit()
                db.dataframe_read()
                print('contact has been added successfully')
            elif choice == 4:
                db.contact_search()
            elif choice == 5:
                db.dataframe_read()
                db.delete_records()
                db.commit()
                print('Record has been deleted')
            elif choice == 6:
                db.dataframe_read()
                db.update_contact()
                db.commit()
                db.dataframe_read()
                print('Contact details has been updated')
            else:
                print('Please select appropriate option from the list')
    except Exception as e:
        print('Please provide a valid input', e)
