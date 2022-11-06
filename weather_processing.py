"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries

import pandas as pd
import re
from datetime import datetime, date

# TODO Import the dataset 

path = r'./data/weather_dataset.data'

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index

data = pd.read_table(path, sep="\s+", parse_dates=[[0, 1, 2]])
data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr_Mo_Dy'])
data = data.set_index(['Yr_Mo_Dy'])

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them


def fix(item):
    match = re.match(r'\d+.\d+', str(item).replace(',', '.'))
    if match and float(match.group()) < 100:
        return float(match.group())
    return None


header = data.columns.to_list()

for column in header:
    data[column] = data[column].apply(fix)

# TODO Write a function in order to fix date (this relate only to the year info) and apply it


def fix_date(item: datetime):
    today = date.today()
    year = item.year - 100 if item.year > today.year else item.year
    return datetime(year, item.month, item.day)


data['datetime'] = data.index
data.index = data['datetime'].apply(fix_date)
del data['datetime']

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]

print(f'{data.index}\n')


# TODO Compute how many values are missing for each location over the entire record

for col in header:
    print(f' In column {col} is {data[col].isna().sum()} missing values')

# TODO Compute how many non-missing values there are in total

print(f'\n Total non-missing values in dataframe {data.notnull().sum().sum()}\n')

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times

print(f' The mean windspeed is {data.mean().mean()} \n')

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days

loc_stats = pd.DataFrame({
    'min': data.min(),
    'max': data.max(),
    'mean': data.mean(),
    'std': data.std()})
print(f'{loc_stats} \n')

# TODO Find the average windspeed in January for each location

print(f'Average windspeed in January \n '
      f'{data.loc[data.index.month == 1].mean()} \n')

# TODO Downsample the record to a yearly frequency for each location

print(f'{data.resample("Y").mean()} \n')

# TODO Downsample the record to a monthly frequency for each location

print(f'{data.resample("M").mean()} \n')

# TODO Downsample the record to a weekly frequency for each location

print(f'{data.resample("W").mean()} \n')

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks

weekly = data.resample('W').agg(['min', 'max', 'mean', 'std'])
print(weekly.loc[weekly.index[1:22]])
