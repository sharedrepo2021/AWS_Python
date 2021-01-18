from Database import DBase
import json


class Addressbook:
    def __init__(self):
        self.datastore = None
        self.all_entries_df = None

    def set_datastore(self, datastore):
        self.datastore = datastore

    def display_main_menu(self):
        print("Main Menu Options::")
        address_option_dict = {
            1: 'Exit',
            2: 'Display all entries',
            3: 'Add a new entry',
            4: 'Delete an entry',
            5: 'Search for an entry',
            6: 'Update an entry',
            7: 'Delete address book',
        }

        print(json.dumps(address_option_dict, indent=4))
        option = int(input("Select Option: "))

        return option

    def get_addressbook_name(self):
        self.datastore.set_tablename(input("Provide the name of your addressbook: "))

    def display_all_entries(self):
        self.all_entries_df = self.datastore.get_all_rows()
        print(self.all_entries_df)

    def add_new_entry(self):
        self.datastore.insert_data()
        self.datastore.commit()

    def delete_an_entry(self):
        id = int(input("Enter the ID value of the entry you want to delete :: "))
        self.datastore.delete_table(id)
        self.datastore.commit()
        print("Entry deleted successfully! ")

    def search_an_entry(self, name):
        # id = int(input("Enter the ID value of the entry you want to search :: "))
        self.all_entries_df = self.datastore.get_specific_row(name)
        print(self.all_entries_df)


if __name__ == '__main__':

    print("WELCOME TO ADDRESSBOOK")

    addr = Addressbook()
    db = DBase()
    db.connect()
    addr.set_datastore(db)

    addr.get_addressbook_name()

    while True:
        option = addr.display_main_menu()

        if option == 1:
            break

        elif option == 2:
            addr.display_all_entries()

        elif option == 3:
            addr.add_new_entry()

        elif option == 4:
            addr.delete_an_entry()

        elif option == 5:
            print("Search Options::")
            search_option_dict = {
                1: 'Press 1 for Name search',
                2: 'Press 2 for Address search',
                3: 'Press 3 for City search',
                4: 'Press 4 for Zip search',
                5: 'Press 5 for Phone search',
            }

            print(json.dumps(search_option_dict, indent=4))
            option = int(input("Select Option: "))

            if option == 1:
                name_search = input("Enter the name here you want to search:: ")
                addr.search_an_entry(name_search)




