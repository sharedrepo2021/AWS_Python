import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1HL1TR2\SQLEXPRESS;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

# cursor = conn.cursor()
# query = 'SELECT TOP 5 * FROM HumanResources.Employee'
# cursor.execute(query)
#
# for row in cursor:
#     print(row)

sql_query_df = pd.read_sql_query('SELECT TOP 5 * FROM HumanResources.Employee', conn)

print(sql_query_df['BusinessEntityID'])