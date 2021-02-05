import datetime as dt
import pandas as pd
import datetime
import pandas_datareader as pdr
from yahoo_fin import stock_info as si
import time
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
#
# start_time = dt.datetime(2021, 1, 1)
# end_time = dt.datetime(2021, 1, 27)
# df = pdr.DataReader('AAPL', 'yahoo', start_time, end_time)
# print(df.head())
# print(df.tail())
#
# stk_price = si.get_live_price('AMZN')
# stk = str(stk_price)
# for i in range(10):
#     print('\r' + stk[:i], end='')
#     time.sleep(.15)
#
# for sticker in tickers:
#     url = finviz_url + sticker
#     req = Request(url=url, headers={'user-agent': 'my-app/0.0.1'})
#     resp = urlopen(req)
#     html = BeautifulSoup(resp, features="lxml")
#     news_table = html.find(id='news-table')
#     news_tables[sticker] = news_table
#
# print(news_tables)

stock_symbols = ['AAPL', 'MSFT', 'CTSH']
_finviz_url = 'https://finviz.com/quote.ashx?t='
_parsed_news = []

for stock_symbol in stock_symbols:
    _news_tables = {}
    _stock_symbol = stock_symbol.upper()

    _url = _finviz_url + stock_symbol
    _req = Request(url=_url, headers={'user-agent': 'my-app/0.0.1'})
    _resp = urlopen(_req)
    _html = BeautifulSoup(_resp, features="lxml")
    _news_table = _html.find(id='news-table')
    _news_tables[stock_symbol] = _news_table

    incre = 1
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
            _parsed_news.append([ticker, _date, _time, _text[:300]])
            incre += 1
            if incre > 3:
                break


_columns = ['Ticker', 'Date', 'Time', 'Headline']
_news = pd.DataFrame(_parsed_news, columns=_columns)
print(_news)

millsec = ':00.0000000'
for index, rows in _news.iterrows():
    rows_list = list(rows.values)
    print(rows_list[0], end=' ')
    print(rows_list[1], end=' ')
    print(rows_list[2][:5]+millsec, end=' ')
    print(rows_list[3], sep='\r')
    # for val in rows_list:
    #     print(val, end=':')

