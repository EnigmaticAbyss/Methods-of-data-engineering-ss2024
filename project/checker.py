import pandas as pd
import sqlite3
import os

# Construct the path to the database file
database_path = os.path.join('data', 'climate-change-earth-surface-temperature-data.db')
database_path1 = os.path.join('data', 'global-food-agriculture-statistics.db')

# Connect to the SQLite database
connection = sqlite3.connect(database_path)
connection1 = sqlite3.connect(database_path1)

# SQL query to select all data from a table
table_name = 'GlobalLandTemperaturesByCountry' 
table_name1 = 'fao_data_crops_data'  
# Replace with your table name either of these two tables are possible choices
query = f'SELECT * FROM {table_name}'
query1 = f'SELECT * FROM {table_name1}'
# query_l= [query,query1]

# Read the data into a pandas DataFrame
try:
    df = pd.read_sql_query(query, connection)
     
    print("First_table")
    print(df.head)
       
    unique_elements = df['Country'].nunique()
    print(unique_elements)

except sqlite3.Error as error:
    print(f"Error while executing the query: {error}")
finally:
    # Close the connection
                    connection.close()
    # Read the data into a pandas DataFrame
try:
    df = pd.read_sql_query(query1, connection1)
   

    print("Second_table")
    print(df.head)
    unique_elements = df['country_or_area'].nunique()
    print(unique_elements)

except sqlite3.Error as error:
    print(f"Error while executing the query: {error}")
finally:
    # Close the connection
                    connection1.close()
    