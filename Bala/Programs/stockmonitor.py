import json
import pyodbc
import time
import pandas as pd
import datetime as dt

from tabulate import tabulate
from datetime import datetime
from yahoo_fin import stock_info as si
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
from emailgmail import SendEmail

class GetRequDetails:
    def __init__(self):
        pass

    def get_conv_val_id(self, idname):
        _id_name = idname
        while True:
            if _id_name == 'user':
                _val_id = input('Enter User ID: ')
            elif _id_name == 'symbol':
                _val_id = input('Enter Stock Symbol ID: ')
            else:
                _val_id = 1
                print('Wrong Value !!!')

            if _val_id.isnumeric():
                _val_id = int(_val_id)
                return(_val_id)
            else:
                print('Enter Valid ID !!!')

    def get_live_stock_news(self, stock_symbols, maxnews):
        _parsed_news = []
        _finviz_url = 'https://finviz.com/quote.ashx?t='
        _max_news = maxnews

        for stock_symbol1 in stock_symbols:
            _news_tables = {}
            _stock_symbol1 = stock_symbol1.upper()

            _url = _finviz_url + stock_symbol1
            _req = Request(url=_url, headers={'user-agent': 'my-app/0.0.1'})
            _resp = urlopen(_req)
            _html = BeautifulSoup(_resp, features="lxml")
            _news_table = _html.find(id='news-table')
            _news_tables[stock_symbol1] = _news_table

            # Iterate through the news
            _incre = 1
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
                    _incre += 1
                    if _incre > _max_news:
                        break

        _columns = ['Ticker', 'Date', 'Time', 'Headline']
        _news = pd.DataFrame(_parsed_news, columns=_columns)
        return(_news)

class StockLivePrice:
    def __init__(self):
        pass

    def liveprice(self, stksymname):
        _stk_sym_name = stksymname
        return(float(si.get_live_price(_stk_sym_name)))

    def opendata(self, stksymname):
        _stk_sym_name = stksymname
        _today = dt.date.today()
        _open_df = pd.DataFrame(si.get_data(_stk_sym_name, start_date=_today))
        return(float(_open_df['open']))

    def closedata(self, stksymname):
        _stk_sym_name = stksymname
        _today = dt.date.today()
        _yesterday = _today - dt.timedelta(days=1)
        _close_df = pd.DataFrame(si.get_data(_stk_sym_name, start_date=_yesterday))
        for cdate, cprice in _close_df['close'].items():
            if str(cdate)[:10] == str(_yesterday):
                return(cprice)

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
                                       'Server=BALALENG50\SQLEXPRESS;'
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

class HandleUserDetailsTable:
    def __init__(self):
        global db_name, db_schema, user_id

    def select_user_details(self, usrid):
        user_id = int(usrid)
        try:
            _selectqry = "SELECT Stk_User_ID, Stk_User_First_Name, " \
                         "Stk_User_Email_ID, Stk_User_Rights FROM {}.{}.STK_USER_DETAILS " \
                         "WHERE Stk_User_ID = {} ;".format(db_name, db_schema, user_id)
            _sql1 = pd.read_sql_query(_selectqry, db_connection)
            return(_sql1.shape[0], _sql1['Stk_User_ID'].values, _sql1['Stk_User_First_Name'].values,
                   _sql1['Stk_User_Email_ID'].values, _sql1['Stk_User_Rights'].values)
        except:
            print('error Enter Valid Stock-Symbol-ID !!!')


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
            return(_sql1.shape[0], _sql1['Stk_Sym_ID'], _sql1['Stk_Sym_Symbol'], _sql1['Stk_Sym_Name'])
        except:
            print('error Enter Valid Stock-Symbol-ID !!!')

    def insert_stk_sym_df(self, insertdf):
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
        global db_name, db_schema, user_id

    def select_fav_usr_stk_sym(self, usrid, mode):
        user_id = int(usrid)
        _what_mode = mode
        try:
            _selectqry = 'SELECT Fav_Usr_Stk_Sym_ID, Fav_Usr_Stk_Symbol, ' \
                         'Fav_Usr_Stk_Name FROM {}.{}.FAV_USER_STK_SYMBOL_DETAILS ' \
                         'WHERE Fav_Usr_Stk_User_ID={} ;'.format(db_name, db_schema, user_id)
            _sql1 = pd.read_sql_query(_selectqry, db_connection)
        except:
            print('Enter Valid User-ID !!!')

        if (_sql1.shape[0] > 0 and _what_mode =='display'):
            return(_sql1)
        elif (_sql1.shape[0] > 0 and _what_mode == 'getsymbol'):
            return(_sql1['Fav_Usr_Stk_Symbol'])
        else:
            print('No Rows Selected !!!')

    def insert_fav_usr_stk_sym(self, symid, tsym, tname, usrid):
        _sym_id = int(symid)
        _sym_sym = tsym
        _sym_name = tname
        user_id = int(usrid)
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            _insertqry = "INSERT INTO {}.{}.FAV_USER_STK_SYMBOL_DETAILS " \
                         "VALUES ({},'{}','{}',{},'{}')".format(db_name, db_schema, _sym_id, _sym_sym,
                                                                _sym_name, user_id, _curr_date_time)
            print(_insertqry)
            db_cursor.execute(_insertqry)
        except:
            print('SQL Error while inserting rows from FAV_USER_STK_SYMBOL_DETAILS table !!!')

    def delete_fav_usr_stk_sym(self, tsym):
        _tick_sym = str(tsym)
        try:
            _deleteqry = "DELETE FROM {}.{}.FAV_USER_STK_SYMBOL_DETAILS " \
                         "WHERE Fav_Usr_Stk_Symbol = '{}'; ".format(db_name, db_schema, _tick_sym)
            db_cursor.execute(_deleteqry)
        except:
            print('SQL Error while deleting row from FAV_USER_STK_SYMBOL_DETAILS table !!!')

class HandleFavStkLivePriceTable:
    def __init__(self):
        global db_name, db_schema, user_id

    def select_fav_stk_live_price(self, usrid):
        user_id = int(usrid)
        try:
            _selectqry = "SELECT * FROM {}.{}.FAV_STK_LIVE_PRICE_DETAILS " \
                         "WHERE Fav_Stk_Live_User_ID = '{}' ORDER BY Fav_Stk_Live_User_ID ASC, " \
                         "Fav_Stk_Live_Symbol ASC, Fav_Stk_Live_Upd_Tmsp DESC ;".format(db_name, db_schema, user_id)
            _sql1 = pd.read_sql_query(_selectqry, db_connection)
            return(_sql1)
        except:
            print('error Enter Valid Stock-Symbol-ID !!!')

    def insert_fav_stk_live_price(self, usrid, symb, price):
        user_id = int(usrid)
        _tick_sym = symb
        _tick_price = float(price)
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            _insertqry = "INSERT INTO {}.{}.FAV_STK_LIVE_PRICE_DETAILS " \
                         "VALUES ({},'{}', {}, '{}')".format(db_name, db_schema, user_id, _tick_sym, _tick_price,
                                                             _curr_date_time)
            db_cursor.execute(_insertqry)
        except:
            print('SQL Error while inserting rows from FAV_STK_LIVE_PRICE_DETAILS table !!!')

class HandleFavStkNewsTable:
    def __init__(self):
        global db_name, db_schema, user_id

    def select_fav_stk_news(self, usrid, symid):
        user_id = int(usrid)
        try:
            _selectqry = "SELECT TOP (2) Fav_Stk_News_Details FROM {}.{}.FAV_STK_NEWS_DETAILS " \
                         "WHERE Fav_Stk_News_User_ID = {} AND Fav_Stk_News_Symbol = '{}' "  \
                         "ORDER BY Fav_Stk_News_User_ID ASC, " \
                         "Fav_Stk_News_Symbol ASC, Fav_Stk_News_Upd_Tmsp DESC ;".\
                         format(db_name, db_schema, user_id, symid)
            _sql1 = pd.read_sql_query(_selectqry, db_connection)
            return(_sql1)
        except:
            print('error Enter Valid Stock-Symbol-ID !!!')

    def insert_fav_stk_news(self, tusrid, tsym, tdate, ttime, tdetails):
        user_id = int(tusrid)
        _tick_sym = tsym
        _tick_date = tdate
        _tick_time = ttime
        _tick_details = tdetails[:300]
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            _insertqry = "INSERT INTO {}.{}.FAV_STK_NEWS_DETAILS " \
                         "VALUES ({},'{}','{}','{}','{}','{}')".format(db_name,db_schema,user_id,_tick_sym,_tick_date,
                                                                       _tick_time, _tick_details, _curr_date_time)
            db_cursor.execute(_insertqry)
        except:
            print('SQL Error while inserting rows from FAV_STK_NEWS_DETAILS table !!!')

class HandleFavStkTrendTable:
    def __init__(self):
        global db_name, db_schema, user_id

    def insert_fav_stk_trend(self, tusrid, tsym, tprevprice, tprevnews, tcurrprice, tcurrnews, ttrendana):
        user_id = int(tusrid)
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            _insertqry = "INSERT INTO {}.{}.FAV_STK_TREND_DETAILS " \
                         "VALUES ({},'{}',{},'{}',{},'{}',{},'{}')".format(db_name,db_schema,user_id,tsym,tprevprice,
                                                                           tprevnews, tcurrprice,tcurrnews,
                                                                           ttrendana, _curr_date_time)
            db_cursor.execute(_insertqry)
        except:
            print('SQL Error while inserting rows from FAV_STK_TREND_DETAILS table !!!')

    def select_fav_stk_trend(self, usrid, symid):
        user_id = int(usrid)
        try:
            _selectqry = "SELECT TOP (1) Fav_Stk_Trend_Curr_Price FROM {}.{}.FAV_STK_TREND_DETAILS " \
                         "WHERE Fav_Stk_Trend_User_ID = {} AND Fav_Stk_Trend_Symbol = '{}' "  \
                         "ORDER BY Fav_Stk_Trend_Upd_Tmsp DESC;".\
                         format(db_name, db_schema, user_id, symid)
            _sql1 = pd.read_sql_query(_selectqry, db_connection)
            return(float(_sql1['Fav_Stk_Trend_Curr_Price'].values))
        except:
            print('error Enter Valid Stock-Symbol-ID !!!')

    def select_fav_stk_trend_analy(self, usrid, symid):
        user_id = int(usrid)
        try:
            _selectqry = "SELECT TOP (1) Fav_Stk_Trend_Analysis FROM {}.{}.FAV_STK_TREND_DETAILS " \
                         "WHERE Fav_Stk_Trend_User_ID = {} AND Fav_Stk_Trend_Symbol = '{}' "  \
                         "ORDER BY Fav_Stk_Trend_Upd_Tmsp DESC;".\
                         format(db_name, db_schema, user_id, symid)
            _sql1 = pd.read_sql_query(_selectqry, db_connection)
            return(int(_sql1['Fav_Stk_Trend_Analysis'].values))
        except:
            print('error Enter Valid Stock-Symbol-ID !!!')


def Handle_Stock_Monitor():
    _fav_usr_stk_sym_list = list(_fav_usr_stk_sym.select_fav_usr_stk_sym(user_id, 'getsymbol'))
    for sym_list in _fav_usr_stk_sym_list:
        _prev_stk_price = _fav_stk_trend.select_fav_stk_trend(user_id, sym_list)
        _curr_stk_price = _stk_live_price.liveprice(sym_list)
        _news_df = _fav_stk_news.get_live_stock_news(_fav_usr_stk_sym_list, 1)
        for index, rows in _news_df.iterrows():
            _rows_list = list(rows.values)
            _nsym = str(_rows_list[0])
            _ndate = str(datetime.strptime(_rows_list[1], "%b-%d-%y")).split(' ')[0]
            _ntime = str(_rows_list[2][:5] + millsec)
            _ndetails = str(_rows_list[3][:300].replace("'", ""))
            _fav_stk_curr_news.insert_fav_stk_news(user_id, _nsym, _ndate, _ntime, _ndetails)
            handle_db.commit_database()
        _fav_stk_live_price.insert_fav_stk_live_price(user_id, sym_list, _curr_stk_price)
        handle_db.commit_database()

        _trend_analy = 0
        print('Symbol: ', sym_list)
        print('Initial Trend Analysis: ', _trend_analy)
        print('Previous Price: ', _prev_stk_price)
        print('Current Price: ', _curr_stk_price)
        if _curr_stk_price > _prev_stk_price:
            _trend_analy += 1
        else:
            _trend_analy -= 1

        print('After updation: ', _trend_analy)
        _news_cnt = 1
        for sym_list in _fav_usr_stk_sym_list:
            _top2_news_df = _fav_stk_curr_news.select_fav_stk_news(user_id, sym_list)
            while True:
                for nhead, nnews in _top2_news_df.iterrows():
                    if _news_cnt == 1:
                        _curr_news = str(nnews[:300])
                        _news_cnt += 1
                    else:
                        _prev_news = str(nnews[:300])
                        _news_cnt = 1
                break
            _curr_price = _stk_live_price.liveprice(sym_list)
            _prev_price = _stk_live_price.closedata(sym_list)
            _prev_news = _prev_news[24:]
            _curr_news = _curr_news[24:]
            email_content = 'Symbol: {} Price is increased. Previous Value={} Current Value={}' \
                   ''.format(sym_list, _prev_price, _curr_price)
            _fav_stk_trend.insert_fav_stk_trend(user_id, sym_list, _prev_price, _prev_news,
                                                _curr_price, _curr_news, _trend_analy)
            handle_db.commit_database()


if __name__ == '__main__':

    db_connection = None
    db_cursor = None
    db_name = 'StockMonitor'
    db_schema = 'Stock'
    user_id = 1
    millsec = ':00.0000000'
    email_content = ''

    option_dict = {
        0: "Exit from the Application",
        1: "Refresh the Stock Symbols",
        2: "List User Favourite's Stocks",
        3: "Change User Favourite's Stocks",
        4: "Load the Latest Values",
        5: "Start Monitoring the Favourite's Stocks"
    }

    # Validations Class
    getconv = GetRequDetails()

    # Establish the Connections with Database
    handle_db = HandleDataBaseOperations()
    handle_db.establish_db_connection()

    _user_details = HandleUserDetailsTable()
    _load_symbol = LoadSymbolDataFrame()
    _stock_symbol = HandleStockSymbolTable()
    _fav_usr_stk_sym = HandleFavUsrStkSymTable()
    _fav_stk_live_price = HandleFavStkLivePriceTable()
    _fav_stk_news = GetRequDetails()
    _stk_live_price = StockLivePrice()
    _fav_stk_curr_news = HandleFavStkNewsTable()
    _fav_stk_trend = HandleFavStkTrendTable()
    _send_email_to = SendEmail()

    while True:
        print("Select an Option: ")
        print(json.dumps(option_dict, indent=4))
        option = input("Select Option: ")

        if option == '0':
            break

        elif option == '1':
            # These statements below loads the latest stock in to a STK_SYMBOL_DETAILS

            load_symbol_df = _load_symbol.load_sym_table()
            _stock_symbol.delete_stk_sym()

            str_print = 'STK_SYMBOL_DETAILS Refresh In-Progress ...'
            for k in range(50):
                print('\r' + str_print[:k], end='')
                time.sleep(.05)
            print('\r', end='')
            _stock_symbol.insert_stk_sym_df(load_symbol_df)
            handle_db.commit_database()
            str_print = 'STK_SYMBOL_DETAILS Loaded Successfully!'
            for k in range(50):
                print('\r' + str_print[:k], end='')
                time.sleep(.05)
            print('\n')

        elif option == '2':
            # These statements below list User Favourite's Stocks
            user_id = getconv.get_conv_val_id('user')

            _fav_usr_stK_sym_df = _fav_usr_stk_sym.select_fav_usr_stk_sym(user_id, 'display')
            print(tabulate(_fav_usr_stK_sym_df, headers='keys', tablefmt="psql"))

        elif option == '3':
            #These statements below updates User Favourite's Stocks
            user_id = getconv.get_conv_val_id('user')

            chg_fav = input("Do You want to Add your Favourite's (Y/N): ").upper()
            if chg_fav == 'Y':
                while True:
                    fav_stk_sym = input('Enter Favourite Stock Symbol: ').upper()

                    ret_cd, sym_id, sym_symbol, sym_name = _stock_symbol.select_stk_sym(fav_stk_sym)
                    ret_cd = int(ret_cd)
                    if (ret_cd > 0):
                        sym_id = int(sym_id)
                        sym_symbol = str(sym_symbol).split()[1]
                        sym_name = str(sym_name)[5:].split('Name:')[0]
                        _fav_usr_stk_sym.insert_fav_usr_stk_sym(sym_id, sym_symbol, sym_name, user_id)
                        handle_db.commit_database()
                        break
                    else:
                        print('Stock Not Present. Enter the valid stock symbol !!!')

            chg_fav = input("Do You want to Delete your Favourite's (Y/N): ").upper()
            if chg_fav == 'Y':
                fav_stk_sym = input('Enter Favourite Stock Symbol: ').upper()
                _fav_usr_stk_sym.delete_fav_usr_stk_sym(fav_stk_sym)
                handle_db.commit_database()

        elif option == '4':
            user_id = getconv.get_conv_val_id('user')

            _fav_usr_stk_sym_list = list(_fav_usr_stk_sym.select_fav_usr_stk_sym(user_id, 'getsymbol'))
            for sym_list in _fav_usr_stk_sym_list:
                _sym_price = _stk_live_price.liveprice(sym_list)
                _fav_stk_live_price.insert_fav_stk_live_price(user_id, sym_list, _sym_price)
                handle_db.commit_database()

            live_price_df = _fav_stk_live_price.select_fav_stk_live_price(user_id)
            # print(tabulate(live_price_df, headers='keys', tablefmt="psql"))

            _news_df = _fav_stk_news.get_live_stock_news(_fav_usr_stk_sym_list, 3)
            # print(_news_df)

            for index, rows in _news_df.iterrows():
                _rows_list = list(rows.values)
                _nsym = str(_rows_list[0])
                _ndate = str(datetime.strptime(_rows_list[1], "%b-%d-%y")).split(' ')[0]
                _ntime = str(_rows_list[2][:5] + millsec)
                _ndetails = str(_rows_list[3][:300].replace("'", ""))
                _fav_stk_curr_news.insert_fav_stk_news(user_id,_nsym,_ndate,_ntime,_ndetails)
                handle_db.commit_database()

            _news_cnt = 1
            for sym_list in _fav_usr_stk_sym_list:
                _top2_news_df = _fav_stk_curr_news.select_fav_stk_news(user_id, sym_list)
                while True:
                    for nhead, nnews in _top2_news_df.iterrows():
                        if _news_cnt == 1:
                            _curr_news = str(nnews[:300])
                            _news_cnt += 1
                        else:
                            _prev_news =str(nnews[:300])
                            _news_cnt = 1
                    break
                _curr_price = _stk_live_price.liveprice(sym_list)
                _prev_price = _stk_live_price.closedata(sym_list)
                _prev_news = _prev_news[24:]
                _curr_news = _curr_news[24:]
                _trend_ana = 0
                _fav_stk_trend.insert_fav_stk_trend(user_id, sym_list, _prev_price, _prev_news,
                                                    _curr_price, _curr_news, _trend_ana)
                handle_db.commit_database()

        elif option == '5':
            user_id = getconv.get_conv_val_id('user')
            _usr_ret_cd, _usr_id, _usr_fname, _usr_email, _usr_rights = _user_details.select_user_details(user_id)
            print('return code: ', _usr_ret_cd)
            print('name: ', _usr_fname)

            if _usr_ret_cd == 0:
                pass
            else:
                while True:
                    print('going to sleep for 10 secs')
                    dtime_now = datetime.now()
                    current_time = dtime_now.strftime("%H:%M:%S")
                    time.sleep(30)
                    print('slept 10 seconds')
                    Handle_Stock_Monitor()
                    print('after handle stk moni ... sleeping for 10 seconds')
                    time.sleep(30)
                    print('slept 10 seconds')

                    _fav_usr_stk_sym_list = list(_fav_usr_stk_sym.select_fav_usr_stk_sym(user_id, 'getsymbol'))
                    for sym_list in _fav_usr_stk_sym_list:
                        _trend_analyze = _fav_stk_trend.select_fav_stk_trend_analy(user_id, sym_list)
                        print('inside email part')
                        print('Symbol name: ', sym_list)
                        print('Trend analysis: ', _trend_analyze)
                        if _trend_analyze >= 1:
                            _sub = 'Reg: Your Latest Stock Information'
                            # _curr_stkk_price = _stk_live_price.liveprice(sym_list)
                            # _txt = 'Symbol: {} Price is increased. Current Value={}'.format(sym_list, _curr_stkk_price)
                            _send_email_to.sendemail(_sub, _usr_email, email_content)

                    if current_time >= '14:05:59':
                        break

        else:
            print('An Invalid Option. Try Valid Option !!!')
