import pyodbc
import json
import pandas as pd


class Library:

    def __init__(self):
        self.conn = None
        self.query = None
        self.value = None
        self.my_cursor = None

    def connect(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=DESKTOP-2OIFI6J\SQLEXPRESS;'
                                   'Database=library_management_system;'
                                   'Trusted_Connection=yes;')
        self.my_cursor = self.conn.cursor()
        return self.my_cursor

    def commit(self):
        self.conn.commit()

    def create_books_table(self):
        self.query = '''
         CREATE TABLE dbo.books (SL_No INT IDENTITY(1,1),
              book_name VARCHAR(50), 
              author VARCHAR(200),
              book_code VARCHAR(10), 
              book_quantity INT)
              '''
        self.my_cursor.execute(self.query)

    def create_books_issued_table(self):
        self.query = '''
            CREATE TABLE dbo.issued (SL_No INT IDENTITY(1,1),
                 candidate_name VARCHAR(50), 
                 phone_number INT, 
                 book_code VARCHAR(10),
                 issue_date DATE)
                 '''
        self.my_cursor.execute(self.query)

    def create_books_returned_table(self):
        self.query = '''
               CREATE TABLE dbo.returned (SL_No INT IDENTITY(1,1),
                    candidate_name VARCHAR(50), 
                    phone_number INT, 
                    book_code VARCHAR(10),
                    return_date DATE)
                    '''
        self.my_cursor.execute(self.query)

    def add_book(self):
        try:
            book_name = input("Enter book name: ")
            author_name = input("Enter the name of the author: ")
            book_code = input("Enter book code: ")
            book_quantity = input("Enter the number of books: ")

            self.query = '''INSERT INTO books VALUES ('{}', '{}', '{}', '{}')'''.format(
                book_name, author_name, book_code,
                book_quantity)

            self.my_cursor.execute(self.query)
            print("Book has been added successfully")
        except Exception as e:
            print("Please provide appropriate input. Error:", e)

    def issued_book(self):
        try:
            candidate_name = input("Enter candidates name: ")
            phone_number = int(input("Enter the candidates phone number: "))
            book_code = input("Enter book code: ")
            issue_date = input("Enter the date of issue(YYYY-MM-DD): ")

            self.query = '''INSERT INTO issued VALUES ('{}', '{}', '{}', '{}')'''.format(
                candidate_name, phone_number, book_code,
                issue_date)

            self.my_cursor.execute(self.query)
            print("Book has been issued to", candidate_name)
            self.update_book_table(book_code, -1)
        except Exception as e:
            print("Please provide appropriate input. Error:", e)

    def returned_book(self):
        try:
            candidate_name = input("Enter candidates name: ")
            phone_number = int(input("Enter the candidates phone number: "))
            book_code = input("Enter book code: ")
            return_date = input("Enter the date of return(YYYY-MM-DD: ")

            self.query = '''INSERT INTO returned VALUES ('{}', '{}', '{}', '{}')'''.format(
                candidate_name, phone_number, book_code,
                return_date)

            self.my_cursor.execute(self.query)
            print("Book has been returned successfully by", candidate_name)
            self.update_book_table(book_code, 1)
        except Exception as e:
            print("Please provide appropriate input. Error:", e)

    def update_book_table(self, book_code, update):
        self.query = '''
        Select book_quantity FROM books WHERE book_code = '{}'
        '''.format(book_code)
        result = self.my_cursor.execute(self.query).fetchone()
        total = result[0] + update

        self.query = '''
        UPDATE books SET book_quantity = '{}' WHERE book_code = '{}'
        '''.format(total, book_code)
        self.my_cursor.execute(self.query)

    def display_table(self):
        table_name = input("Enter the name of the table to be viewed: ")
        query = pd.read_sql_query('''SELECT * FROM dbo.{} '''.format(table_name), self.conn)
        df = pd.DataFrame(query)
        print(df)

    def delete_rows(self):
        try:
            self.display_table()
            field_value = input("Enter the Sl No. of the row you want to remove: ")
            table_name = input("Enter the name of the table: ")
            self.query = '''
            DELETE FROM dbo.{} WHERE SL_No = '{}'
                                '''.format(table_name, field_value)
            self.my_cursor.execute(self.query)
        except Exception as e:
            print("Please provide appropriate input. Error:", e)

    def update_row(self):
        self.display_table()
        table_name = input("Enter the name of the table you want to update: ")
        column_name = input("Enter the name of the column to be updated: ")
        column_value = input("Enter the updated value: ")
        field_value = input("Enter the serial number of the row to be updated: ")

        self.query = '''
                       UPDATE dbo.{} SET {} = '{}' WHERE SL_No = '{}'
                       '''.format(table_name, column_name, column_value, field_value)

        self.my_cursor.execute(self.query)


if __name__ == "__main__":

    lib = Library()
    lib.connect()
try:
    while True:

        option_dict = {
            1: 'Add Book',
            2: 'Issue Book',
            3: 'Submit Book',
            4: 'Delete Book',
            5: 'Exit',
            6: 'Display books table',
            7: 'Update table'
        }
        print(json.dumps(option_dict, indent=5))
        user_input = int(input('Please select an option: '))

        if user_input == 1:
            lib.add_book()
            lib.commit()
        elif user_input == 2:
            lib.issued_book()
            lib.commit()
        elif user_input == 3:
            lib.returned_book()
            lib.commit()
        elif user_input == 4:
            lib.delete_rows()
            lib.commit()
        elif user_input == 5:
            break
        elif user_input == 6:
            lib.display_table()
        elif user_input == 7:
            lib.update_row()
            lib.commit()
        else:
            print("Please select an appropriate option from the give list")
except Exception as e:
    print("Please provide appropriate input. Error:", e)




