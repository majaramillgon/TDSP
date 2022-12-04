import pandas as pd
import mysql.connector

pwr = input()

mydb = mysql.connector.connect(
  host="sql7.freesqldatabase.com",
  user="sql7582498",
  password=pwr,
  database="sql7582498"
)

#mycursor = mydb.cursor()

query = 'SELECT * FROM climate_db'

result_dataFrame = pd.read_sql(query, mydb)