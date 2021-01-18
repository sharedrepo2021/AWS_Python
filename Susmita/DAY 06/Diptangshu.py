import json
import pandas as pd
from os import path
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


class Address:
    def __init__(self):

        self.add_dict = {}
        self.search_address = None

    def add_contact(self):
        try:
            self.add_dict['first_name'] = input('Enter first name: ')
            self.add_dict['last_name'] = input('Enter last name: ')
            self.add_dict['phone_number'] = int(input('Enter phone number: '))
            self.add_dict['address'] = input('Enter complete address: ')
            self.add_dict['email'] = input('Enter complete email address: ')
            self.add_dict['city'] = input('Enter the name of the city: ')
            self.add_dict['state'] = input('Enter the name of the state: ')
            self.add_dict['birthday'] = input('Enter birthdate in DD/MM/YYYY format: ')

            print("contact has been added")
            return self.add_dict

        except Exception as e:
            print('Unable to add item', e)

    def contact_search(self, address_book):

        try:
            search_criteria = {
                1: 'first_name',
                2: 'last_name',
                3: 'phone_number',
                4: 'email',
                5: 'city',
                6: 'state',
                7: 'birthday'

            }
            print(json.dumps(search_criteria, indent=5))
            search_criteria_input = int(input('Please select the option you want to search: '))

            if search_criteria_input == 1:
                self.search_address = address_book.loc[
                    (address_book['first_name'] == input('Enter the first name of the person: '))]
            elif search_criteria_input == 2:
                self.search_address = address_book.loc[
                    (address_book['last_name'] == input('Enter the last name of the person: '))]
            elif search_criteria_input == 3:
                self.search_address = address_book.loc[
                    (address_book['phone_number'] == int(input('Enter the phone number of the person: ')))]
            elif search_criteria_input == 4:
                self.search_address = address_book.loc[
                    (address_book['email'] == input('Enter the email address of the person: '))]
            elif search_criteria_input == 5:
                self.search_address = address_book.loc[
                    (address_book['city'] == input('Enter the name of the city the person belongs to: '))]
            elif search_criteria_input == 6:
                self.search_address = address_book.loc[
                    (address_book['state'] == input('Enter the name of the state the person belongs to: '))]
            elif search_criteria_input == 7:
                self.search_address = address_book.loc[
                    (address_book['birthdate'] == input('Enter the birthdate of the person in dd/mm/yyyy format: '))]
            else:
                print('Please select proper search criteria')

            if self.search_address.empty:
                print('No search record found')
            else:
                print(self.search_address)
                return self.search_address

        except Exception as e:
            print('Please provide proper input', e)

    def delete_contact(self, address_book, address_book_file):

        try:
            print(address_book)
            updated_address_book = address_book.drop(
                int(input('Enter the index number of the entry you want to delete: ')))
            print("Contact has been deleted'")
            updated_address_book.to_json(address_book_file, orient='records', lines=True)

        except Exception as e:
            print('Please provide proper input', e)

    def update_contact(self, address_book, address_book_file):

        try:
            print(address_book)
            x = int(input("Please select the index of table to be updated: "))

            option_dict = {
                1: 'first_name',
                2: 'last_name',
                3: 'phone_number',
                4: 'address',
                5: 'email',

            }
            print(json.dumps(option_dict, indent=5))
            user_input = int(input('Please select the option you want to update: '))

            if user_input == 1:
                new_first_name = pd.Series([input('Please enter the new first name: ')], name='first_name', index=[x])
                address_book.update(new_first_name)
            elif user_input == 2:
                new_last_name = pd.Series([input('Please enter the new last name: ')], name='last_name', index=[x])
                address_book.update(new_last_name)
            elif user_input == 3:
                new_phone_number = pd.Series([input(
                    'Please enter the new phone number: ')], name='phone_number', index=[x])
                address_book.update(new_phone_number)
            elif user_input == 4:
                new_address = pd.Series([input('Please enter the new address: ')], name='address', index=[x])
                address_book.update(new_address)
            elif user_input == 5:
                new_email = pd.Series([input('Please enter the new email dress: ')], name='email', index=[x])
                address_book.update(new_email)

            else:
                print("Please enter a correct input")

            address_book.to_json(address_book_file, orient='records', lines=True)

        except Exception as e:
            print("Please provide valid input", e)


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

    try:
        address_book_file = r'F:/address book.json'
        obj_address = Address()

        while True:
            choice = int(input('Please enter your choice: '))

            if choice == 1:
                break

            elif choice == 2:
                if path.exists(address_book_file):
                    address_book = pd.read_json(address_book_file, lines=True)
                    print(address_book)
                else:
                    print('No address book found')

            elif choice == 3:
                entry_dict = obj_address.add_contact()
                with open(address_book_file, 'a') as f:
                    json.dump(entry_dict, f)
                    f.write("\n")

            elif choice == 4:
                if path.exists(address_book_file):
                    address_book = pd.read_json(address_book_file, lines=True)
                    obj_address.contact_search(address_book)
                else:
                    print('No address book found')

            elif choice == 5:
                if path.exists(address_book_file):
                    address_book = pd.read_json(address_book_file, lines=True)
                    obj_address.delete_contact(address_book, address_book_file)
                else:
                    print('No address book found')

            elif choice == 6:
                if path.exists(address_book_file):
                    address_book = pd.read_json(address_book_file, lines=True)
                    obj_address.update_contact(address_book, address_book_file)
                    print('contact has been updated')
                else:
                    print('No address book found')

            else:
                print('Invalid input')

    except Exception as e:
        print('Provide proper input', e)