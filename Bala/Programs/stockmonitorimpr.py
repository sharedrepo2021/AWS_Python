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
from emailgmail import Handle_Send_Email


class HandleGivenInput:
    def __init__(self):
        pass

    @staticmethod
    def validate_convert_given_id(arg_identifier):
        while True:
            if arg_identifier == 'user':
                _val_id = input('Enter User ID: ')
            elif arg_identifier == 'symbol':
                _val_id = input('Enter Stock Symbol ID: ')
            else:
                _val_id = 1
                print('!!! Please enter valid identifier !!!')

            if _val_id.isnumeric():
                return int(_val_id)
            else:
                print('!!! Please enter valid entry !!!')


class HandleStkSymbolDataFrame:
    def __init__(self):
        pass

    @staticmethod
    def load_symbols_dataframe():
        try:
            _nasdaq_csv = r'https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/' \
                          r'7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv'
            _nyse_csv = r'https://pkgstore.datahub.io/core/nyse-other-listings/other-listed_csv/data/' \
                        r'9f38660d84fe6ba786a4444b815b3b80/other-listed_csv.csv'

            _nasdaq_data = pd.read_csv(_nasdaq_csv, usecols=['Symbol', 'Company Name'])
            _nyse_data = pd.read_csv(_nyse_csv, usecols=['ACT Symbol', 'Company Name'])
            _nasdaq_data.columns = ['Ticker_Symbol', 'Stock_Name']
            _nyse_data.columns = ['Ticker_Symbol', 'Stock_Name']

            _nasdaq_nyse_data = pd.concat([_nasdaq_data, _nyse_data], ignore_index=True)
            return _nasdaq_nyse_data
        except Exception as _error:
            print('!!! Error: {} while loading the symbols table !!!'.format(_error))


class HandleStockLatestNews:
    def __init__(self):
        pass

    @staticmethod
    def get_stock_news(arg_symbols_id, arg_max_news):
        try:
            _finviz_url = 'https://finviz.com/quote.ashx?t='
            _parsed_news = []
            _max_news = int(arg_max_news)

            for _symbol_id in arg_symbols_id:
                _news_tables = {}
                _symbol_id_upper = _symbol_id.upper()

                _url = _finviz_url + _symbol_id_upper
                _req = Request(url=_url, headers={'user-agent': 'my-app/0.0.1'})
                _resp = urlopen(_req)
                _html = BeautifulSoup(_resp, features="lxml")
                _news_table = _html.find(id='news-table')
                _news_tables[_symbol_id_upper] = _news_table

                # Iterate through the news till max_news
                _increment_var = 1
                _news_date = ''
                _news_time = ''
                for file_name, news_table in _news_tables.items():
                    for x in news_table.findAll('tr'):
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
            return _news_latest
        except Exception as _error:
            print('!!! Error: {} while retrieving the latest news !!!'.format(_error))


class HandleStockLivePrice:
    def __init__(self):
        pass

    @staticmethod
    def get_live_price(arg_symbol_id):
        try:
            return float(si.get_live_price(arg_symbol_id))
        except Exception as _error:
            print('!!! Error: {} while retrieving the latest price !!!'.format(_error))

    @staticmethod
    def get_open_price(arg_symbol_id):
        try:
            _today = dt.date.today()
            _open_df = pd.DataFrame(si.get_data(arg_symbol_id, start_date=_today))
            return float(_open_df['open'])
        except Exception as _error:
            print('!!! Error: {} while retrieving the open price !!!'.format(_error))


class HandleDataBaseConnection:
    def __init__(self):
        pass

    @staticmethod
    def db_establish_connection():
        global db_connection, db_cursor
        try:
            db_connection = pyodbc.connect('Driver={SQL Server};' 
                                           'Server=BALALENR7\SQLEXPRESS;' 
                                           'Database=StockMonitor;' 
                                           'Trusted_Connection=yes;')
            db_cursor = db_connection.cursor()
        except Exception as _error:
            print('!!! Error: {} database connection !!!'.format(_error))

    @staticmethod
    def db_commit_opertion():
        try:
            db_cursor.execute('COMMIT')
        except Exception as _error:
            print('!!! Error: {} while committing !!!'.format(_error))


class HandleStkSymbolDetailsTable:
    def __init__(self):
        global db_connection, db_cursor, db_name, db_schema

    @staticmethod
    def delete_stk_sym_det_tab():
        try:
            _delete_qry = 'DELETE FROM {}.{}.STK_SYMBOL_DETAILS ;'.format(db_name, db_schema)
            db_cursor.execute(_delete_qry)
        except Exception as _error:
            print('!!! Error: {} while deleting rows from STK_SYMBOL_DETAILS table !!!'.format(_error))

    @staticmethod
    def select_stk_sym_det_tab(arg_symbol_id):
        try:
            _select_qry = "SELECT * FROM {}.{}.STK_SYMBOL_DETAILS " \
                         "WHERE Stk_Sym_Symbol='{}';".format(db_name, db_schema, arg_symbol_id)
            _result_set = pd.read_sql_query(_select_qry, db_connection)
            return(_result_set.shape[0], _result_set['Stk_Sym_ID'], _result_set['Stk_Sym_Symbol'],
                   _result_set['Stk_Sym_Name'])
        except Exception as _error:
            print('!!! Error: {} while selecting rows from STK_SYMBOL_DETAILS table !!!'.format(_error))

    @staticmethod
    def insert_stk_sym_det_tab(arg_nasdaq_nyse):
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            for index, row in arg_nasdaq_nyse.iterrows():
                _row_str = row.Stock_Name.replace("'", "")
                _insert_qry = "INSERT INTO {}.{}.STK_SYMBOL_DETAILS " \
                              "VALUES ({}, '{}', '{}', '{}')".format(db_name, db_schema, index, row.Ticker_Symbol,
                                                                     _row_str, _curr_date_time)
                db_cursor.execute(_insert_qry)
        except Exception as _error:
            print('!!! Error: {} while inserting rows into STK_SYMBOL_DETAILS table !!!'.format(_error))


class HandleStkUserDetailsTable:
    def __init__(self):
        global db_connection, db_name, db_schema, user_id

    @staticmethod
    def select_user_det_tab(arg_user_id):
        user_id = int(arg_user_id)
        try:
            _select_qry = "SELECT Stk_User_ID, Stk_User_First_Name, " \
                         "Stk_User_Email_ID, Stk_User_Rights FROM {}.{}.STK_USER_DETAILS " \
                         "WHERE Stk_User_ID = {} ;".format(db_name, db_schema, user_id)
            _result_set = pd.read_sql_query(_select_qry, db_connection)
            return(_result_set.shape[0], _result_set['Stk_User_ID'].values, _result_set['Stk_User_First_Name'].values,
                   _result_set['Stk_User_Email_ID'].values, _result_set['Stk_User_Rights'].values)
        except Exception as _error:
            print('!!! Error: {} while selecting rows from STK_USER_DETAILS table !!!'.format(_error))


class HandleFavUsrStkSymTable:
    def __init__(self):
        global db_connection, db_cursor, db_name, db_schema, user_id

    @staticmethod
    def select_fav_usr_stk_sym_tab(arg_user_id, retrieve_mode):
        user_id = int(arg_user_id)
        try:
            _select_qry = 'SELECT Fav_Usr_Stk_Sym_ID, Fav_Usr_Stk_Symbol, ' \
                         'Fav_Usr_Stk_Name FROM {}.{}.FAV_USER_STK_SYMBOL_DETAILS ' \
                         'WHERE Fav_Usr_Stk_User_ID={} ;'.format(db_name, db_schema, user_id)
            _result_set = pd.read_sql_query(_select_qry, db_connection)
        except Exception as _error:
            print('!!! Error: {} while selecting rows from FAV_USER_STK_SYMBOL_DETAILS table !!!'.format(_error))

        if _result_set.shape[0] > 0 and retrieve_mode == 'display':
            return _result_set
        elif _result_set.shape[0] > 0 and retrieve_mode == 'getsymbol':
            return _result_set['Fav_Usr_Stk_Symbol']
        else:
            print('!!! No Rows Selected from FAV_USER_STK_SYMBOL_DETAILS table !!!')

    @staticmethod
    def insert_fav_usr_stk_sym_tab(arg_symbol_id, arg_stk_symbol, arg_stk_name, arg_user_id):
        user_id = int(arg_user_id)
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            _insert_qry = "INSERT INTO {}.{}.FAV_USER_STK_SYMBOL_DETAILS " \
                         "VALUES ({},'{}','{}',{},'{}')".format(db_name, db_schema, arg_symbol_id, arg_stk_symbol,
                                                                arg_stk_name, user_id, _curr_date_time)
            db_cursor.execute(_insert_qry)
        except Exception as _error:
            print('!!! Error: {} while inserting rows into FAV_USER_STK_SYMBOL_DETAILS table !!!'.format(_error))

    @staticmethod
    def delete_fav_usr_stk_sym_tab(arg_symbol_id):
        try:
            _delete_qry = "DELETE FROM {}.{}.FAV_USER_STK_SYMBOL_DETAILS " \
                         "WHERE Fav_Usr_Stk_Symbol = '{}'; ".format(db_name, db_schema, arg_symbol_id)
            db_cursor.execute(_delete_qry)
        except Exception as _error:
            print('!!! Error: {} while deleting rows into FAV_USER_STK_SYMBOL_DETAILS table !!!'.format(_error))


class HandleFavStkLivePriceDetailsTable:
    def __init__(self):
        global db_connection, db_cursor, db_name, db_schema, user_id

    @staticmethod
    def select_fav_stk_live_price_tab(arg_user_id):
        user_id = int(arg_user_id)
        try:
            _select_qry = "SELECT * FROM {}.{}.FAV_STK_LIVE_PRICE_DETAILS " \
                         "WHERE Fav_Stk_Live_User_ID = '{}' ORDER BY Fav_Stk_Live_User_ID ASC, " \
                         "Fav_Stk_Live_Symbol ASC, Fav_Stk_Live_Upd_Tmsp DESC ;".format(db_name, db_schema, user_id)
            _result_set = pd.read_sql_query(_select_qry, db_connection)
            return _result_set
        except Exception as _error:
            print('!!! Error: {} while selecting rows from FAV_STK_LIVE_PRICE_DETAILS table !!!'.format(_error))

    @staticmethod
    def insert_fav_stk_live_price_tab(arg_user_id, arg_symbol_id, arg_symbol_price):
        user_id = int(arg_user_id)
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            _insert_qry = "INSERT INTO {}.{}.FAV_STK_LIVE_PRICE_DETAILS " \
                         "VALUES ({},'{}', {}, '{}')".format(db_name, db_schema, user_id, arg_symbol_id,
                                                             arg_symbol_price, _curr_date_time)
            db_cursor.execute(_insert_qry)
        except Exception as _error:
            print('!!! Error: {} while inserting rows into FAV_STK_LIVE_PRICE_DETAILS table !!!'.format(_error))


class HandleFavStkNewsDetailsTable:
    def __init__(self):
        global db_connection, db_cursor, db_name, db_schema, user_id

    @staticmethod
    def select_top2_fav_stk_news_tab(arg_user_id, arg_symbol_id):
        user_id = int(arg_user_id)
        try:
            _select_qry = "SELECT TOP (2) Fav_Stk_News_Details FROM {}.{}.FAV_STK_NEWS_DETAILS " \
                         "WHERE Fav_Stk_News_User_ID = {} AND Fav_Stk_News_Symbol = '{}' "  \
                         "ORDER BY Fav_Stk_News_User_ID ASC, " \
                         "Fav_Stk_News_Symbol ASC, Fav_Stk_News_Upd_Tmsp DESC ;".\
                         format(db_name, db_schema, user_id, arg_symbol_id)
            _result_set = pd.read_sql_query(_select_qry, db_connection)
            return _result_set
        except Exception as _error:
            print('!!! Error: {} while selecting rows from FAV_STK_NEWS_DETAILS table !!!'.format(_error))

    @staticmethod
    def insert_fav_stk_news_tab(arg_user_id, arg_symbol_id, arg_symbol_date, arg_symbol_time, arg_symbol_news):
        user_id = int(arg_user_id)
        _symbol_news = arg_symbol_news[:300]
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            _insert_qry = "INSERT INTO {}.{}.FAV_STK_NEWS_DETAILS " \
                         "VALUES ({},'{}','{}','{}','{}','{}')".format(db_name, db_schema, user_id, arg_symbol_id,
                                                                       arg_symbol_date, arg_symbol_time,
                                                                       _symbol_news, _curr_date_time)
            db_cursor.execute(_insert_qry)
        except Exception as _error:
            print('!!! Error: {} while inserting rows into FAV_STK_NEWS_DETAILS table !!!'.format(_error))


class HandleFavStkTrendDetailsTable:
    def __init__(self):
        global db_connection, db_cursor, db_name, db_schema, user_id

    @staticmethod
    def insert_fav_stk_trend_tab(arg_user_id, arg_symbol_id, arg_prev_price, arg_prev_news, arg_curr_price,
                                 arg_curr_news, arg_trend_analysis):
        user_id = int(arg_user_id)
        _curr_date_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            _insert_qry = "INSERT INTO {}.{}.FAV_STK_TREND_DETAILS " \
                         "VALUES ({},'{}',{},'{}',{},'{}',{},'{}')".format(db_name, db_schema, user_id,
                                                                           arg_symbol_id, arg_prev_price, arg_prev_news,
                                                                           arg_curr_price, arg_curr_news,
                                                                           arg_trend_analysis, _curr_date_time)
            db_cursor.execute(_insert_qry)
        except Exception as _error:
            print('!!! Error: {} while inserting rows into FAV_STK_TREND_DETAILS table !!!'.format(_error))

    @staticmethod
    def select_tana_fav_stk_trend_tab(arg_user_id, arg_symbol_id):
        user_id = int(arg_user_id)
        try:
            _select_qry = "SELECT TOP (1) Fav_Stk_Trend_Analysis FROM {}.{}.FAV_STK_TREND_DETAILS " \
                         "WHERE Fav_Stk_Trend_User_ID = {} AND Fav_Stk_Trend_Symbol = '{}' "  \
                         "ORDER BY Fav_Stk_Trend_Upd_Tmsp DESC;".\
                         format(db_name, db_schema, user_id, arg_symbol_id)
            _result_set = pd.read_sql_query(_select_qry, db_connection)
            return int(_result_set['Fav_Stk_Trend_Analysis'].values)
        except Exception as _error:
            print('!!! Error: {} while selecting rows from FAV_STK_TREND_DETAILS table !!!'.format(_error))

    @staticmethod
    def select_cprice_fav_stk_trend_tab(arg_user_id, arg_symbol_id):
        user_id = int(arg_user_id)
        try:
            _select_qry = "SELECT TOP (1) Fav_Stk_Trend_Curr_Price FROM {}.{}.FAV_STK_TREND_DETAILS " \
                         "WHERE Fav_Stk_Trend_User_ID = {} AND Fav_Stk_Trend_Symbol = '{}' "  \
                         "ORDER BY Fav_Stk_Trend_Upd_Tmsp DESC;".\
                         format(db_name, db_schema, user_id, arg_symbol_id)
            _result_set = pd.read_sql_query(_select_qry, db_connection)
            return float(_result_set['Fav_Stk_Trend_Curr_Price'].values)
        except Exception as _error:
            print('!!! Error: {} while selecting rows from FAV_STK_TREND_DETAILS table !!!'.format(_error))


class HandleStockMonitor:
    def __init__(self):
        global db_connection, db_cursor, db_name, db_schema, user_id

    @staticmethod
    def start_stock_monitor():
        global email_content
        _fav_usr_stk_sym_list = list(_db_fav_usr_stk_sym.select_fav_usr_stk_sym_tab(user_id, 'getsymbol'))
        for sym_list in _fav_usr_stk_sym_list:
            _prev_stk_price = _db_fav_stk_trend.select_cprice_fav_stk_trend_tab(user_id, sym_list)
            _curr_stk_price = round(_load_stk_live_price.get_live_price(sym_list), 2)
            _news_df = _load_stk_late_news.get_stock_news(_fav_usr_stk_sym_list, 1)

            for index, rows in _news_df.iterrows():
                _rows_list = list(rows.values)
                _nsym = str(_rows_list[0])
                _ndate = str(datetime.strptime(_rows_list[1], "%b-%d-%y")).split(' ')[0]
                _ntime = str(_rows_list[2][:5] + milli_secs)
                _ndetails = str(_rows_list[3][:300].replace("'", ""))
                _db_fav_stk_news.insert_fav_stk_news_tab(user_id, _nsym, _ndate, _ntime, _ndetails)
                _db_handle_conn.db_commit_opertion()

            _db_stk_live_price.insert_fav_stk_live_price_tab(user_id, sym_list, _curr_stk_price)
            _db_handle_conn.db_commit_opertion()

            _trend_analysis = 0
            if _curr_stk_price > _prev_stk_price:
                _trend_analysis += 1
            else:
                _trend_analysis -= 1

            _news_cnt = 1
            for sym_list in _fav_usr_stk_sym_list:
                _top2_news_df = _db_fav_stk_news.select_top2_fav_stk_news_tab(user_id, sym_list)
                while True:
                    for nhead, nnews in _top2_news_df.iterrows():
                        if _news_cnt == 1:
                            _curr_news = str(nnews[:300])
                            _news_cnt += 1
                        else:
                            _prev_news = str(nnews[:300])
                            _news_cnt = 1
                    break
                _trd_curr_price = round(_load_stk_live_price.get_live_price(sym_list), 2)
                _trd_prev_price = _db_fav_stk_trend.select_cprice_fav_stk_trend_tab(user_id, sym_list)
                _prev_news = _prev_news[24:]
                _curr_news = _curr_news[24:]
                email_content = 'Symbol: {} Price is increased. Previous Value={} ' \
                                'Current Value={}'.format(sym_list, _trd_prev_price, _trd_curr_price)
                _db_fav_stk_trend.insert_fav_stk_trend_tab(user_id, sym_list, _trd_prev_price, _prev_news,
                                                           _trd_curr_price, _curr_news, _trend_analysis)
                _db_handle_conn.db_commit_opertion()


if __name__ == '__main__':

    # Definition of Global Variables
    db_name = 'StockMonitor'
    db_schema = 'Stock'
    db_connection = None
    db_cursor = None

    user_id = 1
    milli_secs = ':00.0000000'
    email_content = ' '

    # Definition of Dictionary
    main_dict = {
        0: "Exit            from the application",
        1: "Enter           user details",
        2: "Preset          the stocks for today",
        3: "Start           monitoring the favourite's stocks"
    }

    user_sub_dict = {
        '0': "Exit            from the application",
        'a': "Refresh         the stock symbols (Optional)",
        'b': "Display         your favourite stocks",
        'c': "Add Stock       to your favourite",
        'd': "Remove Stock    to your favourite"
    }

    # Definition of Class
    _validate_given_id = HandleGivenInput()
    _start_stk_monitor = HandleStockMonitor()
    _send_email_to = Handle_Send_Email()

    _load_stk_late_news = HandleStockLatestNews()
    _load_stk_live_price = HandleStockLivePrice()
    _load_stk_symbols = HandleStkSymbolDataFrame()

    _db_handle_conn = HandleDataBaseConnection()
    _db_stock_symbol = HandleStkSymbolDetailsTable()
    _db_user_details = HandleStkUserDetailsTable()
    _db_fav_usr_stk_sym = HandleFavUsrStkSymTable()
    _db_stk_live_price = HandleFavStkLivePriceDetailsTable()
    _db_fav_stk_news = HandleFavStkNewsDetailsTable()
    _db_fav_stk_trend = HandleFavStkTrendDetailsTable()

    _db_handle_conn.db_establish_connection()

    # Main Logic
    while True:
        print('\n')
        print("********************************************************")
        print("**************SELECT AN OPTION: ************************")
        print("********************************************************")
        print('\n')
        print(json.dumps(main_dict, indent=4))
        user_option = input("Select an option: ")

        if user_option == "0":
            break

        elif user_option == "1":
            while True:
                user_id = _validate_given_id.validate_convert_given_id('user')
                _db_usr_ret_cd, _db_usr_id, _db_usr_fname, _db_usr_email, _db_usr_rights = \
                    _db_user_details.select_user_det_tab(user_id)
                if _db_usr_ret_cd == 0:
                    print("No rows found in the STK_USER_DETAILS table for the user id: {} ".format(user_id))
                else:
                    print("\n" * 20, end='')
                    print('\n Hello {}. Enter your choice \n'.format(''.join(_db_usr_fname)))
                    print(json.dumps(user_sub_dict, indent=4))
                    user_sub_option = input("Select an option: ")

                    if user_sub_option == "0":
                        break

                    elif user_sub_option == "a":
                        print("\n" * 20)
                        load_symbol_df = _load_stk_symbols.load_symbols_dataframe()
                        _db_stock_symbol.delete_stk_sym_det_tab()

                        str_print = 'STK_SYMBOL_DETAILS Refresh In-Progress ...'
                        for k in range(50):
                            print('\r' + str_print[:k], end='')
                            time.sleep(.05)
                        print('\r', end='')
                        _db_stock_symbol.insert_stk_sym_det_tab(load_symbol_df)
                        _db_handle_conn.db_commit_opertion()
                        str_print = 'STK_SYMBOL_DETAILS Loaded Successfully!'
                        for k in range(50):
                            print('\r' + str_print[:k], end='')
                            time.sleep(.05)
                        print('\n')

                    elif user_sub_option == "b":
                        print("\n" * 20)
                        _fav_usr_stK_sym_df = _db_fav_usr_stk_sym.select_fav_usr_stk_sym_tab(user_id, 'display')
                        print(tabulate(_fav_usr_stK_sym_df, headers='keys', tablefmt="psql"))

                    elif user_sub_option == "c":
                        print("\n" * 20)
                        while True:
                            fav_stk_sym = input('Enter Favourite Stock Symbol: ').upper()
                            ret_cd, sym_id, sym_symbol, sym_name = _db_stock_symbol.select_stk_sym_det_tab(fav_stk_sym)
                            ret_cd = int(ret_cd)
                            if ret_cd > 0:
                                sym_id = int(sym_id)
                                sym_symbol = str(sym_symbol).split()[1]
                                sym_name = str(sym_name)[5:].split('Name:')[0]
                                _db_fav_usr_stk_sym.insert_fav_usr_stk_sym_tab(sym_id, sym_symbol, sym_name, user_id)
                                _db_handle_conn.db_commit_opertion()
                                break
                            else:
                                print('Stock Not Present. Enter the valid stock symbol !!!')

                    elif user_sub_option == "d":
                        print("\n" * 20)
                        fav_stk_sym = input('Enter Favourite Stock Symbol: ').upper()
                        _db_fav_usr_stk_sym.delete_fav_usr_stk_sym_tab(fav_stk_sym)
                        _db_handle_conn.db_commit_opertion()

                    break

        elif user_option == "2":
            print("\n" * 20)
            str_print = 'Your stock details are getting loaded ...'
            for k in range(60):
                print('\r' + str_print[:k], end='')
                time.sleep(.05)
            print('\r', end='')

            _fav_usr_stk_sym_list = list(_db_fav_usr_stk_sym.select_fav_usr_stk_sym_tab(user_id, 'getsymbol'))
            for sym_list in _fav_usr_stk_sym_list:
                _sym_price = round(_load_stk_live_price.get_live_price(sym_list), 2)
                _db_stk_live_price.insert_fav_stk_live_price_tab(user_id, sym_list, _sym_price)
                _db_handle_conn.db_commit_opertion()

            live_price_df = _db_stk_live_price.select_fav_stk_live_price_tab(user_id)
            _news_df = _load_stk_late_news.get_stock_news(_fav_usr_stk_sym_list, 3)

            for index, rows in _news_df.iterrows():
                _rows_list = list(rows.values)
                _nsym = str(_rows_list[0])
                _ndate = str(datetime.strptime(_rows_list[1], "%b-%d-%y")).split(' ')[0]
                _ntime = str(_rows_list[2][:5] + milli_secs)
                _ndetails = str(_rows_list[3][:300].replace("'", ""))
                _db_fav_stk_news.insert_fav_stk_news_tab(user_id, _nsym, _ndate, _ntime, _ndetails)
                _db_handle_conn.db_commit_opertion()

            _news_cnt = 1
            for sym_list in _fav_usr_stk_sym_list:
                _top2_news_df = _db_fav_stk_news.select_top2_fav_stk_news_tab(user_id, sym_list)
                while True:
                    for nhead, nnews in _top2_news_df.iterrows():
                        if _news_cnt == 1:
                            _curr_news = str(nnews[:300])
                            _news_cnt += 1
                        else:
                            _prev_news = str(nnews[:300])
                            _news_cnt = 1
                    break
                _curr_price = round(_load_stk_live_price.get_live_price(sym_list), 2)
                _prev_price = _db_fav_stk_trend.select_cprice_fav_stk_trend_tab(user_id, sym_list)
                _prev_news = _prev_news[24:]
                _curr_news = _curr_news[24:]
                _trend_ana = 0
                _db_fav_stk_trend.insert_fav_stk_trend_tab(user_id, sym_list, _prev_price, _prev_news,
                                                           _curr_price, _curr_news, _trend_ana)
                _db_handle_conn.db_commit_opertion()

            str_print = 'Your stock are loaded successfully'
            for k in range(60):
                print('\r' + str_print[:k], end='')
                time.sleep(.05)
            print('\n')

        elif user_option == "3":
            _db_usr_ret_cd, _db_usr_id, _db_usr_fname, _db_usr_email, _db_usr_rights = \
                _db_user_details.select_user_det_tab(user_id)

            if _db_usr_ret_cd == 0:
                print("No rows found in the STK_USER_DETAILS table for the user id: {} ".format(user_id))
            else:
                while True:
                    str_print = 'Stock monitoring started ...'
                    for k in range(60):
                        print('\r' + str_print[:k], end='')
                        time.sleep(.05)
                    print('\n')

                    dtime_now = datetime.now()
                    current_time = dtime_now.strftime("%H:%M:%S")
                    time.sleep(30)
                    _start_stk_monitor.start_stock_monitor()
                    time.sleep(30)

                    str_print = 'Stock monitoring in-progress ...'
                    for k in range(60):
                        print('\r' + str_print[:k], end='')
                        time.sleep(.05)
                    print('\n')

                    _fav_usr_stk_sym_list = list(_db_fav_usr_stk_sym.select_fav_usr_stk_sym_tab(user_id, 'getsymbol'))
                    for sym_list in _fav_usr_stk_sym_list:
                        _trend_analyze = _db_fav_stk_trend.select_tana_fav_stk_trend_tab(user_id, sym_list)
                        if _trend_analyze >= 1:
                            _subject = 'Reg: Your Latest Stock Information'
                            _send_email_to.send_email(_subject, _db_usr_email, email_content)

                    if current_time >= '11:05:59':
                        str_print = 'Stock monitoring completed.'
                        for k in range(60):
                            print('\r' + str_print[:k], end='')
                            time.sleep(.05)
                        print('\n')
                        break