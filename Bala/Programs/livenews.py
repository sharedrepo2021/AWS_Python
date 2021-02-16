from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import pandas as pd


_finviz_url = 'https://finviz.com/quote.ashx?t='
_parsed_news = []
_max_news = 1
arg_symbols_id = ['AAPL']

for _symbol_id in arg_symbols_id:
    _news_tables = {}
    _ticker_tables = {}
    _symbol_id_upper = _symbol_id.upper()


    _url = _finviz_url + _symbol_id_upper
    _req = Request(url=_url, headers={'user-agent': 'my-app/0.0.1'})
    _resp = urlopen(_req)
    _html = BeautifulSoup(_resp, features="lxml")

    _news_table = _html.find(id='news-table')
    _news_tables[_symbol_id_upper] = _news_table
    _increment_var = 1
    _news_date = ''
    _news_time = ''

    for file_name, news_table in _news_tables.items():
        for x in news_table.findAll('tr'):
            #print(x)
            _news_text = x.a.get_text()
            _date_scrape = x.td.text.split()
            if len(_date_scrape) == 1:
                _news_time = _date_scrape[0]
            else:
                _news_date = _date_scrape[0]
                _news_time = _date_scrape[1]

            _symbol_id = file_name.split('_')[0]
            _parsed_news.append([_symbol_id, _news_date, _news_time, _news_text[:300]])
            _increment_var += 1
            if _increment_var > _max_news:
                break

    _columns = ['Symbol', 'Date', 'Time', 'Headline']
    _news_latest = pd.DataFrame(_parsed_news, columns=_columns)



    _ticker_body = _html.find(class_ = "snapshot-table2")
    _ticker_tables[_symbol_id_upper] = _ticker_body
    print(_ticker_tables[_symbol_id_upper])

    # for fname, tdetails in _ticker_tables.items():
    #
    #     for tdet in tdetails.findAll('tr'):
    #         tdet_str = str(tdet)
    #         print(tdet_str)
    #         print(tdet_str.find('Prev Close'))
