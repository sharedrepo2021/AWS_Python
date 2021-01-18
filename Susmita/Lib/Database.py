import pyodbc
import pandas as pd


class DBase:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.table_name = None

    def connect(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-1HL1TR2\SQLEXPRESS;'
                              'Database=AdventureWorks2019;'
                              'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    def commit(self):
        query = 'COMMIT'
        self.cursor.execute(query)

    def get_tablename(self):
        return self.table_name

    def set_tablename(self, table_name):
        self.table_name = table_name

    def create_table(self):
        query = '''
        CREATE TABLE Susmita.{} (
            ID smallint NOT NULL IDENTITY(1,1),	
            Name varchar(255) NOT NULL,	
            Address varchar(255),
            City varchar(255),
            Zip varchar(25),
            Phone varchar(25)
            );
        '''.format(self.table_name)
        self.cursor.execute(query)

    def insert_data(self):
        _name = input("Enter name: ")
        _address = input("Enter address: ")
        _city = input("Enter city: ")
        _zip = input("Enter zip: ")
        _phone = input("Enter phone number: ")

        query = "INSERT INTO Susmita.{} VALUES('{}', '{}', '{}', '{}', '{}')" \
            .format(self.table_name, _name, _address, _city, _zip, _phone)
        self.cursor.execute(query)

    def drop_table(self):
        query = "DROP TABLE Susmita.{}".format(self.table_name)
        self.cursor.execute(query)

    def get_all_rows(self):
        query = "SELECT * FROM Susmita.{}".format(self.table_name)
        sql_query_df = pd.read_sql_query(query, self.conn)
        return sql_query_df

    def update_table(self, id):
        print("Now enter address, city, zip and phone number...")
        _address = input("Enter address: ")
        _city = input("Enter city: ")
        _zip = input("Enter zip: ")
        _phone = input("Enter phone number: ")

        query = '''
        UPDATE Susmita.{} 
        SET Address = '{}', City = '{}', Zip = '{}', Phone = '{}'
        WHERE ID = {};
        '''.format(self.table_name, _address, _city, _zip, _phone, id)

        self.cursor.execute(query)

    def delete_table(self, id):
        query = '''
        DELETE FROM Susmita.{} 
        WHERE ID = {};
        '''.format(self.table_name, id)

        self.cursor.execute(query)

    def get_specific_row(self, name):
        query = "SELECT * FROM Susmita.{} WHERE Name = '{}'".format(self.table_name, name)
        sql_query_df = pd.read_sql_query(query, self.conn)
        return sql_query_df


