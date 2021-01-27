import json as js
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt


class CovidGraph:
    def __init__(self):
        self.owid_url = r'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        self.covid_df = pd.read_csv(self.owid_url, usecols=['iso_code', 'continent', 'location', 'date', 'total_cases',
                                    'new_cases', 'total_deaths', 'new_deaths'], parse_dates=['date'])

        self.avail_countries = self.covid_df['location'].unique()
        self.covid_data = pd.DataFrame()

    def display_header(self):
        print('\n=================================================')
        print('|            Select Your Options                |')
        print('=================================================\n')

    def get_country(self):
        while True:
            self.covid_country = input('Enter the Country Name: ')
            if self.covid_country in self.avail_countries:
                break
            else:
                print('Enter the Correct Country Name: ')

    def get_dates(self):
        self.from_date = input('Enter From Date (mm/dd/yyyy): ')
        self.to_date = input('Enter To Date (mm/dd/yyyy): ')


    def generate_data(self):
        self.covid_data = self.covid_df[(self.covid_df['location'] == self.covid_country ) & (self.covid_df['date'] >= self.from_date) &
                                                 (self.covid_df['date'] <= self.to_date)]
        headers = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths',
                   'new_deaths']

    def generate_graph(self, col_name):
        _name_col = col_name
        _x_axis = list(self.covid_data['date'])
        _y_axis = list(self.covid_data[_name_col])
        plt.bar(_x_axis, _y_axis)
        plt.show()


if __name__ == '__main__':

    covid_graph = CovidGraph()

    options = {
        1: 'Trends by Total Cases',
        2: 'Trends by New Cases',
        3: 'Trends by Total Deaths',
        4: 'Trends by New Deaths',
        0: 'Exit'
    }

    while True:
        print(js.dumps(options, indent=2))
        opt = input("Select Your Option: ")

        covid_graph.get_country()
        covid_graph.get_dates()
        covid_graph.generate_data()

        if opt == '1':
            covid_graph.generate_graph('total_cases')
        elif opt == '2':
            covid_graph.generate_graph('new_cases')
        elif opt == '3':
            covid_graph.generate_graph('total_deaths')
        elif opt == '4':
            covid_graph.generate_graph('new_deaths')
        elif opt == '0':
            break
        else:
            print('An Invalid Option is Given. Please give correct option')
