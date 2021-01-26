import pycountry
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df1 = pd.read_csv(URL_DATASET)
#print(df1.head(3))  # Get first 3 entries in the dataframe
#df_india = df1[df1['Country'] == 'India']
#print(df_india.head(3))
URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df1 = pd.read_csv(URL_DATASET)
# print(df1.head(3))  # Uncomment to see the dataframe

#### ----- Step 2 (Select data for India)----
df_india = df1[df1['Country'] == 'India']
print(df_india.head(3))

#### ----- Step 3 (Plot data)----
# Increase size of plot
plt.rcParams["figure.figsize"]=20,20  # Remove if not on Jupyter
# Plot column 'Confirmed'
df_india.plot(kind = 'bar', x = 'Date', y = 'Confirmed', color = 'blue')

ax1 = plt.gca()
df_india.plot(kind = 'bar', x = 'Date', y = 'Deaths', color = 'red', ax = ax1)
plt.show()
