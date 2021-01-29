import time
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd
import pyodbc
from fast_to_sql import fast_to_sql as fts

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


class Database:

    def __init__(self):
        self.conn = None
        self.query = None
        self.value = None
        self.my_cursor = None

    def connect(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=DESKTOP-2OIFI6J\SQLEXPRESS;'
                                   'Database=Stock_details;'
                                   'Trusted_Connection=yes;')
        self.my_cursor = self.conn.cursor()
        return self.my_cursor

    def create_stock_news_table(self):
        news_df = stock_news()
        fts.fast_to_sql(news_df, "stock_news_table", self.conn, if_exists="append", temp=False)

    def create_favourites_stock_table(self):
        favourites_df = stock_data()
        fts.fast_to_sql(favourites_df, "favourite_stock_table", self.conn, if_exists="append", temp=False)



    def commit(self):
        self.conn.commit()


finviz_news__url = 'https://finviz.com/quote.ashx?t='
symbols = ['AMZN']


def stock_news():
    news_tables = {}

    for symbol in symbols:
        url = finviz_news__url + symbol
        req = Request(url=url, headers={'user-agent': 'my-app'})
        response = urlopen(req)
        soup = BeautifulSoup(response, 'html.parser')
        news_table = soup.find(id='news-table')
        news_tables[symbol] = news_table

    news_table_parsed = []

    for symbol, news_table in news_tables.items():
        for row in news_table.findAll('tr'):

            title = row.a.get_text()
            date_data = row.td.text.split(" ")

            if len(date_data) == 1:
                time1 = date_data[0]

            else:
                date = date_data[0]
                time1 = date_data[1]

            news_table_parsed.append([symbol, date, time1, title])

    df = pd.DataFrame(news_table_parsed, columns=['symbols', 'date', 'time', 'title'])
    return df


def stock_data():
    stock_details_tables = {}
    stock_details_list = []

    for symbol in symbols:
        yahoo_finance_stock_url = 'https://finance.yahoo.com/quote/{}?p={}&.tsrc=fin-srch'.format(symbol, symbol)
        req = Request(url=yahoo_finance_stock_url, headers={'user-agent': 'my-app'})
        response = urlopen(req)
        soup = BeautifulSoup(response, 'html.parser')
        stock_details_table = soup.find('div', {
            'class': "quote-header-section Cf Pos(r) Mb(5px) Bgc($lv2BgColor) Maw($maxModuleWidth) Miw($minGridWidth) smartphone_Miw(ini) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) Mend(a) Px(20px) smartphone_Pb(0px) smartphone_Mb(0px)"})
        stock_details_tables[symbol] = stock_details_table

    for symbol, stock_details_table in stock_details_tables.items():
        for key in stock_details_table.findAll('h1'):
            text = key.get_text().split(" ")
            tickers = text[2].replace('(', '').replace(')', '')
            title = text[0].replace(',', '')

        for key in stock_details_table.findAll('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}):
            value = key.get_text()

        stock_details_list.append([tickers, title, value])
    df = pd.DataFrame(stock_details_list, columns=['symbols', 'company_name', 'value'])
    return df


if __name__ == "__main__":
    db = Database()

    db.connect()

    db.create_stock_news_table()
    db.commit()

    db.create_favourites_stock_table()
    db.commit()


