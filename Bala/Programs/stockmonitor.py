import json
import pyodbc
import time
import pandas as pd
import datetime as dt

from tabulate import tabulate
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
        pass

    def establish_db_connection(self):
        global db_connection, db_cursor

        try:
            db_connection = pyodbc.connect('Driver={SQL Server};'
                                       'Server=BALALENR7\SQLEXPRESS;'
                                       'Database=StockMonitor;'
                                       'Trusted_Connection=yes;')

            db_cursor = db_connection.cursor()
        except Exception:
            print('Database Connection Failed !!!')

    def commit_database(self):
        try:
            db_cursor.execute('COMMIT')
        except Exception:
            print('COMMIT Failed !!!')

class HandleStockSymbolTable:
    def __init__(self):
        global db_name, db_schema

    def delete_stk_sym(self):
        try:
            _deleteqry = 'DELETE FROM {}.{}.STK_SYMBOL_DETAILS;'.format(db_name, db_schema)
            db_cursor.execute(_deleteqry)
        except:
            print('SQL Error while deleting all rows from STK_SYMBOL_DETAILS table !!!')

    def select_stk_sym(self, stk_sym_id):
        try:
            _selectqry = "SELECT * FROM {}.{}.STK_SYMBOL_DETAILS " \
                         "WHERE Stk_Sym_Symbol='{}';".format(db_name, db_schema, stk_sym_id)
            _sql1 = pd.read_sql_query(_selectqry, db_connection)
            return(_sql1.shape[0])
        except:
            print('error Enter Valid Stock-Symbol-ID !!!')

    def insert_stk_sym(self, insertdf):
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        _insert_df = insertdf
        try:
            for index, rows in _insert_df.iterrows():
                _rows_str = rows.Stock_Name.replace("'", "")
                _insertqry = "INSERT INTO {}.{}.STK_SYMBOL_DETAILS " \
                            "VALUES ({}, '{}', '{}', '{}')".format(db_name, db_schema, index,
                                                                   rows.Ticker_Symbol, _rows_str, _curr_date_time)
                db_cursor.execute(_insertqry)
        except:
            print('SQL Error while inserting rows from STK_SYMBOL_DETAILS table !!!')

class HandleFavUsrStkSymTable:
    def __init__(self):
        global db_name, db_schema, db_user_id

    def select_fav_usr_stk_sym(self):
        try:
            _selectqry = 'SELECT Fav_Usr_Stk_Sym_ID as Symbol_ID, Fav_Usr_Stk_Symbol as Stock_Symbol, ' \
                         'Fav_Usr_Stk_Name as Stock_Name FROM {}.{}.FAV_USER_STK_SYMBOL_DETAILS ' \
                         'WHERE Fav_Usr_Stk_User_ID={} ;'.format(db_name, db_schema, db_user_id)
            _sql1 = pd.read_sql_query(_selectqry, db_connection)
            if (_sql1.shape[0] > 0):
                print(tabulate(_sql1, headers='keys', tablefmt="psql"))
            else:
                print('No Rows Selected !!!')
        except:
            print('Enter Valid User-ID !!!')


if __name__ == '__main__':

    db_connection = None
    db_cursor = None
    db_name = 'StockMonitor'
    db_schema = 'Stock'
    db_user_id = ''

    option_dict = {
        0: "Exit from the Application",
        1: "Refresh the Stock Symbols",
        2: "List User Favourite's Stocks",
        3: "Change User Favourite's Stocks"
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

            stock_symbol = HandleStockSymbolTable()
            stock_symbol.delete_stk_sym()

            str_print = 'STK_SYMBOL_DETAILS Refresh In-Progress ...'
            for k in range(50):
                print('\r' + str_print[:k], end='')
                time.sleep(.05)
            print('\r', end='')
            stock_symbol.insert_stk_sym(load_symbol_df)
            handle_db.commit_database()
            str_print = 'STK_SYMBOL_DETAILS Loaded Successfully!'
            for k in range(50):
                print('\r' + str_print[:k], end='')
                time.sleep(.05)
            print('\n')
            stock_symbol = None

        elif option == '2':
            # These statements below list User Favourite's Stocks
            db_user_id = input('Enter User ID: ')
            if db_user_id.isnumeric():
                db_user_id = int(db_user_id)
                fav_usr_stk_sym = HandleFavUsrStkSymTable()
                fav_usr_stk_sym.select_fav_usr_stk_sym()
            else:
                print('Enter Valid User-ID !!!')

        elif option == '3':
            #These statements below updates User Favourite's Stocks
            db_user_id = input('Enter User ID: ')
            if db_user_id.isnumeric():
                db_user_id = int(db_user_id)
            chg_fav = input("Do You want to Add your Favourite's (Y/N): ").upper()
            if chg_fav == 'Y':
                fav_stk_sym = input('Enter Favourite Stock Symbol: ').upper()
                stock_symbol = HandleStockSymbolTable()
                if (stock_symbol.select_stk_sym(fav_stk_sym) > 0):
                    print('Stock Present')
                else:
                    print('Stock Not Present')

            chg_fav = input("Do You want to Delete your Favourite's (Y/N): ").upper()
            if chg_fav == 'Y':
                fav_stk_sym = input('Enter Favourite Stock Symbol: ').upper()
                stock_symbol = HandleStockSymbolTable()
                if (stock_symbol.select_stk_sym(fav_stk_sym) > 0):
                    print('Stock Present')
                else:
                    print('Stock Not Present')

        else:
            print('An Invalid Option. Try Valid Option !!!')

