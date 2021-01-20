from tabulate import tabulate
from numpy.random import randn
import pandas as pd


df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print('Initial DataFrame')
headers = ['INDEX', 'X', 'Y', 'Z']
print(tabulate(df, headers, tablefmt="fancy_grid"))


# Selection and Indexing and Pass a list of column names
print('\nValues in W Column')
print(df['W'])
print('\nValues in W and Z Column')
print(df[['W', 'Z']])


# Creating new columns
df['W+Y'] = df['W'] + df['Y']
df['Z+10'] = df['Z'] + 10
df['X-Y'] = df['X'].sub(df['Y'])
print('\nNew DataFrame')
headers = ['INDEX', 'W', 'X', 'Y', 'Z', 'W+Y', 'Z+10', 'X-Y']
print(tabulate(df, headers, tablefmt="fancy_grid"))


# Removing Column(s)
df.drop('W+Y', axis=1, inplace=True)
print('\nDataframe after Deleting an Column:')
headers = ['INDEX', 'W', 'X', 'Y', 'Z', 'Z+10', 'X-Y']
print(tabulate(df, headers, tablefmt="fancy_grid"))


# Removing Row(s)
df.drop('E', axis=0, inplace=True)
print('\nDataframe after Removing a Row')
headers = ['INDEX', 'W', 'X', 'Y', 'Z', 'Z+10', 'X-Y']
print(tabulate(df, headers, tablefmt="fancy_grid"))


# Selecting Rows
print('\nSelecting "A" Row')
print(df.loc['A'])
print('\nSelecting "C" Row')
print(df.iloc[2])


# Selecting subset of rows and columns
print('\nSelecting Subset of Row(B) and Column(Y)')
print(df.loc['B', 'Y'])
print('\nSelecting Subset of Rows(A & B) and Columns(W & Y)')
print(df.loc[['A', 'B'], ['W', 'Y']])


# Conditional Selection
df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print('\n\nInitial DataFrame')
headers = ['INDEX', 'W', 'X', 'Y', 'Z']

print(tabulate(df, headers, tablefmt="fancy_grid"))
print('\nSelecting the values GT Zeroes in BOOL')
print(tabulate((df > 0), headers, tablefmt="fancy_grid"))
print('\nSelecting the values LT Zeroes')
print(tabulate((df[df < 0]), headers, tablefmt="fancy_grid"))
print('\nSelecting the values in W Column LE Zeroes')
print(tabulate((df[df['W'] <= 0]), headers, tablefmt="fancy_grid"))
print('\nSelecting the values in Y Column where W GT Zeroes')
print(df[df['W'] > 0]['Y'])

print('\nSelecting the values using & operator', df[(df['W'] > 0) & (df['Y'] <= 0)])
print('\nSelecting the values in Y X Columns where W GT Zeroes', df[df['W'] > 0][['Y', 'X']])

#Index Details
df = pd.DataFrame(randn(5, 4), index='AA BB CC DD EE'.split(), columns='W X Y Z'.split())
headers = ['INDEX', 'W', 'X', 'Y', 'Z']
print('\n\nInitial DataFrame')
print(tabulate(df, headers, tablefmt="fancy_grid"))

# Reset to default 0,1...n index
df.reset_index(inplace=True)
print('\nAfter Reset DataFrame')
print(tabulate(df, headers, tablefmt="fancy_grid"))

#Set Index
newind = 'CA NY WY OR CO'.split()
df['States'] = newind
print('\n\nNew DataFrame: \n', df)
df.set_index('States',inplace=True)
print('\n\nSet DataFrame: \n', df)

#Missing Values
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print('\n\nInitial DataFrame: \n', df)

#dropna and fillna
df_new = df[df>0]
print('\n\nNew DataFrame: \n', df_new)
print('\n\nDrop NaN Values in the DataFrame: \n', df_new.dropna())
print('\n\nDrop NaN Values in the DataFrame: \n', df_new.dropna(axis=1))
print('\n\nDrop NaN Values in the DataFrame: \n', df_new.dropna(axis=1,thresh=3))
print('\n\nFill NaN Values in the DataFrame: \n', df_new.fillna(value='1.0'))