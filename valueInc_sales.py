#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 00:30:36 2024

@author: mac
"""

import pandas as pd

data = pd.read_csv('transaction2.csv' , sep=';')

data.info()

CostPerItem = 11.73
SellinPricePerItem=21.11
NumberofItemsPurchased=6

ProfitPerItem=21.11-11.73

ProfitPerItem=SellinPricePerItem-CostPerItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem

CostPerTransaction=NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction=NumberofItemsPurchased*SellinPricePerItem

CostPerItem = data['CostPerItem']

NumberofItemsPurchased=data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberofItemsPurchased

data['CostPerTransaction']= data['CostPerItem']*data['NumberOfItemsPurchased']

data['SalesPerTransaction']= data['SellingPricePerItem']*data['NumberOfItemsPurchased']

# PROFIT CALCULATION

data['ProfitPerTransaction']= data['SalesPerTransaction']-data['CostPerTransaction']

#data= data.drop("Profit",axis='columns')

data['Markup']=(data['ProfitPerTransaction'])/data['CostPerTransaction']

data['Markup']= round(data['Markup'],2)

# concatinating day month and year 

day=data['Day'].astype(str)

year=data['Year'].astype(str)

my_date=day+'-'+ data['Month']+'-'+year

data['Date']=my_date

data.iloc[10]


data.head(5)

data.info()

# spliting the clientKeyWords Column

split_col=data['ClientKeywords'].str.split(',' ,expand=True)

# splitimg the columns which are in the split_col variable

data['ClientAge']= split_col[0]
data['ClientType']=split_col[1]
data['LengthOfContract']=split_col[2]

data['ClientAge']=data['ClientAge'].str.replace('[' ,'')
data['LengthOfContract']=data['LengthOfContract'].str.replace(']' ,'')

# using the lower function on ItemDescription to make text lower

data['ItemDescription']=data['ItemDescription'].str.lower()


# How to merge files and bring new data set 

seasons_data=pd.read_csv('value_inc_seasons.csv',sep=';')

# merging files

data = pd.merge(data, seasons_data, on='Month')

# dropping columns as per the requirements 

# df = df.drop['ColumnName',axis=1]


data=data.drop('ClientKeywords',axis=1)
data=data.drop('Day',axis=1)

data=data.drop(['Year','Month'],axis=1)


# exporting the cleaned data into a csv

data.to_csv('ValueINC_cleaned.csv',index=False)