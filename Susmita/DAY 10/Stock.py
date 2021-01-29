import datetime
import json
from urllib.request import urlopen, Request

import pandas as pd
import pyodbc
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from yahoo_earnings_calendar import YahooEarningsCalendar
from yahoo_fin import stock_info as si


def print_formatted(df):
    from tabulate import tabulate
    print(tabulate(df, headers='keys', tablefmt='psql'))


def print_header(text):
    print('=' * (len(text) + 2))
    print('{} ::'.format(text))
    print('=' * (len(text) + 2))


class DatabaseHandler:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.schema = None

    def connect(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=DESKTOP-1HL1TR2\SQLEXPRESS;'
                                   'Database=AdventureWorks2019;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    def set_schema(self, schema):
        self.schema = schema

    def commit(self):
        query = 'COMMIT'
        self.cursor.execute(query)

    def create_tables(self):
        try:
            _sql = '''
            IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='Stock_Symbols' and xtype='U')
                CREATE TABLE [Susmita].[Stock_Symbols](
                    Symbol [varchar](10) PRIMARY KEY NOT NULL,
                    StockName [varchar](255) NOT NULL,
                    Current_Price DECIMAL(10,2) NOT NULL,
                    Market_Cap [varchar](255) NULL,
                    Country [varchar](255) NULL,
                    IPO_Year [varchar](255) NULL,
                    Volume [varchar](255) NULL,
                    Sector [varchar](255) NULL,
                    Industry [varchar](255) NULL,
                    Update_DateTime DateTime NOT NULL
                ) ON [PRIMARY]
            '''
            self.cursor.execute(_sql)

            _sql = '''
            IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='[FavStocks]' and xtype='U')
                CREATE TABLE [Susmita].[FavStocks](
                    Symbol [varchar](10) PRIMARY KEY NOT NULL,
                    StockName [varchar](255) NOT NULL
                ) ON [PRIMARY]
            '''

        except Exception as e:
            print('Unable to create tables...Error: {}'.format(e))
        else:
            self.commit()

    def load_stock_symbols_table(self, df):
        _row = None
        _sql = None
        try:
            self.delete_table_data('Stock_Symbols')
            _current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

            for _index, _row in df.iterrows():
                _sql = "INSERT INTO {}.Stock_Symbols ([Symbol], [StockName], [Current_Price], [Market_Cap], " \
                       "[Country], [IPO_Year], [Volume], [Sector], [Industry], [Update_DateTime]) " \
                       "values('{}','{}',{},'{}','{}','{}', '{}','{}','{}','{}')". \
                    format(self.schema, _row.Symbol, _row.StockName, _row.Current_Price, _row.Market_Cap, _row.Country,
                           _row.IPO_Year, _row.Volume, _row.Sector, _row.Industry, _current_time)
                self.cursor.execute(_sql)

        except Exception as e:
            print('Error in inserting data to [Stock_Symbols] table...Error: {}'.format(e))
            print(_sql)
        else:
            self.commit()

    def execute_sql_and_commit(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print('Error in executing...Query: {}...Error: {}'.format(sql, e))
            return False
        else:
            self.commit()
            return True

    def delete_table_data(self, table_name):
        try:
            _sql = "DELETE FROM {}.{}".format(self.schema, table_name)
            self.cursor.execute(_sql)

        except Exception as e:
            print('Error in deleting data from {} table...Error: {}'.format(table_name, e))
        else:
            self.commit()

    def execute_sql(self, sql):
        try:
            sql_query_df = pd.read_sql_query(sql, self.conn)
        except Exception as e:
            print('Unable to execute query: {}...Error: {}'.format(sql, e))
        else:
            return sql_query_df

    def disconnect(self):
        self.cursor.close()


class StockHandler:
    def __init__(self, db):
        # https://www.nasdaq.com/market-activity/stocks/screener?exchange=NASDAQ&render=download
        self.stock_symbol_nyse_path = r'C:\Users\dipan\Downloads\NYSE.csv'
        self.stock_symbol_nasdaq_path = r'C:\Users\dipan\Downloads\NASDAQ.csv'
        self.finwiz_url = 'https://finviz.com/quote.ashx?t='

        self.db = db
        self.db.create_tables()

    def refresh_stock_symbols(self):
        print('[i] Refreshing Stock Symbols...')
        _stock_symbol_data_nyse = pd.read_csv(self.stock_symbol_nyse_path)
        _stock_symbol_data_nasdaq = pd.read_csv(self.stock_symbol_nasdaq_path)
        _stock_symbol_data = pd.concat([_stock_symbol_data_nyse, _stock_symbol_data_nasdaq], ignore_index=True)
        _stock_symbol_data.drop_duplicates(subset=None, keep='first', inplace=True, ignore_index=True)
        _stock_symbol_data.sort_values(by=['Symbol'], inplace=True)

        _stock_symbol_data.rename({'Name': 'StockName', 'Last Sale': 'Current_Price', 'Market Cap': 'Market_Cap',
                                   'IPO Year': 'IPO_Year'}, axis=1, inplace=True)
        _stock_symbol_data.drop(['Net Change', '% Change'], axis=1, inplace=True)

        _stock_symbol_data['Current_Price'] = _stock_symbol_data['Current_Price'].str.replace(',', ''). \
            str.replace('$', '')
        _stock_symbol_data['Current_Price'] = _stock_symbol_data['Current_Price'].fillna(0)
        _stock_symbol_data = _stock_symbol_data.applymap(
            lambda x: x.strip().replace("'", '') if isinstance(x, str) else x)

        _stock_symbol_data = _stock_symbol_data.astype({'Current_Price': 'float64'})
        self.db.load_stock_symbols_table(_stock_symbol_data)
        print('[i] Stock Symbols refreshed...')

    def search_stock_using_symbol(self, stock_symbol):
        _table_name = 'Stock_Symbols'
        _sql = "SELECT * FROM {}.{} WHERE Symbol = '{}'".format(self.db.schema, _table_name, stock_symbol)
        resultset = self.db.execute_sql(_sql)
        return resultset

    def search_stock_using_name(self, stock_name):
        _table_name = 'Stock_Symbols'
        _sql = "SELECT * FROM {}.{} WHERE UPPER(StockName) LIKE '%{}%'".format(self.db.schema, _table_name, stock_name)
        resultset = self.db.execute_sql(_sql)
        return resultset

    def add_to_favorites(self, stock_symbol):
        _table_name = 'FavStocks'
        _stock_df = self.search_stock_using_symbol(stock_symbol)
        if _stock_df.empty:
            print('Unable to find stock with this symbol')
        else:
            _stock_name = _stock_df.iloc[0][1]
            _sql = "INSERT INTO {}.{} ([Symbol], [StockName]) values('{}','{}')". \
                format(self.db.schema, _table_name, stock_symbol, _stock_name)
            if self.db.execute_sql_and_commit(_sql):
                print('Stock added to Favorites...')
            else:
                print('Unable to add stock to Favorites...')

    def delete_from_favorites(self, stock_symbol):
        _table_name = 'FavStocks'
        _sql = "DELETE FROM {}.{} WHERE Symbol = '{}'".format(self.db.schema, _table_name, stock_symbol)
        if self.db.execute_sql_and_commit(_sql):
            print('Stock deleted from Favorites...')
        else:
            print('Unable to delete stock to Favorites...')

    def get_favorites(self):
        _table_name = 'FavStocks'
        _sql = "SELECT * FROM {}.{}".format(self.db.schema, _table_name)
        _resultset = self.db.execute_sql(_sql)
        return _resultset

    def get_favorites_list(self):
        _resultset = self.get_favorites()
        return _resultset['Symbol'].tolist()

    def show_favorites(self):
        print_formatted(self.get_favorites())

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

    def update_stock_price(self, stock_symbol, current_price):
        _current_price = round(current_price, 2)
        _table_name = 'Stock_Symbols'
        _current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        _sql = "UPDATE {}.{} SET [Current_Price] = {}, [Update_DateTime] = '{}' WHERE [Symbol] = '{}'". \
            format(self.db.schema, _table_name, _current_price, _current_time, stock_symbol)
        self.db.execute_sql_and_commit(_sql)

    def get_live_stock_price(self, stock_symbol):
        _current_price = si.get_live_price(stock_symbol)
        self.update_stock_price(stock_symbol, _current_price)
        return _current_price

    @staticmethod
    def get_analysts_info(stock_symbol):
        _analysts_info = si.get_analysts_info(stock_symbol)
        for key, value in _analysts_info.items():
            print_header(key)
            print_formatted(value)

    @staticmethod
    def get_balance_sheet(stock_symbol):
        _balance_sheet = si.get_balance_sheet(stock_symbol)
        print_formatted(_balance_sheet)

    @staticmethod
    def get_all_tickers():
        _tickers = si.tickers_sp500() + si.tickers_nasdaq() + si.tickers_other() + si.tickers_dow()
        _tickers = sorted(list(set(_tickers)))
        print(_tickers)
        print(len(_tickers))

    @staticmethod
    def get_stats(stock_symbol):
        _stats = si.get_stats(stock_symbol)
        print(_stats)

    def show_upcoming_calendar(self):
        print('Showing calendar for upcoming 3 days :')
        _date_from = datetime.datetime.now()
        _date_to = _date_from + datetime.timedelta(days=3)

        _yec = YahooEarningsCalendar()
        _df = pd.DataFrame(_yec.earnings_between(_date_from, _date_to))
        _df = _df.loc[_df['ticker'].isin(self.get_favorites_list())]
        print_formatted(_df)

    @staticmethod
    def remove_stopwords(text):
        text_tokens = word_tokenize(text)
        tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
        return tokens_without_sw


if __name__ == '__main__':
    db = DatabaseHandler()
    db.connect()
    db.set_schema('Susmita')

    sh = StockHandler(db)

    while True:
        print('\n')
        print("Select an Option::")
        search_option_dict = {
            0: 'Exit',
            1: 'Refresh the Stock Symbols from NASDAQ',
            2: 'Search stock by Symbol',
            3: 'Search stock by Name',
            4: 'Get live stock price',
            5: 'Get live stock news',
            6: 'Show upcoming event calendar',
            7: 'Add Stock to Favorites',
            8: 'Delete Stock from Favorites',
            9: 'Show Favorites',
            10: 'Get analysts info',
            11: 'Get balance sheet'
        }
        print(json.dumps(search_option_dict, indent=4))

        option = int(input("Select Option: "))
        if option == 0:
            break
        elif option == 1:
            sh.refresh_stock_symbols()
        elif option == 2:
            symbol = input("Enter symbol: ")
            print_formatted(sh.search_stock_using_symbol(symbol.upper()))
        elif option == 3:
            stock_name = input("Enter stock name: ")
            print_formatted(sh.search_stock_using_name(stock_name.upper()))
        elif option == 4:
            symbol = input("Enter symbol: ")
            print(sh.get_live_stock_price(symbol.upper()))
        elif option == 5:
            symbol = input("Enter symbol: ")
            if symbol:
                sh.print_live_stock_news([symbol.upper()])
            else:
                sh.print_live_stock_news(sh.get_favorites_list())
        elif option == 6:
            sh.show_upcoming_calendar()
        elif option == 7:
            symbol = input("Enter symbol: ")
            sh.add_to_favorites(symbol)
        elif option == 8:
            symbol = input("Enter symbol: ")
            sh.delete_from_favorites(symbol)
        elif option == 9:
            sh.show_favorites()
        elif option == 10:
            symbol = input("Enter symbol: ")
            sh.get_analysts_info(symbol)
        elif option == 11:
            symbol = input("Enter symbol: ")
            sh.get_balance_sheet(symbol)
        else:
            print('Invalid option')

    db.disconnect()
