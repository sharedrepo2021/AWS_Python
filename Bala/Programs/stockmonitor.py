import json
import pyodbc
import pandas as pd
import datetime as dt


from yahoo_fin import stock_info as si
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

class LoadSymbolDataFrame:
    def __init__(self):
        self.nasdaq_csv = r'https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv'
        self.nyse_csv = r'https://pkgstore.datahub.io/core/nyse-other-listings/other-listed_csv/data/9f38660d84fe6ba786a4444b815b3b80/other-listed_csv.csv'
        self.stk_sym_df = None

    def load_sym_table(self):
        _nasdaq_data = pd.read_csv(self.nasdaq_csv, usecols=['Symbol', 'Company Name'])
        _nyse_data = pd.read_csv(self.nyse_csv, usecols=['ACT Symbol', 'Company Name'])
        _nasdaq_data.columns = ['Ticker_Symbol', 'Stock_Name']
        _nyse_data.columns = ['Ticker_Symbol', 'Stock_Name']

        _nasdaq_nyse_data = pd.concat([_nasdaq_data, _nyse_data], ignore_index=True)
        return(_nasdaq_nyse_data)

class HandleDataBaseOperations:
    def __init__(self):
        self.db_connection = None
        self.db_cursor = None

        self.db_db = 'StockMonitor'
        self.db_schema = 'Stock'

    def establish_db_connection(self):
        try:
            self.db_connection = pyodbc.connect('Driver={SQL Server};'
                                       'Server=BALALENR7\SQLEXPRESS;'
                                       'Database=StockMonitor;'
                                       'Trusted_Connection=yes;')

            self.db_cursor = self.db_connection.cursor()
        except Exception:
            print('Database Connection Failed !!!')

    def commit_database(self):
        try:
            self.db_cursor.execute('COMMIT')
        except Exception:
            print('COMMIT Failed !!!')

    def delete_stk_sym_table(self):
        try:
            _deleteqry = 'DELETE FROM {}.{}.STK_SYMBOL_DETAILS;'.format(self.db_db, self.db_schema)
            self.db_cursor.execute(_deleteqry)
        except:
            print('SQL Error while deleting all rows from STK_SYMBOL_DETAILS table !!!')

    def insert_stk_sym_table(self, insertdf):
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        _insert_df = insertdf
        try:
            for index, rows in _insert_df.iterrows():
                _rows_str = rows.Stock_Name.replace("'", "")
                _insertqry = "INSERT INTO {}.{}.STK_SYMBOL_DETAILS " \
                            "VALUES ({}, '{}', '{}', '{}')".format(self.db_db, self.db_schema, index,
                                                                rows.Ticker_Symbol, _rows_str, _curr_date_time)
                self.db_cursor.execute(_insertqry)
        except:
            print('SQL Error while inserting rows from STK_SYMBOL_DETAILS table !!!')


if __name__ == '__main__':

    option_dict = {
        0: 'Exit from the Application',
        1: 'Refresh the Stock Symbols',
        2: 'List User Favourite Stocks'
    }

    # Establish the Connections with Database
    handle_db = HandleDataBaseOperations()
    handle_db.establish_db_connection()

    while True:
        print("Select an Option: ")
        print(json.dumps(option_dict, indent=4))
        option = input("Select Option: ")

        if option == '0':
            break
        elif option == '1':
            # These statements below loads the latest stock in to a STK_SYMBOL_DETAILS
            load_symbol = LoadSymbolDataFrame()
            load_symbol_df = load_symbol.load_sym_table()
            handle_db.delete_stk_sym_table()
            handle_db.insert_stk_sym_table(load_symbol_df)
            handle_db.commit_database()
            print('STK_SYMBOL_DETAILS Loaded Successfully.')
        elif option == '2':
            # These statements below handles User's Favourite Stocks
            load_symbol = LoadSymbolDataFrame()
            load_symbol_df = load_symbol.load_sym_table()
            handle_db.delete_stk_sym_table()
            handle_db.insert_stk_sym_table(load_symbol_df)
            handle_db.commit_database()
            print('STK_SYMBOL_DETAILS Loaded Successfully.')
        else:
            print('An Invalid Option. Try Valid Option !!!')
