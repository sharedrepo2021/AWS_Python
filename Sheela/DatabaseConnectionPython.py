import pyodbc
import pandas as pd
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=BALALENOVO\SQLEXPRESS;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
'''
cursor.execute('SELECT TOP 5 FROM [AdventureWorks2019].[Person].[Person]')

for row in cursor:
    print(row)


sql_query = pd.read_sql_query('SELECT * FROM [AdventureWorks2019].[Person].[Person]', conn)
print(sql_query)
print(type(sql_query))

'''

cursor.execute("SELECT * FROM [AdventureWorks2019].INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")

for x in cursor:
  print(x)