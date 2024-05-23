import pandas as pd
import sqlite3
import os

# Construct the path to the database file
database_path = os.path.join('data', 'climate-change-earth-surface-temperature-data.db')

# Connect to the SQLite database
connection = sqlite3.connect(database_path)

# SQL query to select all data from a table
table_name = 'GlobalLandTemperaturesByCountry'  # Replace with your table name
query = f'SELECT * FROM {table_name}'

# Read the data into a pandas DataFrame
try:
    df = pd.read_sql_query(query, connection)
    print(df.head())
except sqlite3.Error as error:
    print(f"Error while executing the query: {error}")
finally:
    # Close the connection
    connection.close()
