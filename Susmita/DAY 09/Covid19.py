import pycountry
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df1 = pd.read_csv(URL_DATASET)
country = input("Enter the country name:: ")
df_temp = df1[df1['Country'] == country]
days = int(input("How many days you want see:: "))
print(df_temp.tail(days))
#### ----- Step 3 (Plot data)----
# Increase size of plot
plt.rcParams["figure.figsize"] = 2, 2  # Remove if not on Jupyter
# Plot column 'Confirmed'

df_temp.plot(kind='bar', x='Date', y='Confirmed', color='blue')
ax1 = plt.gca()
df_temp.plot(kind='bar', x='Date', y='Deaths', color='red', ax=ax1)
plt.show()

df_temp.plot(kind='bar', x='Date', y='Recovered', color='green')
ax1 = plt.gca()
df_temp.plot(kind='bar', x='Date', y='Confirmed', color='red', ax=ax1)
plt.show()
