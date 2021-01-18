import json


def add_entry():
    my_dict = {}
    input_var = input('Enter your name: ')
    my_dict['Name'] = input_var
    input_var = input('Enter your phone number: ')
    if input_var:
        my_dict['Phone'] = input_var
    input_var = input('Enter your address: ')
    if input_var:
        my_dict['Address'] = input_var
    return my_dict


def search_entry():
    pass


def delete_entry():
    pass


def update_entry():
    pass


def display_address_book(addressbook):
    print(addressbook)


if __name__ == "__main__":
    print('ADDRESS BOOK')
    addressbook = []
    option_dict = {
        1: 'Search for a person',
        2: 'Add your information to the address book',
        3: 'Delete an Entry',
        4: 'Update an Entry',
        5: 'Display address book',
        6: 'Exit'
    }
    print(json.dumps(option_dict, indent=4))

    while True:
        i = int(input("Select an option :"))
        if i == 1:
            search_entry()
        elif i == 2:
            new_entry = add_entry()
            addressbook.append(new_entry)
        elif i == 3:
            delete_entry()
        elif i == 4:
            update_entry()
        elif i == 5:
            display_address_book(addressbook)
        elif i == 6:
            break
        else:
            print("Please enter a valid option")
