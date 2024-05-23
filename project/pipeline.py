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
def transform_data_first(file_path):
    df = pd.read_csv(file_path)
    # Example transformation: drop missing values
    df = df.dropna()
    # Fix errors or apply any transformations as needed
 # Load the data
  
    df = pd.read_csv(file_path)

    # Convert the 'dt' column to datetime format
    df['dt'] = pd.to_datetime(df['dt'])

    # Extract the year from the 'dt' column
    df['year'] = df['dt'].dt.year

    # Filter the data to include only years greater than 2010
    df_filtered = df[df['year'] > 1961]

    # Drop the 'AverageTemperatureUncertainty' column
    df_filtered = df_filtered.drop(columns=['AverageTemperatureUncertainty'])

    # Group by year and country, then calculate the average temperature
    df_grouped = df_filtered.groupby(['year', 'Country'])['AverageTemperature'].mean().reset_index()

    # Rename the columns for clarity
    df_grouped.rename(columns={'AverageTemperature': 'average_yearly_temperature'}, inplace=True)


    return df_grouped

def transform_data_second(file_path):
    df = pd.read_csv(file_path)
    # Example transformation: drop missing values
    df = df.dropna()
    # Fix errors or apply any transformations as needed
    # Example: convert date columns to datetime
    # Define the values you need in 'column2'
    values_needed = ['tonnes', 'Ha']

    # Filter the DataFrame
    filtered_df = df[df['unit'].isin(values_needed)]
    # Columns to drop
    columns_to_drop = ['element_code', 'value_footnotes']

    # Drop the specified columns
    df_dropped = filtered_df.drop(columns=columns_to_drop)
    # print(df_dropped)
    return df_dropped

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
    
    for index, ds in enumerate(datasets):
        file_path = f"/tmp/{ds['file']}"
        if index ==  0:
            df = transform_data_first(file_path)
        else:
            df = transform_data_second(file_path)
            
            
        db_name = ds['dataset'].split('/')[-1]
        table_name = os.path.splitext(ds['file'])[0]
        save_to_sqlite(df, db_name, table_name)
        print(f"Processed and stored: {ds['file']}")

if __name__ == "__main__":
    main()



