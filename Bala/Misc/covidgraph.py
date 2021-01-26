import pandas as pd
import matplotlib as mp

#covid = pd.read_csv(r'D:\My_Bala\My_Study\My_Python\My_Programs\GitRepo\AWS_Python\Bala\Misc\coviddata.csv')

url = r'https://covid.ourworldindata.org/data/owid-covid-data.csv'
coviddf = pd.read_csv(url)
print(coviddf.head(5))

cov_ind = coviddf[coviddf['iso_code'] == 'IND']
print(cov_ind.head(5))








