import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
import datetime

stock =input("Enter the name of the stock:: ")

start = datetime.datetime(2013, 1, 1)
end = datetime.datetime(2021, 1, 2)
df = web.DataReader(stock, 'yahoo', start, end)

dates = []
for x in range(len(df)):
    newdate = str(df.index[x])
    newdate = newdate[0:5]
    dates.append(newdate)

df['dates'] = dates

print(df.head())
print(df.tail())