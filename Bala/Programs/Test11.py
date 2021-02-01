import pandas as pd
import time
import datetime
from tabulate import tabulate
import re

if __name__ == '__main__':

    # nasdaq_csv = r'https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv'
    # nyse_csv = r'https://pkgstore.datahub.io/core/nyse-other-listings/other-listed_csv/data/9f38660d84fe6ba786a4444b815b3b80/other-listed_csv.csv'
    #
    # nasdaq_data = pd.read_csv(nasdaq_csv, usecols=['Symbol', 'Company Name'])
    # nyse_data = pd.read_csv(nyse_csv, usecols=['ACT Symbol', 'Company Name'])
    # nasdaq_data.columns = ['Ticker_Symbol', 'Stock_Name']
    # nyse_data.columns = ['Ticker_Symbol', 'Stock_Name']
    #
    #
    # nasdaq_nyse_data = pd.concat([nasdaq_data, nyse_data], ignore_index=True)
    # nasdaq_nyse_data.drop_duplicates(inplace=True)
    # print(tabulate(nasdaq_nyse_data.head(10), headers='keys', tablefmt='fancy_grid'))
    #
    # for index, rows in nasdaq_nyse_data.iterrows():
    #     print(index)
    #     print(rows.Ticker_Symbol)
    #     print(rows.Stock_Name)
    #
    # current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # print(current_date)
    #
    # curr_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    # print(curr_date_time)

    sentence = r"i've been running from what i don't know if she's there or if she's cares it's taken you a long time to see you've got a goldfish memory this song's ed'"
    print(sentence)
    print(sentence.replace("'", ""))

    sentence = r"i've been running from what i don't know if she's there or if she's cares it's taken you a long time to see you've got a goldfish memory this song's ed'"
    re.sub("'", "", sentence)
    print(sentence)