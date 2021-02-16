from yahoo_fin import stock_info as si
from yahoo_fin import options as op
import datetime
import pandas as pd
import calendar

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
days_2 = today - datetime.timedelta(days = 3)

int_today = datetime.datetime.today().weekday()



print('Yesterday    : ', yesterday)
print('Today        : ', today)
print('Tomorrow     : ', tomorrow)
print('days_2       : ', days_2)
print('int_today    : ', int_today)

# print('analysts info: ', si.get_analysts_info('nflx'))
print('live price: ', si.get_live_price('nflx'))
#print('Today Data', si.get_data('aapl'))
# print('get data 02', si.get_data('nflx', start_date=today))
# print('get data 02', si.get_data('nflx', start_date=yesterday))

df1 = pd.DataFrame(si.get_data('nflx'))
print(df1['open'])


dict1 = si.get_quote_table("nflx")
print(dict1['Open'])


# if int_today == 0:
#     df = pd.DataFrame(si.get_data('nflx', start_date=days_2))
# else:
#     df = pd.DataFrame(si.get_data('nflx', start_date='2021-02-16'))
#
# print(df)
# print(df['open'][0])
# print(df['close'])
# for i, j in df['close'].items():
#     if str(i)[:10] == str(yesterday):
#         print(i)
#         print(j)

# df = pd.DataFrame(si.get_data('nflx', start_date=today))
# print(df)
# tlist = float(df['open'])
# print(tlist)
# for i, j in df['open'].items():
#     if str(i)[:10] == str(today):
#         print(i)
#         print(j)

# for label, content in df.items():
#     print(label)
#     print(content)
# print(df['close'])
# print('get data 03', si.get_data('nflx', start_date='2021-01-26', end_date='2021-01-27'))
# print('get data 04', si.get_data('nflx', interval='1mo'))
#
# print(si.tickers_dow())
# print(si.tickers_nasdaq())
# print(si.tickers_other())
# print(si.tickers_sp500())

# print(op.get_calls('nflx'))
# print(op.get_expiration_dates('nflx'))

