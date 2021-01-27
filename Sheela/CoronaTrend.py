import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import json as js

class CovidTrend:

    def __init__(self):
        self.URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
        self.df = pd.read_csv(self.URL_DATASET)

    def show_covid_result_date(self, date):
        df_tempdate = self.df[self.df['Date'] == date]

        if df_tempdate.empty:
            print("Date not found  . Available dates are:")
            print(self.df['Date'].unique())
        else:
            print(tabulate(df_tempdate, headers='keys', tablefmt='psql'))
            plt.plot(df_tempdate['Country'], df_tempdate['Confirmed'], label="Confirmed")
            plt.plot(df_tempdate['Country'], df_tempdate['Recovered'], label="Recovered")
            plt.plot(df_tempdate['Country'], df_tempdate['Deaths'], label="Deaths")
            plt.xlabel('Country')
            plt.ylabel('Cases')
            plt.title('Corona Trend _ On a Date')
            plt.legend()
            plt.show()

    def show_covid_result_country(self, country):
        df_tempcountry = self.df[self.df['Country'] == country]
        if df_tempcountry.empty:
            print("Invalid Country Name. Valid names are:")
            print(self.df['Country'].unique())
        else:
            print(tabulate(df_tempcountry, headers='keys', tablefmt='psql'))
            plt.plot(df_tempcountry['Date'], df_tempcountry['Confirmed'], label="Confirmed")
            plt.plot(df_tempcountry['Date'], df_tempcountry['Recovered'], label="Recovered")
            plt.plot(df_tempcountry['Date'], df_tempcountry['Deaths'], label="Deaths")
            plt.xlabel('Date')
            plt.ylabel('Cases')
            plt.title('Corona Trend_ For a Country')
            plt.legend()
            plt.show()

    def show_covid_result_countrywiselatest(self):
        date =[]
        lastestcoronarecord = self.df.tail(1)
        latestdate = lastestcoronarecord.values.tolist()
        df_tempdatecountry = self.df[self.df['Date'] == latestdate[0][0]]
        print(df_tempdatecountry)
        if df_tempdatecountry.empty:
            print("Incorrect data in record")
        else:
            print(tabulate(df_tempdatecountry, headers='keys', tablefmt='psql'))
            plt.plot(df_tempdatecountry['Country'], df_tempdatecountry['Confirmed'], label="Confirmed")
            plt.plot(df_tempdatecountry['Country'], df_tempdatecountry['Recovered'], label="Recovered")
            plt.plot(df_tempdatecountry['Country'], df_tempdatecountry['Deaths'], label="Deaths")
            plt.xlabel('Country')
            plt.ylabel('Cases')
            plt.title('Corona Trend _ On a Date')
            plt.legend()
            plt.show()



if __name__ == '__main__':

    option_Corona = {
        1: 'Corona Trend for a Date',
        2: 'Corona Trend for a Country',
        3: 'Country Wise latest number of Confirmed Case',
        4: 'Exit'
    }

    c = CovidTrend()

    while True:
        print(js.dumps(option_Corona, indent=4))
        choice = input("Enter your choice::::")

        if choice == "1":
            date = input("Enter the date for which you want to see the trend:")
            c.show_covid_result_date(date)
        elif choice == "2":
            country = input("Enter the Country Name for which you want to see the trend:")
            c.show_covid_result_country(country)
        elif choice == "3":
            c.show_covid_result_countrywiselatest()
        elif choice == "4":
            break
        else:
            print("Invalid choice!! Give numbers specified in the options")
