import pycountry
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'


class Covid:
    def __init__(self):
        self.country = None
        self.days = None
        self.df_temp = None

    def get_input(self):
        self.country = input("Enter the country name:: ")
        self.days = int(input("How many days you want see:: "))

    def show_covid_result(self):
        df1 = pd.read_csv(URL_DATASET)

        self.df_temp = df1[df1['Country'] == self.country]
        if self.df_temp.empty:
            print("Invalid Country Name. Valid names are:")
            print(df1['Country'].unique())

        print(self.df_temp.tail(self.days))

    def get_plot_options(self):
        print("Press 1 for Confirmed and Death graph")
        print("Press 2 for Confirmed and Recoverd graph")
        i = int(input("Enter options:: "))
        if i == 1:
            self.plot_confirm_death()
        elif i == 2:
            self.plot_confirm_recover()
        else:
            print("Invalid input...Exiting...")

    def plot_confirm_death(self):
        plt.rcParams["figure.figsize"] = 3, 3
        self.df_temp.plot(kind='bar', x='Date', y='Confirmed', color='blue')
        ax1 = plt.gca()
        self.df_temp.plot(kind='bar', x='Date', y='Deaths', color='red', ax=ax1)
        plt.show()

    def plot_confirm_recover(self):
        plt.rcParams["figure.figsize"] = 3, 3
        self.df_temp.plot(kind='bar', x='Date', y='Confirmed', color='green')
        ax1 = plt.gca()
        self.df_temp.plot(kind='bar', x='Date', y='Recovered', color='red', ax=ax1)
        plt.show()


if __name__ == '__main__':
    c = Covid()
    c.get_input()
    c.show_covid_result()
    c.get_plot_options()
