from SQL_DB import DBase
import pandas as pd


def print_formatted(df):
    from tabulate import tabulate
    print(tabulate(df, headers='keys', tablefmt='psql'))


class Stock:
    def __init__(self):
        self.db = DBase()
        self.db.connect()
        self.stock_nasdaq_path = r"C:\Users\Owner\Desktop\nasdaq_screener_1611713854464.csv"

    def create_database(self):
        _query = '''
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='STOCK_LIST' AND XTYPE='U')
        CREATE TABLE SUSMITA.STOCK_LIST(
            SYMBOL VARCHAR(255) PRIMARY KEY NOT NULL,
            STOCKNAME VARCHAR(255) NOT NULL,
            PRICE DECIMAL(10,2),
            UPDATE_DATE DATETIME NOT NULL
            )
        '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='FAVOURITES' AND XTYPE='U')
        CREATE TABLE SUSMITA.FAVOURITES(
            SYMBOL VARCHAR(255) PRIMARY KEY NOT NULL,
            PRICE_INCREASE_COUNTER INT,
            UPDATE_DATE DATETIME NOT NULL
            )
        '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='FAVOURITES_HISTORY' AND XTYPE='U')
        CREATE TABLE SUSMITA.FAVOURITES_HISTORY(
            SYMBOL VARCHAR(255) PRIMARY KEY NOT NULL,
            PRICE DECIMAL(10,2),
            PRICE_CHANGE_AMOUNT DECIMAL(10,2),
            UPDATE_DATE DATETIME NOT NULL
            ) 
        '''
        self.db.execute_sql_and_commit(_query)

    def populate_stock_list(self):
        stock_df = pd.read_csv(self.stock_nasdaq_path)
        print(stock_df)

    def search_stock(self, symbol):
        _query = "SELECT * FROM Susmita.STOCK_LIST WHERE SYMBOL = '{}';".format(symbol)
        print_formatted(self.db.execute_sql(_query))


if __name__ == '__main__':
    st = Stock()
    st.create_database()
    st.populate_stock_list()
