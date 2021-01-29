from SQL_DB import DBase
import pandas as pd
from yahoo_fin import stock_info as si
import datetime
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from Send_Email import Email
import time


def print_formatted(df):
    from tabulate import tabulate
    print(tabulate(df, headers='keys', tablefmt='psql'))


class Stock:
    def __init__(self):
        self.email = Email()
        self.db = DBase()
        self.db.connect()
        self.stock_nasdaq_path = r"C:\Users\dipan\Downloads\All_Stocks.csv"
        self.finwiz_url = 'https://finviz.com/quote.ashx?t='

    def create_database(self):
        _query = '''
        IF NOT EXISTS ( SELECT  *
                FROM    sys.schemas
                WHERE   name = N'Susmita' )
        EXEC('CREATE SCHEMA [Susmita]');
        '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='STOCK_LIST' AND XTYPE='U')
        CREATE TABLE SUSMITA.STOCK_LIST(
            SYMBOL VARCHAR(255) PRIMARY KEY NOT NULL,
            STOCKNAME VARCHAR(255) NOT NULL
            )
        '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='FAVOURITES' AND XTYPE='U')
        CREATE TABLE SUSMITA.FAVOURITES(
            SYMBOL VARCHAR(255) PRIMARY KEY NOT NULL,
            PRICE DECIMAL(10,2),
            PRICE_INCREASE_COUNTER INT,
            UPDATE_DATE DATETIME NOT NULL
            )
        '''
        self.db.execute_sql_and_commit(_query)

        _query = '''
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='FAVOURITES_HISTORY' AND XTYPE='U')
        CREATE TABLE SUSMITA.FAVOURITES_HISTORY(
            SYMBOL VARCHAR(255) NOT NULL,
            PRICE DECIMAL(10,2),
            PRICE_CHANGE_AMOUNT DECIMAL(10,2),
            UPDATE_DATE DATETIME NOT NULL
            ) 
        '''
        self.db.execute_sql_and_commit(_query)

    def populate_stock_list(self):
        stock_df = pd.read_csv(self.stock_nasdaq_path)
        print(stock_df)

        _query = "DELETE FROM SUSMITA.STOCK_LIST"
        self.db.execute_sql_and_commit(_query)

        for index, row in stock_df.iterrows():
            _query = "INSERT INTO SUSMITA.STOCK_LIST (SYMBOL, STOCKNAME) VALUES('{}', '{}')".\
                    format(row.Symbol, row.StockName)
            self.db.execute_sql_and_commit(_query)

    def get_live_stock_price(self, stock_symbol):
        _current_price = si.get_live_price(stock_symbol)
        return _current_price

    def search_stock_with_symbol(self, stock_symbol):
        _query = "SELECT * FROM Susmita.STOCK_LIST WHERE SYMBOL = '{}';".format(stock_symbol)
        print_formatted(self.db.execute_sql(_query))

    def search_stock_with_name(self, text):
        _query = "SELECT * FROM Susmita.STOCK_LIST WHERE UPPER(STOCKNAME) LIKE '%{}%';".format(text.upper())
        print_formatted(self.db.execute_sql(_query))

    def add_to_favourites(self, stock_symbol):
        stock_price = self.get_live_stock_price(stock_symbol)
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        _query = "INSERT INTO SUSMITA.FAVOURITES (SYMBOL, PRICE, PRICE_INCREASE_COUNTER, UPDATE_DATE) " \
                 "VALUES('{}', {}, {}, '{}')".\
            format(stock_symbol, stock_price, 0, current_date)

        self.db.execute_sql_and_commit(_query)

    def delete_from_favourites(self, stock_symbol):
        _query = "DELETE FROM SUSMITA.FAVOURITES WHERE SYMBOL = '{}' ".format(stock_symbol)
        self.db.execute_sql_and_commit(_query)

    def get_favourites(self):
        _query = "SELECT * FROM SUSMITA.FAVOURITES"
        result_df = self.db.execute_sql(_query)
        return result_df

    def get_favourites_history(self, stock_symbol):
        _query = "SELECT TOP 3 * FROM SUSMITA.FAVOURITES_HISTORY WHERE SYMBOL = '{}' ORDER BY UPDATE_DATE DESC".format(stock_symbol)
        result_df = self.db.execute_sql(_query)
        return result_df

    def show_favourites(self):
        print_formatted(self.get_favourites())

    def update_favourites(self):
        result_df = self.get_favourites()

        for index, row in result_df.iterrows():
            current_price = round(self.get_live_stock_price(row.SYMBOL), 2)
            current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

            if current_price > row.PRICE:
                _query = "UPDATE SUSMITA.FAVOURITES SET PRICE = {}, PRICE_INCREASE_COUNTER = {}, UPDATE_DATE = '{}' WHERE SYMBOL = '{}'".format(current_price, row.PRICE_INCREASE_COUNTER + 1, current_date, row.SYMBOL)
            else:
                _query = "UPDATE SUSMITA.FAVOURITES SET PRICE = {}, PRICE_INCREASE_COUNTER = {}, UPDATE_DATE = '{}' WHERE SYMBOL = '{}'".format(current_price, 0, current_date, row.SYMBOL)
            self.db.execute_sql_and_commit(_query)

            _query = "INSERT INTO SUSMITA.FAVOURITES_HISTORY (SYMBOL, PRICE, PRICE_CHANGE_AMOUNT, UPDATE_DATE) VALUES('{}', {}, {}, '{}')".format(row.SYMBOL, current_price, current_price - row.PRICE, current_date)
            self.db.execute_sql_and_commit(_query)

        self.notify_user()

    def begin_autorun(self):
        time_interval = int(input("Time interval in minutes:: ")) * 60
        while True:
            print("Current Time:: {}".format(datetime.datetime.now()))
            self.update_favourites()
            time.sleep(time_interval)

    def delete_old_history(self):
        deletion_date = (datetime.datetime.now() - datetime.timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        _query = "DELETE FROM SUSMITA.FAVOURITES_HISTORY WHERE UPDATE_DATE < '{}' ".format(deletion_date)
        self.db.execute_sql_and_commit(_query)

    def notify_user(self):
        result_df = self.get_favourites()

        for index, row in result_df.iterrows():
            if row.PRICE_INCREASE_COUNTER == 3:
                history_df = self.get_favourites_history(row.SYMBOL)
                subject = "Favourite Stock [{}] price increase thrice in a row".format(row.SYMBOL)
                body = '''
                Price change history::\n
                {}\n\n
                
                Recent news::\n 
                {}
                '''.format(history_df, self.get_live_stock_news([row.SYMBOL]))

                self.email.send_email(subject, body)

                _query = "UPDATE SUSMITA.FAVOURITES SET PRICE_INCREASE_COUNTER = {} WHERE SYMBOL = '{}'".format(
                    0, row.SYMBOL)
                self.db.execute_sql_and_commit(_query)

    def get_live_stock_news(self, stock_symbols):
        _parsed_news = []
        for stock_symbol in stock_symbols:
            _news_tables = {}
            _stock_symbol = stock_symbol.upper()

            _url = self.finwiz_url + stock_symbol
            _req = Request(url=_url, headers={'user-agent': 'my-app/0.0.1'})
            _resp = urlopen(_req)
            _html = BeautifulSoup(_resp, features="lxml")
            _news_table = _html.find(id='news-table')
            _news_tables[stock_symbol] = _news_table

            # Iterate through the news
            for file_name, news_table in _news_tables.items():
                for x in news_table.findAll('tr'):
                    _text = x.a.get_text()
                    _date_scrape = x.td.text.split()

                    if len(_date_scrape) == 1:
                        _time = _date_scrape[0]
                    else:
                        _date = _date_scrape[0]
                        _time = _date_scrape[1]

                    ticker = file_name.split('_')[0]

                    _parsed_news.append([ticker, _date, _time, _text])

        _columns = ['Ticker', 'Date', 'Time', 'Headline']
        _news = pd.DataFrame(_parsed_news, columns=_columns)
        return _news

    def print_live_stock_news(self, stock_symbols):
        _stock_news = self.get_live_stock_news(stock_symbols)
        _number_of_news_to_Show = 3

        for _ticker in stock_symbols:
            _news_list = []

            print('\nRecent News Headlines for {}:'.format(_ticker))
            _ticker_stock_news = _stock_news.loc[_stock_news['Ticker'] == _ticker].head(_number_of_news_to_Show)

            for ind in _ticker_stock_news.index:
                _news_list.append('{} ( {} )'.format(_stock_news['Headline'][ind], _stock_news['Time'][ind]))

            print(*_news_list, sep='\n')


if __name__ == '__main__':

    st = Stock()
    st.create_database()
    # st.populate_stock_list()
    # st.add_to_favourites('CTSH')
    # st.delete_from_favourites('AAPL')
    # st.show_favourites()
    # st.print_live_stock_news(['AAPL'])
    # st.update_favourites()
    # st.notify_user()
    st.show_favourites()
    st.begin_autorun()

