import datetime as dt
import pandas as pd
import pandas_datareader as pdr
from yahoo_fin import stock_info as si
import time
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

# start_time = dt.datetime(2021, 1, 1)
# end_time = dt.datetime(2021, 1, 27)
# df = pdr.DataReader('AAPL', 'yahoo', start_time, end_time)
# print(df.head())
# print(df.tail())

# stk_price = si.get_live_price('AMZN')
# stk = str(stk_price)
# for i in range(10):
#     print('\r' + stk[:i], end='')
#     time.sleep(.15)

news_tables ={}
tickers = ['AAPL', 'SPY', 'BABA']
finviz_url = 'https://finviz.com/quote.ashx?t='
for sticker in tickers:
    url = finviz_url + sticker
    req = Request(url=url, headers={'user-agent': 'my-app/0.0.1'})
    resp = urlopen(req)
    html = BeautifulSoup(resp, features="lxml")
    news_table = html.find(id='news-table')
    news_tables[sticker] = news_table

print(news_tables)
