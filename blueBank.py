#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:20:59 2024

@author: mac
"""

import json
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# method 1 to load json data

json_file= open('loan_data_json.json')
data = json.load(json_file)


# other method to load json data
with open('loan_data_json.json') as json_file:
    data=json.load(json_file)
    #print(data)


# transforming list to dataframe

loanData=pd.DataFrame(data)

# finding the unique values for purpose column

loanData['purpose'].unique()


# describe the data

loanData.describe()

loanData['dti'].describe()
loanData['fico'].describe()

# using EXP to ge the annual income 

income=np.exp(loanData['log.annual.inc'])
loanData['Annual Income']=income

# FICO SCORE

fico = 250

if fico>=300 and fico<400:
    ficocat = 'very poor'
elif fico>=400 and fico<600:
    ficocat = 'Poor'
elif fico>=601 and fico<=660:
    ficocat='Fair'
elif fico>=660 and fico<700:
    ficocat='Good'
elif fico>=700:
    ficocat='Excellent'
else:
    ficocat= 'Unknown'
    
print(ficocat)


fruits = ['apple','pear','chickoo','banana','pineapple'] 

for x in fruits:
    print(x)
    y = x+ 'fruit'
    print(y)
    
    
for x in range(0,3):
    y = fruits[x]
    print(y)
    
    

# applying for loops in loan data

length = len(loanData)
ficocat = []

for x in range(0,length):
    category=loanData['fico'][x]
    
    try:
        if category>=300 and category< 400:
            cat='Very Poor'
        elif category>=400 and category< 600:
            cat='Poor'
        elif category>=600 and category < 700:
            cat='Good'
        elif category>=700:
            cat = 'Excellent'
        else:
            cat= 'Unknown'
    except:
        cat='Unknown Error'
    ficocat.append(cat)
    
ficocat=pd.Series(ficocat)

loanData['fico.category']= ficocat


# df.loc as conditional statements
# df.loc[df[columnanme],condition, 'newcolumnnane'] ='value if the condirional is met

# for interest rate a new column is wanted if the rate of interest is greater than point twelve percdnt (>0.12) then high or low 

loanData.loc[loanData['int.rate']>0.12,  'int.rate.type']='High'
loanData.loc[loanData['int.rate']<0.12,  'int.rate.type']='Low'


# number of rows by fico.category

catplot = loanData.groupby(['fico.category']).size()
catplot.plot.bar(color = 'red', width = 0.1)
plt.show()

purposeplot = loanData.groupby(['purpose']).size()
purposeplot.plot.bar(color='yellow',width=0.1)
plt.show()

# Scatter Plots

xpoint = loanData['dti']
ypoint = loanData['Annual Income']

plt.scatter(xpoint,ypoint)
plt.show()


# Writing to csv

loanData.to_csv('loan_cleaned.csv', index = True)