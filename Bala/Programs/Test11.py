import pandas as pd
import time
from datetime import datetime
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

    # sentence = r"i've been running from what i don't know if she's there or if she's cares it's taken you a long time to see you've got a goldfish memory this song's ed'"
    # print(sentence)
    # print(sentence.replace("'", ""))
    #
    # sentence = r"i've been running from what i don't know if she's there or if she's cares it's taken you a long time to see you've got a goldfish memory this song's ed'"
    # re.sub("'", "", sentence)
    # print(sentence)



    date_received = 'Feb-02-21'
    date_convert = str(datetime.strptime(date_received, "%b-%d-%y"))
    print(date_convert.split(' ')[0])

    date_string = "21 June, 2018"

    print("date_string =", date_string)
    print("type of date_string =", type(date_string))

    date_object = datetime.strptime(date_string, "%d %B, %Y")

    print("date_object =", date_object)
    print("type of date_object =", type(date_object))

    dt_string = "12/11/2018 09:15:32"

    # Considering date is in dd/mm/yyyy format
    dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
    print("dt_object1 =", dt_object1)

    # Considering date is in mm/dd/yyyy format
    dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
    print("dt_object2 =", dt_object2)