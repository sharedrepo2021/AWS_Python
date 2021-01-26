import pandas as pd
import pyodbc
from bs4 import BeautifulSoup
import datetime
import time
from urllib.request import urlopen
from urllib.request import Request
from yahoo_fin import stock_info as si


class StockPrice:
    def __init__(self):
        self.tickers = []
        self.stk_price = None
        pass

    def liveprice(self):
        self.stk_price = si.get_live_price(st.ticker)


class DatabaseConnect:
    def __init__(self):
        self.servername = None
        pass

    def connect(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server='+self.servername+';'
                                                             'Database=master;'
                                                             'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()


class StockTable(DatabaseConnect):
    def __init__(self):

        self.stock_dict = {
            "ticker": '',
            "tkr_price": '',
            "tkr_tracker": '',
            "news_day": '',
            "news_time": '',
            "news_header": '',
            "updated_time": ''
        }

        self.mytable = None
        self.tableexist = None
        self.schemaexist = None
        self.mytable_schema = None
        self.mytable_name = None
        self.ticker = None
        self.table_stk_value = None
        self.tracker = 0
        self.table_news_hd = None
        self.table_max_newsID = None

    def tablestatus(self):
        sql = "SELECT * from information_schema.tables where table_schema = '{0}' and table_name ='{1}'" \
            .format(self.mytable_schema, self.mytable_name)
        self.cursor.execute(sql)
        self.tableexist = self.cursor.fetchone()

    def schemastatus(self):
        sql = "SELECT * from information_schema.tables where table_schema = '{0}'" \
            .format(self.mytable_schema)
        self.cursor.execute(sql)
        self.schemaexist = self.cursor.fetchone()

    def createschema(self):
        sql = "CREATE SCHEMA {0}".format(self.mytable_schema)
        self.cursor.execute(sql)
        sql = 'COMMIT'
        self.cursor.execute(sql)

    def createstktable(self):
        sql = "CREATE TABLE {0} (newsID int IDENTITY(1,1) PRIMARY KEY, ticker varchar(4), tkr_price varchar(15),\
         tkr_tracker varchar(5), news_day varchar(10), news_time varchar(7), news_header varchar(200),\
          updated_time datetime)".format(self.mytable)
        self.cursor.execute(sql)
        sql = 'COMMIT'
        self.cursor.execute(sql)

    def addstock(self):
        placeholders = ', '.join(['?'] * len(self.stock_dict))
        columns = ', '.join(self.stock_dict.keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )  " % (self.mytable, columns, placeholders)
        value = tuple(self.stock_dict.values())
        self.cursor.execute(sql, value)
        sql = 'COMMIT'
        self.cursor.execute(sql)

    def selectall(self):
        sql = "SELECT * from {0} where ticker = '{1}' " \
            .format(self.mytable, self.ticker)
        self.sql1 = pd.read_sql_query(sql, self.conn)

    def selectlatestnews(self):
        st.findlastetnewsid()
        sql = "SELECT news_header from {0} where ticker = '{1}' and newsID = {2}" \
            .format(self.mytable, self.ticker, st.table_max_newsID)
        self.sql1 = pd.read_sql_query(sql, self.conn)
        self.table_news_hd = self.sql1['news_header'][0]

    def findlastetnewsid(self):
        sql = "SELECT MAX(newsID) as newsID from {0} where ticker = '{1}' ".format(self.mytable, self.ticker)
        self.sql1 = pd.read_sql_query(sql, self.conn)
        self.table_max_newsID = self.sql1['newsID'][0]

    def updatestktable(self):
        st.findlastetnewsid()
        sql = "UPDATE {0} SET tkr_tracker = '{1}' where ticker = '{2}' and newsID = {3} " \
            .format(self.mytable, self.table_stk_tracker, self.ticker, st.table_max_newsID)
        self.cursor.execute(sql)
        sql = 'COMMIT'
        self.cursor.execute(sql)

    def gettableprice(self):
        st.findlastetnewsid()
        sql = "SELECT tkr_price, tkr_tracker FROM {0} where ticker = '{1}' and newsID = {2} " \
            .format(self.mytable, self.ticker, st.table_max_newsID)
        self.sql1 = pd.read_sql_query(sql, self.conn)
        self.table_stk_value = float(self.sql1['tkr_price'][0])
        self.table_stk_tracker = float(self.sql1['tkr_tracker'][0])

    def printstatistics(self):
        try:
            print("\n[********************************* STOCK TREND STATISTICS ***********************************]\n")
            for st.ticker in tickers:
                sp.liveprice()
                new_price = float(sp.stk_price)
                st.gettableprice()
                if st.table_stk_tracker > 3:
                    trend = 'UP'
                elif 3 >= st.table_stk_tracker >= 0:
                    trend = 'NEUTRAL'
                else:
                    trend = 'DOWN'
                blk = 4 - len(st.ticker)
                print('Ticker : ', st.ticker, ' '*blk, '   ', 'News Time Price : ', "{:.2f}".format(st.table_stk_value),
                      '   ', 'Current Price : ', "{:.2f}".format(new_price), '   ', 'Trend : ', trend)
            print("\n[********************************************************************************************]\n")
        except KeyError:
            pass

    def stockanalysis(self):
        try:
            print('\n')
            print("INITIATING STOCK ANALYSIS....\n")
            for j in range(steps):
                for st.ticker in tickers:
                    sp.liveprice()
                    stock_p = "{:.2f}".format(sp.stk_price)
                    new_price = float(stock_p)
                    st.gettableprice()
                    if new_price > st.table_stk_value:
                        st.table_stk_tracker = st.table_stk_tracker + 1
                    elif new_price < st.table_stk_value:
                        st.table_stk_tracker = st.table_stk_tracker - 1
                    st.updatestktable()
                    if j == 0:
                        str_p = 'Analyzing news data for : ' + st.ticker
                    elif j == 1:
                        str_p = 'Fetching Price data for : ' + st.ticker
                    elif j == 2:
                        str_p = 'Finalizing trend data for : ' + st.ticker
                    for k in range(50):
                        print('\r' + str_p[:k], end='')
                        time.sleep(.10)
                    print('\r', end='')
            print('\r' + ' ' * 50, end='')
        except KeyError:
            pass


if __name__ == '__main__':

    sp = StockPrice()
    st = StockTable()

    schema = 'finance'
    ftable = 'stock_db'
    fin_table = 'finance.stock_db'
    choice = 1

    st.servername = input("\nPlease Enter the SQL Server Name : ")

    st.connect()

    st.mytable_schema = schema
    st.mytable_name = ftable
    st.mytable = fin_table
    st.schemastatus()
    if st.schemaexist:
        pass
    else:
        st.createschema()
        print("SCHEMA CREATED")

    st.tablestatus()
    if st.tableexist:
        pass
    else:
        st.createstktable()
        print("STOCK TABLE CREATED!")

    print("\nSTARTING STOCK TREND ANALYZER .....\n")

    num_of_news = 4
    tickers = ['AAPL', 'SPY', 'BABA']

    finviz_url = 'https://finviz.com/quote.ashx?t='
    news_tables = {}
    time.sleep(.5)
    while choice != 0:
        if choice == 1:
            try:
                for st.ticker in tickers:
                    url = finviz_url + st.ticker
                    req = Request(url=url, headers={'user-agent': 'my-app/0.0.1'})
                    resp = urlopen(req)
                    html = BeautifulSoup(resp, features="lxml")
                    news_table = html.find(id='news-table')
                    news_tables[st.ticker] = news_table
                try:
                    for st.ticker in tickers:
                        df = news_tables[st.ticker]
                        df_tr = df.findAll('tr')
                        print('\n')
                        print('Recent News Headlines for {}: '.format(st.ticker))
                        sp.liveprice()
                        for i, table_row in enumerate(df_tr):
                            a_text = table_row.a.text
                            td_text = table_row.td.text
                            td_text = td_text.strip()
                            td_text_date = td_text[:10]
                            td_text_time = td_text[10:]
                            if td_text_time != '':
                                temp_date = td_text_date
                            else:
                                td_text_time = td_text_date[:7]
                            print('[', temp_date, td_text_time, ']', a_text)
                            if i == 0:
                                st.stock_dict['ticker'] = st.ticker
                                st.stock_dict['tkr_price'] = sp.stk_price
                                st.stock_dict['tkr_tracker'] = 0
                                st.stock_dict['news_day'] = temp_date
                                st.stock_dict['news_time'] = td_text_time
                                st.stock_dict['news_header'] = a_text
                                st.stock_dict['updated_time'] = datetime.datetime.now()
                                st.selectall()
                                if not st.sql1.empty:
                                    st.selectlatestnews()
                                    if st.table_news_hd == a_text:
                                        pass
                                    else:
                                        st.addstock()
                                else:
                                    st.addstock()
                            if i == num_of_news - 1:
                                break
                        time.sleep(1)
                except KeyError:
                    pass
                steps = 3
                st.stockanalysis()
                st.printstatistics()
            except:
                break
        while True:
            try:
                choice = int(input("Key in 1 to CONTINUE or 0 to EXIT : "))
                break
            except:
                print("\n !!!INVALID CHOICE. PLEASE TRY AGAIN!!!\n")
        print("\n")
