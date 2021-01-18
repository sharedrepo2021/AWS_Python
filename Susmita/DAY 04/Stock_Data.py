import json
import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
print(json.dumps(msft.info, indent=4))

print(msft.calendar)

print(msft.history(period="max"))