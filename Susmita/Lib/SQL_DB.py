import pyodbc
import pandas as pd


class DBase:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.table_name = None

    def connect(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=DESKTOP-5H4SDFK\SQLEXPRESS;'
                                   'Database=LocalDB;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    def commit(self):
        _query = 'COMMIT'
        try:
            self.cursor.execute(_query)
        except pyodbc.ProgrammingError:
            pass
        except Exception as e:
            print('Unable to commit...')

    def disconnect(self):
        self.cursor.close()

    def execute_sql_and_commit(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print('Error in executing...Query: {}...Error: {}'.format(sql, e))
        else:
            self.commit()

    def execute_sql(self, sql):
        try:
            sql_query_df = pd.read_sql_query(sql, self.conn)
        except Exception as e:
            print('Unable to execute query: {}...Error: {}'.format(sql, e))
        else:
            return sql_query_df
