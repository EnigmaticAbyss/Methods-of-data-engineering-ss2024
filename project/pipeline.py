import os
import pandas as pd
from sqlalchemy import create_engine

# Kaggle dataset details
# Here we give two things in 
datasets = [
    {"dataset": "berkeleyearth/climate-change-earth-surface-temperature-data", "file": "GlobalLandTemperaturesByCountry.csv"},
    {"dataset": "unitednations/global-food-agriculture-statistics", "file": "fao_data_crops_data.csv"}
]


# Function to download datasets from Kaggle
def download_datasets():
    for ds in datasets:
        os.system(f"kaggle datasets download -d {ds['dataset']} -p /tmp")
        os.system(f"unzip -o /tmp/{ds['dataset'].split('/')[-1]}.zip -d /tmp")

# Function to transform and clean data
def transform_data(file_path):
    df = pd.read_csv(file_path)
    # Example transformation: drop missing values
    df = df.dropna()
    # Fix errors or apply any transformations as needed
    # Example: convert date columns to datetime
    for col in df.columns:
        if 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

# Function to save DataFrame to SQLite
def save_to_sqlite(df, db_name, table_name):
    engine = create_engine(f"sqlite:///data/{db_name}.db")
    df.to_sql(table_name, engine, index=False, if_exists='replace')

# Main pipeline execution
def main():
    # Ensure the /data directory exists
    os.makedirs('/data', exist_ok=True)
    
    # Download datasets
    download_datasets()
    
    # Process each dataset
    for ds in datasets:
        file_path = f"/tmp/{ds['file']}"
        df = transform_data(file_path)
        db_name = ds['dataset'].split('/')[-1]
        table_name = os.path.splitext(ds['file'])[0]
        save_to_sqlite(df, db_name, table_name)
        print(f"Processed and stored: {ds['file']}")

if __name__ == "__main__":
    main()





















# for this part you need to use kaggle api to get dataset 
# instruction on how to get API and use it can be found here : https://github.com/Kaggle/kaggle-api


# import subprocess
# import zipfile
# import os
# import shutil
# import pandas as pd
# import sqlite3
# import requests
# from io import StringIO


# # Get Everything done for first dataset
# # World Happiness Report up to 2022 (as described in project plan, we only use 2020 data as it was the year of Covid occurance)

# # First step : Download the Kaggle dataset using the Kaggle API
# # Define the command to download the dataset
# command = 'kaggle datasets download -d mathurinache/world-happiness-report'

# # Execute the command using subprocess
# subprocess.run(command, shell=True)

# # Path to the downloaded ZIP file
# zip_file_path = 'world-happiness-report.zip'

# # Destination folder for extracted files
# extract_folder = 'world-happiness-report'

# # Extract the contents of the ZIP file
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(extract_folder)

# # Access and read the CSV file
# csv_file_path = os.path.join(extract_folder, '2020.csv')  # Path to the CSV file


# # Read the CSV file into a pandas DataFrame
# happiness_df = pd.read_csv(csv_file_path)

# # Second step : Perform operations, fix errors, and manipulate the DataFrame as needed
# # happiness_df = happiness_df.dropna()  # Remove rows with missing values
# #useless_cols = ["Overall rank", "Score", "Generosity", "Perceptions of corruption"]
# #happiness_df.drop(useless_cols, axis = 1, inplace = True)
# #happiness_df.rename(columns={'Country name': 'Country_name'}, inplace=True)

# happiness_df.set_index('Country name', inplace= True)

# # Third step : Save DataFrame as SQLite Database in the /data directory
# data_folder = 'data'  # Relative path to the data directory

# # Create the /data directory if it doesn't exist
# if not os.path.exists(data_folder):
#     os.makedirs(data_folder)

# # SQLite database file path
# sqlite_file = os.path.join(data_folder, '2020report.sqlite')

# # Create a connection to SQLite database
# conn = sqlite3.connect(sqlite_file)

# # Store DataFrame in the SQLite database
# happiness_df.to_sql('world_happiness_2020', conn, index=False, if_exists='replace')

# # last step : time to clean up
# # Close the connection
# conn.close()

# # Delete the ZIP file and extracted folder
# os.remove(zip_file_path)
# shutil.rmtree(extract_folder)


# # Get Everything done for Second dataset
# # Novel Coronavirus (COVID-19) Cases Data

# # URL of the CSV file
# url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"

# # First step : Fetch the CSV data from the URL
# response = requests.get(url)
# data = response.content.decode('utf-8')

# # Read the CSV data using pandas
# df = pd.read_csv(StringIO(data))

# # Second Step : Perform operations, fix errors, and manipulate the DataFrame as needed
# # df = df.dropna()  # Remove rows with missing values

# df.drop(["Province/State","Lat", "Long"], axis = 1, inplace = True) # There are 3 unneccery column in file which we do not need

# # Grouping by 'Country/Region' and creating a new DataFrame
# grouped_df = df.groupby('Country/Region').sum().reset_index()

# # Assigning the grouped DataFrame back to the original 'df'
# # df = grouped_df.copy()
# # covid_df = df.groupby("Country/Region").sum() # summing up based on countries or region

# # Adding two new columns for further analyse
# countries = list(grouped_df.index)

# # first one is sum of infections in each country
# # sum values across all columns except the country column
# columns_to_sum = grouped_df.columns[1:]  # Exclude the first column (assuming it's the 'Country' column)

# # Creating a new column to store the sum for each country
# grouped_df['sum_for_each_country'] = grouped_df[columns_to_sum].sum(axis=1)

# # final dataset with countries name and sum for each country only
# selected_columns = ['Country/Region', 'sum_for_each_country']
# covid_df = grouped_df[selected_columns].copy()


# # Third step : Save DataFrame to SQLite database
# # Define the folder path
# folder_path = 'data'

# # Check if the folder exists, if not, create it
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# # Define the database path including the folder
# db_path = os.path.join(folder_path, 'covid_data.sqlite')

# # Save DataFrame to SQLite database in the data folder
# conn = sqlite3.connect(db_path)
# covid_df.to_sql('covid_cases', conn, if_exists='replace', index=False)

# # Time to clean up : Close the connection
# conn.close()


# # now I have joined two datasets based on mutual column to have my final dataset and go through it
# # Perform an inner join on the different columns
# # Check the column names in the DataFrames
# # print(covid_df.columns)
# # print(happiness_df.columns)
# merged_df = pd.merge(covid_df, happiness_df, left_on='Country/Region', right_on='Country name', how='inner')

# # final_dataset = covid_df.join(happiness_df, how = "inner")
# # Save Final DataFrame to SQLite database
# # Define the folder path
# folder_path = 'data'

# # Check if the folder exists, if not, create it
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# # Define the database path including the folder
# db_path = os.path.join(folder_path, 'final_dataset.sqlite')

# # Save DataFrame to SQLite database in the data folder
# conn = sqlite3.connect(db_path)
# merged_df.to_sql('final_table', conn, if_exists='replace', index=False)

# # Time to clean up : Close the connection
# conn.close()