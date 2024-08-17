# analysis.py

import pandas as pd

def load_data(csv_path):
    """
        Loading the dataset from the CSV file.
        
        ARGS: csv file
        
        """
    car_data = pd.read_csv(csv_path)
    return car_data

def clean_data(car_data):
    """
        Clean the dataset by handling missing values and creating new columns.
        
        ARGS: dataset
    """
    # Fill missing values in 'paint_color' and 'is_4wd'
    car_data['paint_color'].fillna('unknown', inplace=True)
    car_data['is_4wd'] = car_data['is_4wd'].fillna(0).astype(int)

    # Convert 'date_posted' to datetime
    car_data['date_posted'] = pd.to_datetime(car_data['date_posted'], format='%Y-%m-%d')

    # Create a new 'manufacturer' column by extracting the first word of 'model'
    car_data['manufacturer'] = car_data['model'].str.split().str[0]

    return car_data

def get_manufacturers(car_data):
    """
        Return a list of unique manufacturers.
    
        ARGS: csv file
    """
    return car_data['manufacturer'].unique()

def filter_data_by_manufacturer(car_data, manufacturer_1, manufacturer_2):
    """
        Filter data by selected manufacturers.

        ARGS: csv file, user's choice of manufacturer.
    """
    return car_data[(car_data['manufacturer'] == manufacturer_1) | (car_data['manufacturer'] == manufacturer_2)]
