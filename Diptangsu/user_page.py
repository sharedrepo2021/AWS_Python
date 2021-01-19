import json
from database import *
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


class Addressbook:
    def __init__(self):
        self.input_dict = {}
        self.db = Database()
        self.schema_name = None
        self.table_name = None
        self.field_value = None
        self.field_name = None
        self.column_name = None
        self.column_value = None

    def db_connect(self):
        self.db.connect()

    def get_schema(self):
        self.schema_name = input('Please enter the schema name: ')

    def get_table(self):
        self.table_name = input('Please enter the table name: ')

    def get_field_name(self):
        self.field_name = input('Please enter the field name: ')

    def get_field_value(self):
        self.field_value = input('Please enter the field value: ')

    def display_addressbook(self):
        self.db.dataframe_read(self.schema_name, self.table_name)

    def add_contact(self):
        try:

            self.input_dict['First_Name'] = input('Enter first name: ')
            self.input_dict['Last_Name'] = input('Enter last name: ')
            self.input_dict['Phone_Number'] = int(input('Enter phone number: '))
            self.input_dict['Address'] = input('Enter complete address: ')
            self.input_dict['Email_Address'] = input('Enter complete email address: ')
            self.input_dict['City'] = input('Enter the name of the city: ')
            self.input_dict['DOB'] = input('Enter birthdate in YYYY-MM-DD format: ')

            self.db.add_row(self.input_dict)
            self.db.commit()
            print('Contact has been added')
        except Exception as e:
            print('Please provide appropriate input. Error: ', e)

    def delete_records(self):
        self.get_field_name()
        self.get_field_value()
        self.db.delete_row(self.schema_name, self.table_name, self.field_name, self.field_value)
        self.db.commit()
        print('Contact has been deleted')

    def search_contact(self):
        try:
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

            self.field_name = search_criteria[user_input]
            self.field_value = input('Enter the value you want to search: ')

            self.db.contact_search(self.schema_name, self.table_name, self.field_name, self.field_value)
        except Exception as e:
            print('Please select a valid input. Error: ', e)

    def update_contact(self):
        try:
            self.display_addressbook()

            self.field_name = 'SL_No'
            self.field_value = input('Enter the row number you want to update: ')

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

            self.column_name = option_dict[user_input]
            self.column_value = input('Enter the modified value: ')

            self.db.update_row(self.schema_name, self.table_name, self.column_name, self.column_value, self.field_name,
                               self.field_value)
            self.db.commit()
            print('Contact has been updated')
            self.display_addressbook()
        except Exception as e:
            print('Please provide a proper input. Error: ', e)

    def get_choice(self):
        choices_dict = {
            1: 'Exit',
            2: 'Display address book',
            3: 'Add contact',
            4: 'Search contact',
            5: 'Delete contact',
            6: 'Update contact'

        }
        print(json.dumps(choices_dict, indent=5))
        choice = int(input('Please enter your choice: '))
        return choice


if __name__ == "__main__":

    add_book = Addressbook()

    try:
        add_book.db_connect()
        add_book.get_schema()
        add_book.get_table()

        while True:
            choice = add_book.get_choice()

            if choice == 1:
                break
            elif choice == 2:
                add_book.display_addressbook()
            elif choice == 3:
                add_book.add_contact()
                add_book.display_addressbook()
            elif choice == 4:
                add_book.search_contact()
            elif choice == 5:
                add_book.delete_records()
                add_book.display_addressbook()
            elif choice == 6:
                add_book.update_contact()
            else:
                print('Please select appropriate option from the list')
    except Exception as e:
        print('Please provide a valid input', e)
