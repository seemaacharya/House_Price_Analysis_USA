# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:00:58 2023

@author: DELL
"""

#ABOUT THE DATASET-
#This dataset is collected from Kaggle, it contains the real estate listings in US.

#AIM OF THE PROJECT- Factors that could influence the residential home prices in USA over the next 10 years.

#COLUMNS-7 columns

#Avg. Area Income, Avg. Area House Age, Avg. Area Number of Rooms, Avg. Area Number of Bedrooms, Area Population,Price, Address.

#Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn


#loading the dataset
usa_homes=pd.read_csv("USA_Housing.csv")


#Reading the dataset
usa_homes
usa_homes.describe()
#5000 rows and 7 columns
usa_homes.count()

#Visual Analysis
sns.pairplot(usa_homes)

plt.figure(figsize=(12,6))
sns.scatterplot(x = usa_homes['Avg. Area Income'], y= usa_homes.Price)
plt.title('Relationship between Income and House Prices')
#highly correlated, meaning this could be the factor affecting the Price.

plt.figure(figsize=(12,6))
sns.scatterplot(x = usa_homes['Area Population'], y= usa_homes.Price)
plt.title('Relationship between Area Population and Home Prices ')
#highly correlated, meaning this could be the factor affecting the Price.

plt.figure(figsize=(12,7))
sns.scatterplot(x=usa_homes["Avg. Area Number of Bedrooms"], y= usa_homes.Price, color="green")
plt.title("The relationship between number of Bedrooms and price")
#highly correlated, meaning this could be the factor affecting the Price.

plt.figure(figsize=(12,7))
sns.scatterplot(x=usa_homes["Avg. Area Number of Rooms"], y= usa_homes.Price, color="green")
plt.title("The relationship between number of Living rooms and price")
#highly correlated, meaning this could be the factor affecting the Price.

plt.figure(figsize = (12,7))
sns.scatterplot(x=usa_homes["Avg. Area House Age"], y= usa_homes.Price, color="green")
plt.title("The relationship between House Age and price")
#highly correlated, meaning this could be the factor affecting the Price.









