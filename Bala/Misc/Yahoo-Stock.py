from yahoo_fin import stock_info as si
from yahoo_fin import options as op

# print('analysts info: ', si.get_analysts_info('nflx'))
# print('live price: ', si.get_live_price('nflx'))
# print('get data 01', si.get_data('nflx'))
# print('get data 02', si.get_data('nflx', start_date='2021-01-27'))
# print('get data 03', si.get_data('nflx', start_date='2021-01-26', end_date='2021-01-27'))
# print('get data 04', si.get_data('nflx', interval='1mo'))
#
# print(si.tickers_dow())
# print(si.tickers_nasdaq())
# print(si.tickers_other())
# print(si.tickers_sp500())

print(op.get_calls('nflx'))
print(op.get_expiration_dates('nflx'))