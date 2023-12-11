DINOSAR DATA

import pandas as pd

#loading the data into pandas
df=pd.read_csv("dinosaur.csv")
print(df)

#deleting unwanted columns
df=df.drop("link", axis=1)
print("\nTable after removing the 'link' column:  ")
print(df)

Converting values from meter to feet
#renaming the column
df = df.rename(columns={'length': 'length_feet'})
print(df)

#converting the values from meter to feet
df['length_feet'] = df['length_feet']*3.28084
print(df['length_feet'])

#getting rounded value
df['length_feet'] = df['length_feet'].round(2)
print(df)

#dropping null value and displaying the final table
df.dropna(inplace=True)
print(df)


LAPTOP DATA

import pandas as pd

#Loading the data
df=pd.read_csv("laptopData.csv")
print(df)

#converting the weight to pounds
df['Weight'] = pd.to_numeric(df['Weight'].str.replace('kg',''), errors = 'coerce')
print(df)

#converting weight from kgs to pounds
df['Weight'] = df['Weight']*2.20462
print(df)

#getting rounded value
df['Weight'] = df['Weight'].round(2)
#adding 'lbs' after weights
df['Weight'] = df['Weight'].astype(str)+'lbs'
print(df)

#adding '$' sign to price
df['Price'] = '$' + df['Price'].astype(str)
print(df)

#removing null values and displaying the final table
df.dropna(inplace=True)
print(df)


PHONE DATA

#loading the data into pandas
import pandas as pd

df = pd.read_csv("phones.csv")
print(df)

#adding '$' sign to price columns
df['best_price'] = '$' + df['best_price'].astype(str)
df['highest_price'] = '$' + df['highest_price'].astype(str)
df['lowest_price'] = '$' + df['lowest_price'].astype(str)
print(df)

#dropping null value and displaying the final table
df.dropna(inplace=True)
print(df)


HOUSE DATA

import pandas as pd

#Loading the data
df = pd.read_csv("house.csv")
print(df)

#adding '$' sign
df['price'] = '$' + df['price'].astype(str)
print(df)

#dropping the null values and displaying the final table
df = df.dropna()
print(df)


HEROES INFORMATION

import pandas as pd

#loading the data
df=pd.read_csv("heroes_information.csv")
print(df)

#converting height from centimeter to feet
df['Height'] = df['Height']*0.0328084 
df['Height'] = df['Height'].round(2)
print(df)

#adding feet symbol 'ft'
df['Height'] = df['Height'].astype(str) + 'ft'
print(df)

#final table after removing null values
df = df.dropna()
print(df)


MARVEL MOVIES

import pandas as pd

#loading the data
df = pd.read_csv('marvel.csv')
print(df)

#removing the '$' symbol to get the total collection
df['North America'] = pd.to_numeric(df['North America'].str.replace('$',''), errors = 'coerce')
df['Other territories'] = pd.to_numeric(df['Other territories'].str.replace('$',''), errors = 'coerce')
df['Worldwide'] = pd.to_numeric(df['Worldwide'].str.replace('$',''), errors = 'coerce')
print(df)

#creating a new column by adding the columns to get the total wide collection
df['Total_collection'] = df['North America'] + df['Other territories'] + df['Worldwide']
print(df)

df['North America'] = '$' + df['North America'].astype(str)
df['Other territories'] = '$' + df['Other territories'].astype(str)
df['Worldwide'] = '$' + df['Worldwide'].astype(str)
df['Total_collection'] = '$' + df['Total_collection'].astype(str)

#final table after dropping null values
df = df.dropna()
print(df)
