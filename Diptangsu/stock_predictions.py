import time
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)



finviz_news__url = 'https://finviz.com/quote.ashx?t='
symbols = ['AMZN', 'GOOG', 'FB']

news_tables = {}
stock_details_tables = []

for symbol in symbols:
    url = finviz_news__url + symbol
    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)
    soup = BeautifulSoup(response, 'html.parser')
    news_table = soup.find(id='news-table')
    news_tables[symbol] = news_table

news_table_parsed = []
#
# while True:
#
#     for symbol, news_table in news_tables.items():
#         for row in news_table.findAll('tr'):
#
#             title = row.a.get_text()
#             date_data = row.td.text.split(" ")
#
#             if len(date_data) == 1:
#                 time1 = date_data[0]
#
#             else:
#                 date = date_data[0]
#                 time1 = date_data[1]
#
#             news_table_parsed.append([symbol, date, time, title])
#
#     df = pd.DataFrame(news_table_parsed, columns=['symbols', 'date', 'time', 'title'])
#     print(df)
#     time.sleep(5)
#     break

for symbol in symbols:
    yahoo_finance_stock_url = 'https://finance.yahoo.com/quote/{}?p={}&.tsrc=fin-srch'.format(symbol, symbol)
    req = Request(url=yahoo_finance_stock_url, headers={'user-agent': 'my-app'})
    response = urlopen(req)
    soup = BeautifulSoup(response, 'html.parser')
    stock_details = soup.find('div', {
        'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find(
        'h1').text.split(" ")
    stock_price = soup.find('div', {'class': "D(ib) Mend(20px)"}).find('span').text
    stock_change = soup.find('span',
                             {'class': "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"}).text.split(" ")
    stock_details_tables.append((stock_details, stock_price, stock_change))
    print(stock_details_tables)

# Stock_details_tables = Stock_details_table
# print(Stock_details_tables)
