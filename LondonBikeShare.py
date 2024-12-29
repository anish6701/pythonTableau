import pandas as pd

# Reading the data and storing it in a variable bikes
bikes= pd.read_csv("london_merged.csv")

# Explor the data 
# print(bikes.info())

# To count the number of rows and columns
bikes.shape


# count the unique value in the weather_code column
bikes.weather_code.value_counts()


# count the unique value in the season column
bikes.season.value_counts()


# Creating a dictionary and renaming the column names 


new_cols_dict={
    'timestamp':'time',
    'cnt':'count',
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}

# Renamed the column names below
bikes.rename(new_cols_dict, axis=1, inplace=True)

# Changing the humidity values to percentage (i.e a value between 0 and 1)

bikes.humidity_percent = bikes.humidity_percent /100

# creating a season dictionary so that we can map integers 0-3 to the actual written values

season_dict={
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}

# creating a weather dictionary so that we can map integers to actual written values
weather_dict={
    '1.0':'Clear',
    '2.0':'Scattered clouds',
    '3.0':'Broken clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with ThunderStorm',
    '26.0':'Snowfall'
}

# changing the seasons column data type to string
bikes.season = bikes.season.astype('str')

# mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)

# changing the weather column data type to string
bikes.weather = bikes.weather.astype('str')

# mapping the values 0-3 to the actual written seasons
bikes.weather = bikes.weather.map(weather_dict)

# Checking The dataframe bikes

print(bikes.head())

# writing final dataframe to an excel 

bikes.to_excel('london_bikes_final.xlsx', sheet_name = 'Data')
