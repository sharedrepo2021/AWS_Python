from yahoo_fin import stock_info as si

# get live price of Apple
applevalue = si.get_live_price("aapl")
print(applevalue)
# or Amazon
si.get_live_price("amzn")
amazon = print(si.get_live_price("amzn"))

# or any other ticker
#si.get_live_price("ticker")
print(si.get_quote_table("aapl", dict_result = False))