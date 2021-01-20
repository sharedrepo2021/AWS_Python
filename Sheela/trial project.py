import pyodbc
import pandas as pd
import faker
import json as js
import random
from tabulate import tabulate
import re


conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=BALALENG50\SQLEXPRESS;'
                              'Database=ADDRESSBOOK;'
                              'Trusted_Connection=yes;')

cursor = conn.cursor()
email = input("Enter email")

while not re.match("^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):

    print ("Error! Make sure you only use letters in your name")
    email = input("Enter email")
print("Hello " + email)
